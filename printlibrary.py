import sys
import amzn
import imager

a = amzn.amzn()

args = ['cake', 'harry potter', 'booze', 'party', 'awesome', 'adventure']

#filenames = []
#for arg in args:
#    filenames.extend( a.getItems(arg) )

filenames = [u'71R33MNR2JL.gif', u'51lwWOSkSaL.jpg', u'51PhJ-JaJhL.jpg', u'51bSc-uOuuL.jpg', u'51Sqmx0K%2BoL.jpg', u'51uV9%2BDRt7L.jpg', u'51NIb-uly3L.jpg', u'51AGsuiuemL.jpg', u'513CFwNgzUL.jpg', u'51KdtJaQWNL.jpg', u'41v5r8HSynL.jpg', u'51ynI7I-qnL.jpg', u'51qKFVatzeL.jpg', u'5153Q6BMTNL.jpg', u'51nz3oK3YYL.jpg', u'515PAWDZTEL.jpg', u'51qGerE%2BdNL.jpg', u'51MH9T1MTGL.jpg', u'51tEo-u7pKL.jpg', u'41NNPY3KZ1L.jpg', u'51POE610W0L.jpg', u'41D6EfxyYLL.jpg', u'51ZUAygdXSL.jpg', u'41rkHE8OTjL.jpg', u'51ZX923DPEL.jpg', u'41FJ5pKOrCL.jpg', u'5165GT3HEYL.jpg', u'519Qg-XLMeL.jpg', u'51J3C2H9JJL.jpg', u'41Ki0KG1s0L.jpg', u'51DjjzBM7wL.jpg', u'51vWFoLX%2BEL.jpg', u'51Q2rRr3ghL.jpg', u'515L291209L.jpg', u'51lAKgrJuqL.jpg', u'51y48C3A6tL.jpg', u'51tp1a9d3gL.jpg', u'517%2BpsUoNTL.jpg', u'51DpE9g2jsL.jpg', u'61xHsGKD3IL.jpg', u'41cjTUD6qAL.jpg', u'41aazJ6TKTL.jpg', u'412ZLJTIRML.jpg', u'61OJFPRA1SL.jpg', u'41HAM4kN1OL.jpg', u'51ZwrFjHXFL.jpg', u'61G7pgieA4L.jpg', u'51Tsh83NqJL.jpg', u'51Tl7kuNiYL.jpg', u'51LjXtyEaDL.jpg', u'51vt33Bgq7L.jpg', u'31df-sOHABL.jpg', u'41QMNRD0DZL.jpg', u'51%2BF-pEfKFL.jpg', u'516uR%2Bul3bL.jpg', u'51j-V0EMR5L.jpg', u'41QLeNiFjyL.jpg', u'515WD1CSZBL.jpg', u'513EHvnh9mL.jpg', u'51HBQ8DK2RL.jpg']

print 'Files:',filenames

i = imager.imager()
for fn in filenames:
    i.loadImage(fn)

i.combineImages('out.jpg', 10)
