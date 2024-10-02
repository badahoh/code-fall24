 # start with sample folder 
# three folders with seperate images 
# 2 algorithms 
# pushed up to github before deadline 
# make folders that are themed 
# run algorithm on three folders separately 
 
# cute 
# sea creatures 
# baked goods 
# crayon shin chen
# combined or collaged sea creatures in the ocean
# perhaps including different color patterns and changing hue of pictures 
# create 3 different folders 
# gather images in each folder naming them with their themes 
# python file that randomly selects photos from this folder and combines them 
# manipulate images using codes from previous assignment
# apply same algorithm to 


#1. find a bunch of images (10)
#2.test data folder 
#3 1. file for first algorithm 2nd file for second algorithm 
#4 cd final project touch algo1.py touch algo2.py 
#5 drag folder into vs code and first import puthon image library 
#6 in algo 1 (import sys library)
#7 write a for loop that gets data from images-0 folder 
# change the top left corner, 40 pixel by 40 pixel 
# make those pixels red 
# save that image as algo-1.jpg  
###For Loop:
#Used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects.
#The loop executes a specific number of times, determined by the length of the sequence

import sys ?
import PIL ?
#
# create a variable that is empty, and can hold all of the new red images from my for loop 
redImages[]

redImages.append(img)
image.save(redImages[5])

# algo 2 import pillow 
# import random 
# write series of commands 
# gets 1 random image 
#decreases opacity of image 
# gets another image 
#decreases the opacity 
# puts second image over fist image 
# but pastes it so that it only covers the left 30% of the


# *** three different folders with images and apply both algorithms on each folder 

img1 = Image.open(image name )
img2 = Image.open(image name )

img1.resize((400,400))
img1.convert("RGB")

new_image = Image.new("RGB", (400,400), "blue")
# saving each image as blue 

img1.putalpha(200)
img2.putalpha(50)


new_image.paste(img,(0,0))

new_image.alpha_composite(0,0)

#im so confused 
# my brain hurts 
#ouch ouch 
# go on terminal to run code on two images 
#enter: python3 (name of file.py) (name of img.jpg) (name of img.jpg) *if it requires two arguments
