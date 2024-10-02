import sys
from os import listdir, path 
from PIL import Image

import random 
# python3 algo1.py shells (name of the image folder)
import random
# # i want to import random from shells

currentdirectory = sys.argv[1]
#sys.argv[1] means the user "1" is the second argument after the python file 
#using currentdirectory as a variable for sys.argv[1]

files = listdir(sys.argv[1])
# print(files)
files.remove(".DS_Store")

random_file = random.choice(files)
# random_file2 = random.choice(files)
print(random_file)
#print(random_file, random_file2)
##choosing random image from folder 
#img = Image.open( path.join(sys.argv[1],random_file) ) 
 


# Image.open(random_file)
# # img2 = Image.open(image name )

# random_file.resize((400,400))
# random_file.convert("RGB") 
# # CONVERTING IMAGE SIZE SO THEYRE ALL THE SAME 
 

#making blue square
width = 400
height = 400

img = Image.new("RGB", (width,height), (0,0,255) )

img.save("blue.jpg")


# #blending blue square with a random image taking that blue blended image   
 

width = 400
height = 400

img2 = Image.new("RGB", (width,height), (255,255,255) )

# loop 500 times, and each time, pick a random x and 
# a random y
# and draw a pixel there
for n in range(1000):
    
    ## even distribution
    # x = int( random.random() * 100 )
    # y = int( random.random() * 100 )

    # ## gaussian distribution
    # x = int( random.gauss(50,10) )
    # y = int( random.gauss(50,10) )

    ## gaussian distribution just for x
    x = int( random.gauss(100,80) )
    #y = int( random.random() * 100  )
    y = int( random.gauss(100,80)  )

    img2.putpixel( (x,y), (0,0,255) )
### scatter pixels are blue!!!

img2.save("scatter.jpg")




# if len(sys.argv) != 3:
#    # ! is to say opposite 
#    # could change to 4 
#    # exit("This command requires two arguments")

# img = Image.open( sys.argv[1] )
# img2= Image.open( sys.argv[1] )

# #three_img_blend = Image.blend(random_file, random_file2, .2) 
# #three_img_blend.save("blend3.jpg") 
# # on terminal: python3 algo1.py.py (can enter shells or sea instead of image files) Image-1.jpg , image-1-B.jpg, image-1-A.jpg ?
# blendedrandom_img = Image.blend("blue.jpg", "scatter.jpg",.5)
# blendedrandom_img.save("blueblended.jpg")