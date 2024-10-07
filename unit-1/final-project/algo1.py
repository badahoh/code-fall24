import sys
from os import listdir, path 
from PIL import Image
# python3 algo1.py shells (name of the image folder)
import random
# # i want to import random from shells

currentdirectory = sys.argv[1]
#sys.argv[1] means the user "1" is the second argument after the python file 
#using currentdirectory as a variable for sys.argv[1]

files = listdir(sys.argv[1])
#print(files)
files.remove(".DS_Store")

random_file = random.choice(files)
random_file2 = random.choice(files)
print(random_file, random_file2)
#choosing random image from folder 
randomimage = Image.open( path.join(sys.argv[1],random_file) ) 
randomimage.thumbnail((400,400))
#thumbnail instead of resize 
randomimage2 = Image.open( path.join(sys.argv[1],random_file2) ) 
randomimage2.thumbnail((400,400))
# look at lesson4 excersise 6 
canvas = Image.new("RGB", (800,800), "white")
# need A in RGBA for transparency 
canvas.paste(randomimage,(0,0))
canvas.save("canvas.jpg")

# if len(sys.argv) != 3:
#     #! is to say opposite 
#    #could change to 4 
#     #exit("This command requires two arguments")

# random_file = Image.open( sys.argv[1] )
# random_file2 = Image.open( sys.argv[2] )
# img = Image.open(sys.argv[3])
# # (img is red stripes)

# two_img_blend = Image.blend(random_file, random_file2, .3) 
# two_img_blend.save("blend2random.jpg") 
## on terminal: python3 algo1.py.py (can enter shells or sea instead of image files) Image-1.jpg , image-1-B.jpg, image-1-A.jpg ?
# blendedrandom_img = Image.blend(random_file, random_file2, img, .3)
# blendedrandom_img.save("blended.jpg")
# # make sure images match up in size 
# # only takes 3 arguments at a time 
# # argv 1 being first image argv 2 being second image and third being the opacity 
# #blending images together 

# Image.open(path.join(currentdirectory,random_file ))
# Image.open(path.join(currentdirectory,random_file2 ))



# random_file.resize((400,400))
# random_file2.resize((400,400))
  #      keeps saying on terminal that AttributeError: 'str' object has no attribute 'resize'
  # make sure images are all png or jpg or there will be error 
# random_file.convert("RGBA") 
# random_file2.convert("RGBA") 
# CONVERTING IMAGE SIZE SO THEYRE ALL THE SAME 


# if len(sys.argv) != 3:
#     #! is to say opposite 
#    #could change to 4 
#     #exit("This command requires two arguments")

# random_file = Image.open( sys.argv[1] )
# random_file2 = Image.open( sys.argv[2] )
# img = Image.open(sys.argv[3])
# # (img is red stripes)

# three_img_blend = Image.blend(random_file, random_file2,img, .3) 
# three_img_blend.save("blend3.jpg") 
# on terminal: python3 algo1.py.py (can enter shells or sea instead of image files) Image-1.jpg , image-1-B.jpg, image-1-A.jpg ?
# blendedrandom_img = Image.blend(random_file, random_file2, img, .3)
# blendedrandom_img.save("blended.jpg")
# # make sure images match up in size 
# # only takes 3 arguments at a time 
# # argv 1 being first image argv 2 being second image and third being the opacity 
# #blending images together 

# # # then taking two sets of blended images and blending them together 



# #### TRYING TO PUT RED AND STRIPES BLENDED ONTO THE IMAGES WITH LESS HUE 
# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         g = 0
#         b = 0
#         if x %  50 > 25:
#             r = 255

#         if y % 50  > 25:
#             b = 0

#         if x % 100 > 50 and y % 100 > 50:
#             g = 0
#             #green

#         pixel = (r, g, b)
#         img.putpixel( (x,y), pixel )
# #checking
# img.save("redstripes.jpg") 
# # on terminal enter python3 assignment-4.py redgreen.jpg 




 

