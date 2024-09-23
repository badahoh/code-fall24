import sys
from PIL import Image

if len(sys.argv) != 3:
    #! is to say opposite 
    # could change to 4 
    exit("This command requires two arguments")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
# img3 = Image.open(sys.argv[3])

#three_img_blend = Image.blend(blended_img, img3, .2) 
#three_img_blend.save("blend3.jpg") 
# on terminal: python3 assignment3-2.py Image-1.jpg , image-1-B.jpg, image-1-A.jpg ?
blended_img = Image.blend(img1,img2,.5)
blended_img.save("blended.jpg")
# make sure images match up in size 
# only takes 3 arguments at a time 
# argv 1 being first image argc 2 being second image and third being the opacity 
