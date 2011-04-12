#!/usr/bin/env python

# Dan Goldin

# Based on http://cloudcarpenters.com/blog/amazon_products_api_request_signing/

import base64,hashlib,hmac,time,pprint
import xml.dom.minidom
from urllib import urlencode, urlopen
#from lxml import objectify

class amzn:
    base_url = "http://ecs.amazonaws.com/onca/xml"
    AWS_ACCESS_KEY_ID = '14YWVZGZ892Z61HAWFR2'
    AWS_SECRET_ACCESS_KEY = 'TT3mOBt9XaxeyeZt7MZSh03/CdaFUbizhOV4MoAq'

    def getItems(self,keywords):
        url_params = {'AWSAccessKeyId': self.AWS_ACCESS_KEY_ID, 'Keywords': keywords,
                      'Operation':"ItemSearch", 'SearchIndex': 'Books',
                      'Service':"AWSECommerceService",
                      'Timestamp': time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()), 
                      'Version':"2009-03-31",
                      'Availability':"Available",'Condition':"All",'ItemPage':"1",
                      'ResponseGroup':"Images,ItemAttributes,EditorialReview",
                      }
        dom = self.getData(url_params)
        #print dom.toprettyxml()

        items = dom.getElementsByTagName('Item')

        res = []
        for item in items:
            #print item.toprettyxml()
            titles = item.getElementsByTagName('Title')
            title = titles[0].childNodes[0].nodeValue
            print title

            dims = item.getElementsByTagName('ItemDimensions')
            height = length = width = weight = 0
            #if dims is not None and len(dims) > 0:
                #dims = dims[0]
                #height = dims.getElementsByTagName('Height')[0].childNodes[0].nodeValue
                #length = dims.getElementsByTagName('Length')[0].childNodes[0].nodeValue
                #width  = dims.getElementsByTagName('Width')[0].childNodes[0].nodeValue
                #weight = dims.getElementsByTagName('Weight')[0].childNodes[0].nodeValue

            
            print 'Dims', height, length, width, weight
            #exit()

            info = { 'title':title,
                     'height':height,
                     'length':length,
                     'width':width,
                     'weight':weight,
                     }

            images = item.getElementsByTagName('LargeImage')
            if images is not None and len(images) > 0:
                url = images[0].getElementsByTagName('URL')[0].childNodes[0].nodeValue

                webFile = urlopen(url)
                localFileName = url.split('/')[-1]
                localFile = open(localFileName, 'w')
                localFile.write(webFile.read())
                webFile.close()
                localFile.close()
                info['filename'] = localFileName
                info['success'] = True
            else:
                info['success'] = False
                print "Couldn't find image for",title
            res.append( info )
        return res

    def getData(self,url_params):
        # Sort the URL parameters by key
        keys = url_params.keys()
        keys.sort()

        # Get the values in the same order of the sorted keys
        values = map(url_params.get, keys)

        # Reconstruct the URL paramters and encode them
        url_string = urlencode(zip(keys,values))
        url_string = url_string.replace('+',"%20") 
        url_string = url_string.replace(':',"%3A") 

        # Construct the string to sign
        string_to_sign = """GET
ecs.amazonaws.com
/onca/xml
%s""" % url_string

        # Sign the request
        signature = hmac.new(
            key=self.AWS_SECRET_ACCESS_KEY,
            msg=string_to_sign,
            digestmod=hashlib.sha256).digest()
 
        # Base64 encode the signature
        signature = base64.encodestring(signature)

        # Make the signature URL safe
        signature = signature.replace('+','%2B')
        signature = signature.replace('=',"%3D")

        params = signature
        url_string += "&Signature=" + params

        x = urlopen("%s?%s" % (self.base_url,url_string))
        dom = xml.dom.minidom.parseString(x.read())
        return dom

if __name__ == '__main__':
    a = amzn()
    a.getItems('cakes')
