from PIL import Image, ImageDraw, ImageFont

#taking input for the watermark
text_input = input("Enter your text for watermark : ")
unicode_text = text_input

#selecting the font
font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
text_width, text_height = font.getsize(unicode_text)

#opening the image on which to do watermark
canvas = Image.open('B.png')

#making image editable
draw = ImageDraw.Draw(canvas)

#overiting over the image
x_cor = int(input("Enter the x_co-ordinate : "))
y_cor = int(input("Enter the y_co-ordinate : "))
color = input("Enter the color : ")
draw.text((x_cor, y_cor), unicode_text , color , font)

#saving it to a new file
canvas.save("unicode-text.png", "PNG")

#showing the image
canvas.show()