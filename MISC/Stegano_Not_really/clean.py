from PIL import Image, ImageFilter, ImageEnhance
import PIL.ImageOps
import numpy as np
import pytesseract

img = Image.open('./medias/base64.png')

width = img.size[0] 
height = img.size[1] 
for i in range(0,width):
    for j in range(0,height):

        data = img.getpixel((i,j))
        if (data[0]==255 and data[1]==255 and data[2]==255):
            img.putpixel((i,j),(0, 0, 0))


img = img.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(img)
img  = enhancer.enhance(2)


#img = PIL.ImageOps.invert(img)
#img = img.convert("1")

data = np.array(img)

#converted = np.where(data == 255, 0, 255)

#img = Image.fromarray(converted.astype('uint8'))

img.save('new_pic.png')
	
print(pytesseract.image_to_string(img))