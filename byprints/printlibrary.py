import sys
import amzn
import imager
import csv

a = amzn.amzn()

c = csv.reader( open('amazon_history.csv','r'), delimiter=',', quotechar='"' )

header = None
rows = []
for row in c:
    if header is None:
        header = row
    else:
        rows.append(row)

title_idx = header.index('Title')
asin_idx = header.index('ASIN/ISBN')
format_idx = header.index('Format')
valid_fmts = ['Hardcover', 'Paperback', 'Mass Market Paperback', 'Spiral-bound']

keywords = []
for row in rows:
    if row[format_idx] in valid_fmts:
        print row[asin_idx], row[title_idx]
        keywords.append(row[asin_idx])

#keywords = [ keywords[0] ]

image_dir = 'images/'

#keywords = [ 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'white', 'grey', 'brown', 'black' ]

print keywords

filenames = []
#for kw in keywords:
#    res = a.getItems(kw)
#    filenames.extend( x['filename'] for x in res if x['success'])

#filenames = [u'71R33MNR2JL.gif', u'51lwWOSkSaL.jpg', u'51PhJ-JaJhL.jpg', u'51bSc-uOuuL.jpg', u'51Sqmx0K%2BoL.jpg', u'51uV9%2BDRt7L.jpg', u'51NIb-uly3L.jpg', u'51AGsuiuemL.jpg', u'513CFwNgzUL.jpg', u'51KdtJaQWNL.jpg', u'41v5r8HSynL.jpg', u'51ynI7I-qnL.jpg', u'51qKFVatzeL.jpg', u'5153Q6BMTNL.jpg', u'51nz3oK3YYL.jpg', u'515PAWDZTEL.jpg', u'51qGerE%2BdNL.jpg', u'51MH9T1MTGL.jpg', u'51tEo-u7pKL.jpg', u'41NNPY3KZ1L.jpg', u'51POE610W0L.jpg', u'41D6EfxyYLL.jpg', u'51ZUAygdXSL.jpg', u'41rkHE8OTjL.jpg', u'51ZX923DPEL.jpg', u'41FJ5pKOrCL.jpg', u'5165GT3HEYL.jpg', u'519Qg-XLMeL.jpg', u'51J3C2H9JJL.jpg', u'41Ki0KG1s0L.jpg', u'51DjjzBM7wL.jpg', u'51vWFoLX%2BEL.jpg', u'51Q2rRr3ghL.jpg', u'515L291209L.jpg', u'51lAKgrJuqL.jpg', u'51y48C3A6tL.jpg', u'51tp1a9d3gL.jpg', u'517%2BpsUoNTL.jpg', u'51DpE9g2jsL.jpg', u'61xHsGKD3IL.jpg', u'41cjTUD6qAL.jpg', u'41aazJ6TKTL.jpg', u'412ZLJTIRML.jpg', u'61OJFPRA1SL.jpg', u'41HAM4kN1OL.jpg', u'51ZwrFjHXFL.jpg', u'61G7pgieA4L.jpg', u'51Tsh83NqJL.jpg', u'51Tl7kuNiYL.jpg', u'51LjXtyEaDL.jpg', u'51vt33Bgq7L.jpg', u'31df-sOHABL.jpg', u'41QMNRD0DZL.jpg', u'51%2BF-pEfKFL.jpg', u'516uR%2Bul3bL.jpg', u'51j-V0EMR5L.jpg', u'41QLeNiFjyL.jpg', u'515WD1CSZBL.jpg', u'513EHvnh9mL.jpg', u'51HBQ8DK2RL.jpg']

