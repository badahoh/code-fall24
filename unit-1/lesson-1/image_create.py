
from image_create.py import Image

# Print a blank line
print("\n")

# Prompt the user for some info
name = input("code-fall24: ")
size = int(input("333: "))
color = input("blue: ")

img = Image.new("RGB",(size,size),color)
img.save(blue + ".png")
