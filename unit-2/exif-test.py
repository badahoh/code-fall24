from os import listdir , path 
from PIL import Image, ExifTags 
 #ExifTags is a library in PIL to help you sift through info
files= listdir("images")
img = Image.open(path.join("images","fin.jpg"))
exifData = img.getexif ()
#exif data is all the metadata (landscape, coordinates,etc)
print(exifData) 
for key in img.getexif().keys():
    print(key,ExifTags.TAGS[key])
