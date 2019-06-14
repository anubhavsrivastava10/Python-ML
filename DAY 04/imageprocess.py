from PIL import Image
import os
#opening an image
user_input = input("Enter the image name : ")
img = Image.open(user_input)
print(user_input)
#rotating image 90 clockwise
img_rotate=img.transpose(Image.ROTATE_270)
#croping the image to half
wid = img.width
leg = img.height
x = int(wid/2)
y = int(leg/2)
crop_im = img.crop(box=(0,0,x,y))
img.save('crop_img.jpg')
#creating thumbnail
img = Image.open("sample.jpg")
img.thumbnail((75, 75))
img.save('thumb_sample1.jpg')
#converting to grayscale
img_bw = Image.open("sample.jpg")
img_bw.convert(mode='L').save('sample1.jpg')