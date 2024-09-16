import sys
from PIL import Image

# if len(sys.argv) != 2:
#      exit("This command requires one argument: the name of an image file")

# img = Image.open( sys.argv[1] )

# img.save( sys.argv[1] + ".jpg" )
# img.save( sys.argv[1] + ".gif" )
# img.save( sys.argv[1] + ".tiff" )
# img.save( sys.argv[1] + ".png" )








#####################################################################################
#####################################################################################
# PUT ONE red PIXEL

# img = Image.open( sys.argv[1] )
# one_pixel = img.getpixel( (0,0) )

# print(one_pixel)

# img.putpixel( (10,10), (255,0,0) )
# img.save("new.jpg")








#####################################################################################
#####################################################################################
# PUT ONE red PIXEL BUT MAKE IT A PNG

# img = Image.open( sys.argv[1] )
# one_pixel = img.getpixel( (0,0) )
# # variable is one_pixel 
# #0,0 most top left dot 
# # double parentheses 
# print(one_pixel)

# img.putpixel( (10,10), (255,0,0) )
# #rgb value 255,0,0 (red pixel)
# #output on terminal (39,141,204) 
# #put python3 classnotes.py cowfish.jpg on terminal 
# img.save("new.jpg")
# img.save("new.png")








#####################################################################################
#####################################################################################
# # FILTER PIXELS AS A LIST

# img = Image.open( sys.argv[1] )
# img_hsv = img.convert(mode="HSV")
# # hue saturation value 
# #img is a variable not python language 
# # green is python/ PIL library 
# # argument must be in quotes (mode="")
# img_hsv_data = img_hsv.getdata()
# #full image list 

# new_img_data = []
# for p in img_hsv_data: 
#     # p for pixel 
#     #hsv= saturation
#     print(p)
#     if p[2] < 55:
#         new_img_data.append( (255,255,255) ) 
#         # append is add to empty list 
#         #255,255,255 is wed 
#     else:
#         new_img_data.append(p)
#         # let regular pixel stay 


# img_hsv.putdata(new_img_data)
# #putting data into rgv and saving it 
# img_rgb = img_hsv.convert("RGB")
# img_rgb.save("filtered.jpg")





#####################################################################################
#####################################################################################
# ALTERNATIVE CODE FOR PIXEL FILTER

# img = Image.open( sys.argv[1] )

# img_hsv = img.convert(mode="HSV")

# (width,height) = img_hsv.size

# for x in range(width):
#     for y in range(height):
#         pixel = img_hsv.getpixel((x,y))
#         if pixel[2] < 55:
#             img_hsv.putpixel( (x,y), (255,255,255) )
# img_rgb = img_hsv.convert(mode="RGB")
# img_rgb.save("filtered-range.jpg")








#####################################################################################
#####################################################################################
# # GENERATE IMAGE  ---- TO RUN THIS FROM MY TERMINAL I WROTE
## python3 classnotes.py generative-1.jpg 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 10x10 image
# img = Image.new("RGB", (10,10) )

# img.save(sys.argv[1])












#####################################################################################
#####################################################################################
# # GENERATE IMAGE --- - Gradient ----  TO RUN THIS FROM MY TERMINAL I WROTE
## python3 classnotes.py generative-2.jpg 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 10x10 image
# img = Image.new("RGB", (10,10) )

# data = []
# for i in range(100):
#     pixel = (i, 0, 0)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])
# #newnewnew.jpg







# #####################################################################################
# #####################################################################################
# # # GENERATE IMAGE EX 1 - 400x400 ---- TO RUN THIS FROM MY TERMINAL I WROTE
# ## python3 classnotes.py generative-3.jpg 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# data = []
# for i in range(160000):
#     pixel = (i, 0, 255-i)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])
# #newnewnew.jpg

















#####################################################################################
#####################################################################################
# # EX 2+3 MODULO --- TO RUN THIS FROM MY TERMINAL I WROTE
# ## python3 classnotes.py generative-4.jpg 



# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )
# # coordinates 

# for y in range(400):

#     for x in range(400):

#         pixel = (x % 255, 0, y % 255)
#         #% modulo 
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])
# # restricting it to not increase by a certain point 















#####################################################################################
#####################################################################################
# # EX 4 MODULO / STRIPES --- TO RUN THIS FROM MY TERMINAL I WROTE
# ## python3 classnotes.py generative-5.jpg 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):
#     # range is size 

#     for x in range(400):

#         r = 0
#         b = 0
#         if x % 50 == 0:
#             # every 50 pixels are blue stripes
#             b = 255
            
#         if y % 20 == 0:
#             #every red is spaced by 20 pixels
#             r = 255

#         if y % 30 == 0:
#             # every violet stripes are spaced by 30 pixels 
#             r = 255
#             b = 255

#         pixel = (r, 0, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])


#####################################################################################
#####################################################################################
# # OTHER MODULO EXAMPLE --- TO RUN THIS FROM MY TERMINAL I WROTE
# ## python3 classnotes.py generative-6.jpg 

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 0
        g = 0
        b = 0
        if x % 50 > 25:
            r = 255

        if y % 50 > 25:
            b = 255

        if x % 100 > 50 and y % 100 > 50:
            g = 255
            #green

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )
#checking
img.save(sys.argv[1])













#####################################################################################
#####################################################################################
# # EX 5 IMAGE OVERLAY --- TO RUN THIS FROM MY TERMINAL I WROTE
# ## python3 classnotes.py haraway-dog-original.jpg punch-original.jpg

# if len(sys.argv) != 3:
#     exit("This program requires two arguments: the name of two image files to combine.")


# # open both images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )

# # make a new image 600x600, with a white background
# new_image = Image.new( "RGB", (400,400), "white" )

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# # paste in the second image, to (200,200)
# new_image.paste(img2, (20, 20) )

# # save the resulting image
# new_image.save("overlay-two-images.jpg")












#####################################################################################
#####################################################################################
# EX 6 IMAGE OVERLAY WITH TRANSPARENCY TO RUN THIS FROM MY TERMINAL I WROTE
## python3 classnotes.py haraway-dog-original.jpg punch-original.jpg

# if len(sys.argv) != 3:
#     exit("This program requires two arguments: the name of two image files to combine.")

# # open both images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )

# # make a new image 600x600, with a white background
# # Note that this image now has an "alpha" component
# new_image = Image.new( "RGBA", (400,150), "white" )

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# # add some transparency (alpha) to the second image
# img2.putalpha(128)

# # paste in the second image, preserving its new transparency
# new_image.alpha_composite(img2, (0,0) )

# # save the resulting image
# # Note that we must convert it to RGB with no alpha to save it as a JPEG
# new_image.convert("RGB").save("overlay-transparent.jpg")

# # Alternatively, we could have avoided converting by saving it to a
# # PNG like this (since PNGs allow alpha):
# # new_image.save("overlay-transparent.png")