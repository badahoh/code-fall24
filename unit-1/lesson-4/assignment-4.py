# 
import sys
from PIL import Image
#Working with the code examples in the lesson 4 notes create your own image by building up patterns of pixels using the modulo operator and other techniques from those examples. Try 2-3 versions of this and make sure the output images are saved in your assignment-4 folder and labelled accordingly. 
 
if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 10x10 image
img = Image.new("RGB", (100,100) )

data = []
for i in range(1000):
    pixel = (i, 0, 0)
    data.append( pixel )

img.putdata(data)

img.save(sys.argv[1])
# #newnewnew.jpg 


# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         g = 0
#         b = 0
#         if x % 30 > 25:
#             r = 255

#         if y % 20 > 25:
#             b = 255

#         if x % 50 > 50 and y % 100 > 50:
#             g = 255
#             #green

#         pixel = (r, g, b)
#         img.putpixel( (x,y), pixel )
# #checking
# img.save(sys.argv[1]) 
# on terminal enter python3 assignment-4.py redgreen.jpg 



