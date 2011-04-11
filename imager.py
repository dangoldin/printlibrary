from PIL import Image, ImageFilter
import random, math

class imager:
    imgs = []

    def loadImage(self, filename):
        img = Image.open(filename)
        img = img.convert("RGBA")
        self.imgs.append(img)

    def combineImages(self, outfile, num_rows):
        images_per_row = int(math.ceil(len(self.imgs)/float(num_rows)))
        print 'Num Images',len(self.imgs),images_per_row

        imgs = []
        imgs.append([])
        dims = []
        dims.append([])
        tot_width = 0
        max_height = 0
        cnt = 0
        cur_row = 0
        for img in self.imgs:
            imgs[cur_row].append(img)
            dims[cur_row].append(img.size)
            cnt += 1
            if cnt == images_per_row:
                cur_row += 1
                cnt = 0
                dims.append([])
                imgs.append([])

        row_dims = []
        for row in dims:
            tot_width = max_height = 0
            for dim in row:
                (w,h) = dim
                tot_width += w
                if h > max_height:
                    max_height = h
            row_dims.append( (tot_width, max_height) )
        
        print 'Dims',dims
        print 'Row Dims', row_dims

        tot_width  = max([w for (w,h) in row_dims])
        max_height = sum([h for (w,h) in row_dims])

        print 'W + H', tot_width, max_height

        img = Image.new('RGBA', (tot_width, max_height), (255,255,255,0))

        cur_w = 0
        cnt = 0
        max_height = 0
        for r, row in enumerate(imgs):
            cur_w = 0
            max_height += row_dims[r][1]
            for c, im in enumerate(row):
                img.paste(im, (cur_w, max_height - im.size[1]) )
                cur_w += im.size[0]

        img.save(outfile)
