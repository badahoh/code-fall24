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


# terminal results 
# {296: 2, 282: 72.0, 34853: 10036, 34665: 360, 271: 'Canon', 272: 'Canon EOS Rebel T6i', 315: 'KARINA', 274: 8, 306: '2024:05:07 12:32:44', 531: 2, 33432: '', 283: 72.0}
# 34853 GPSInfo
# 296 ResolutionUnit
# 34665 ExifOffset
# 271 Make
# 272 Model
# 283 YResolution
# 274 Orientation
# 306 DateTime
# 531 YCbCrPositioning
# 33432 Copyright
# 282 XResolution
# 315 Artist


# UNIT 2 
# for my unit 2 project I want to combine the lyrics of all the songs in one album to automatically write a new song/