#filenames = [u'31HmLW2g9kL.jpg', u'31P3ur44%2BlL.jpg', u'412N5Mg6FiL.jpg', u'41CeS0f8VPL.jpg', u'41FL7NN8ukL.jpg', u'41IuliR4ShL.jpg', u'41KKkwFxVuL.jpg', u'41PS15mXxwL.jpg', u'41TVbFLLzOL.jpg', u'41UCN-mtlKL.jpg', u'41X8p6ArW-L.jpg', u'41e87Pr4RJL.jpg', u'41nWtwpjsvL.jpg', u'41pj6qBIiML.jpg', u'41prwCOIxgL.jpg', u'41q88NvvNTL.jpg', u'41tP2BATDZL.jpg', u'41tZLI64elL.jpg', u'511AhbGRx1L.jpg', u'511O1a-mK6L.jpg', u'512kcH-YJpL.jpg', u'513FRTkR-dL.jpg', u'516%2BEYl0-SL.jpg', u'517OzfkYRsL.jpg', u'51Aw3Sx9cmL.jpg', u'51BB8tPy7SL.jpg', u'51FMEXVD2JL.jpg', u'51HJKVrzs9L.jpg', u'51KlaFOf6SL.jpg', u'51L3oFdAUAL.jpg', u'51MXMV44C4L.jpg', u'51N%2B8-Ak8qL.jpg', u'51NK7I%2BZi8L.jpg', u'51PDUYPGA5L.jpg', u'51QL5xQV7ML.jpg', u'51RESG8FXNL.jpg', u'51SrwilzQkL.jpg', u'51VlwtJsyGL.jpg', u'51XkS3OPuvL.jpg', u'51Ye-yHJd5L.jpg', u'51ZCSTHQQ9L.jpg', u'51d4B5U5G6L.jpg', u'51dGrFP6fzL.jpg', u'51f%2BDiB5GXL.jpg', u'51jLKJgexYL.jpg', u'51n%2Bo7GopaL.jpg', u'51oZuCzFqBL.jpg', u'51rfE76SLkL.jpg', u'51uwr76cK9L.jpg', u'61rw0q0YIxL.jpg']

#filenames = [u'21xcqR6YI-L.jpg', u'31HmLW2g9kL.jpg', u'31P3ur44%2BlL.jpg', u'410YwTpGLPL.jpg', u'411VhT2pCrL.jpg', u'412N5Mg6FiL.jpg', u'414s8%2BIT6rL.jpg', u'415gh2Ve7jL.jpg', u'417FZYpJZlL.jpg', u'41CeS0f8VPL.jpg', u'41FL7NN8ukL.jpg', u'41IuliR4ShL.jpg', u'41JIgBBVLyL.jpg', u'41KKkwFxVuL.jpg', u'41LpbBVPaSL.jpg', u'41PNYmFN0NL.jpg', u'41PS15mXxwL.jpg', u'41QafFXmJ2L.jpg', u'41TVbFLLzOL.jpg', u'41UCN-mtlKL.jpg', u'41Wk%2BkYWUvL.jpg', u'41X8p6ArW-L.jpg', u'41X9XqOBs0L.jpg', u'41XM9QWFPTL.jpg', u'41bxeTR41QL.jpg', u'41e87Pr4RJL.jpg', u'41kyJzse4FL.jpg', u'41nWtwpjsvL.jpg', u'41pj6qBIiML.jpg', u'41prwCOIxgL.jpg', u'41q88NvvNTL.jpg', u'41t5xfbSAcL.jpg', u'41tP2BATDZL.jpg', u'41tZLI64elL.jpg', u'511AhbGRx1L.jpg', u'511O1a-mK6L.jpg', u'511vF6Cst1L.jpg', u'512kcH-YJpL.jpg', u'513CficPVUL.jpg', u'513FRTkR-dL.jpg', u'513KJtgv0EL.jpg', u'516%2BEYl0-SL.jpg', u'516Ji73S4kL.jpg', u'51773ETF84L.jpg', u'517MUy57YpL.jpg', u'517OzfkYRsL.jpg', u'518TrjhMnqL.jpg', u'519iaAXOjqL.jpg', u'519wupNV0vL.jpg', u'519zX-AjXDL.jpg', u'51AEZBKJVNL.jpg', u'51ATyY94neL.jpg', u'51AURtljoOL.jpg', u'51Aw3Sx9cmL.jpg', u'51BB8tPy7SL.jpg', u'51CDbUtvMjL.jpg', u'51Ce4GvkwWL.jpg', u'51EYsWl89pL.jpg', u'51FMEXVD2JL.jpg', u'51GXNFJmwKL.jpg', u'51HJKVrzs9L.jpg', u'51KTJeLL0nL.jpg', u'51KXMHF23AL.jpg', u'51KlaFOf6SL.jpg', u'51L3oFdAUAL.jpg', u'51L7e1VhrwL.jpg', u'51MXMV44C4L.jpg', u'51N%2B8-Ak8qL.jpg', u'51NIEJhjdVL.jpg', u'51NK7I%2BZi8L.jpg', u'51NhoaOfnOL.jpg', u'51PDUYPGA5L.jpg', u'51QL5xQV7ML.jpg', u'51RESG8FXNL.jpg', u'51RS6BsVByL.jpg', u'51RTHQ857BL.jpg', u'51SrwilzQkL.jpg', u'51VSwypLFLL.jpg', u'51VlwtJsyGL.jpg', u'51Wp1Livu9L.jpg', u'51XTKsmVJKL.jpg', u'51XkS3OPuvL.jpg', u'51Ye-yHJd5L.jpg', u'51ZCSTHQQ9L.jpg', u'51d4B5U5G6L.jpg', u'51dGrFP6fzL.jpg', u'51f%2BDiB5GXL.jpg', u'51hQ0YT0XIL.jpg', u'51jLKJgexYL.jpg', u'51k-DbGFdoL.jpg', u'51lSItmeozL.jpg', u'51n%2Bo7GopaL.jpg', u'51nOs6q6iOL.jpg', u'51oZuCzFqBL.jpg', u'51pOUClPoHL.jpg', u'51pWi065fiL.jpg', u'51qhhIrjFNL.jpg', u'51rfE76SLkL.jpg', u'51sKz2IWezL.jpg', u'51tS0LMu2vL.jpg', u'51uwr76cK9L.jpg', u'51vpPvjBXoL.jpg', u'51wlrZg7mvL.jpg', u'51z5G2kJrLL.jpg', u'51zm9MndN5L.jpg', u'51zuUgkh02L.jpg', u'61P6PQATNTL.jpg', u'61epEsdbLQL.jpg', u'61rw0q0YIxL.jpg']

