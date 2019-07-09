from PIL import Image

#opening the image
im1 = Image.open('A.png')
im2 = Image.open('C.png')
im3 = Image.open('B.png')

#appending image and saving to form a .gif
im1.save("out.gif", save_all=True, append_images=[im2, im3], duration=1000, loop=0)