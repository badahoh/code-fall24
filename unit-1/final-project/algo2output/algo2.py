import PIL 

from os import listdir, path
import random
from PIL import Image

# I want to import random from sea 
files = listdir("image-0")
#files.remove(".DS_Store")

random_file = random.choice(files)
#choosing random image from folder 
img = Image.open( path.join("image-0",random_file) ) 


# img1 = Image.open(image name )
# img2 = Image.open(image name )

# img1.resize((400,400))
# img1.convert("RGB") 
# # CONVERTING IMAGE SIZE SO THEYRE ALL THE SAME 
 

# #making blue square
# width = 400
# height = 400

# img = Image.new("RGB", (width,height), (0,0,255) )


# blending blue square with a random image 
# taking that blue blended image   
 

#making random white pixels on the image
# loop 500 times, and each time, pick a random x and a random y
# # and draw a pixel there
# for n in range(500):
    
#     ## even distribution
#     # x = int( random.random() * 100 )
#     # y = int( random.random() * 100 )

#     # ## gaussian distribution
#     # x = int( random.gauss(50,10) )
#     # y = int( random.gauss(50,10) )

#     ## gaussian distribution just for x
#     x = int( random.gauss(50,10) )
#     #y = int( random.random() * 100  )
#     y = int( random.gauss(50,10)  )

#     img.putpixel( (x,y), (255,255,255) )

# img.save("more-rando-gauss-x.png")