filenames = [u'316nGh%2BKzXL.jpg', u'319%2B9b52xML.jpg', u'41%2BSdl2La8L.jpg', u'41-tJ0h%2BajL.jpg', u'410tX-4dYAL.jpg', u'414-QZ6LMUL.jpg', u'414-mWgcbZL.jpg', u'41835RNT6ML.jpg', u'418pHnJLHLL.jpg', u'41L00el1QVL.jpg', u'41Mbe-QvUJL.jpg', u'41T7C1fQsVL.jpg', u'41W21jFwWpL.jpg', u'41Z7kQqG99L.jpg', u'41bIN3b1vOL.jpg', u'41cOuN5EclL.jpg', u'41fMC4Bu6NL.jpg', u'41rKxQGcOLL.jpg', u'41s2xaruwKL.jpg', u'41xSE5pTfVL.jpg', u'51-90OrjGFL.jpg', u'513M4EgnCqL.jpg', u'5170RHkgciL.jpg', u'5171YJMtcTL.jpg', u'517E1E0T4DL.jpg', u'518OSm7A04L.jpg', u'51A48UnwE-L.jpg', u'51AtHftrw0L.jpg', u'51Aw3Sx9cmL.jpg', u'51CPKmYrT4L.jpg', u'51DE8H8STKL.jpg', u'51EhMHEsEJL.jpg', u'51GJ3F92JTL.jpg', u'51GqlcW%2BWuL.jpg', u'51IE6iVmiyL.jpg', u'51KxEb%2BpSeL.jpg', u'51MMUYQ8PBL.jpg', u'51PT1ve6nLL.jpg', u'51QRjuTQU%2BL.jpg', u'51Rz2SMWiuL.jpg', u'51TqpnhlMfL.jpg', u'51X4P5WV7NL.jpg', u'51Y%2BAWeU8QL.jpg', u'51ZWM2BWY0L.jpg', u'51bfJbi7uaL.jpg', u'51cU87l6%2BeL.jpg', u'51d2dvp1EyL.jpg', u'51djzHFNzWL.jpg', u'51jyW8Lte%2BL.jpg', u'51mP0my1vAL.jpg', u'51pZYWZFkZL.jpg', u'51qul9M1NOL.jpg', u'51rJqftuHVL.jpg', u'51u6irYUgWL.jpg', u'51x-i5jDS7L.jpg', u'51xG5A2hd4L.jpg', u'51xUY9HBDHL.jpg', u'51y2Buh6%2BaL.jpg', u'51zYORiAUJL.jpg', u'61G6EBDJCKL.jpg', u'71YKFV56VFL.gif']

filenames.sort()

print 'Files:',filenames

i = imager.imager()
for fn in filenames:
    i.loadImage(image_dir + fn)

num_rows = i.calculateNumRows()

print 'Rows',num_rows

#num_rows = 6

i.combineImages('out.jpg', num_rows)
