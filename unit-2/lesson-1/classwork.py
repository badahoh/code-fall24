mylist = ["badah", "is","coding"]
# variable called my list and set it equal to empty list 
# know its a list bc of square brackets 
# to see whats in my list print the variable 
    #print(mylist)
#python3 classwork.py (on terminal)
mylist.append("today")
#.append is adding stuff to the end of the list 
    #print(mylist)
badahinlist = "badah" in mylist 
#set another variable to check list / true or false statement 
#"in" is way to check 
    #print(badahinlist)
#printed true 


#dictionary 
#word and definition == key and value
TNS = { }
TNS["subject"] = "theory"
TNS["course"] = "code as a liberal art"
TNS["department"] = "eugene lang"
TNS["students"] = ["beimnet","badah", "kirsten","miranda"]
TNS["desk"] = ["apple", "laptop", "phone", "charger"]
# curly brackets
checkforapple = "apple" in TNS
# print(TNS)

print("~~~~~~\n~~~~~\n~~~~~~\n~~~~~~~\n~~~~~~\n~~~~~\n~~~~~~")
#just for visual line break between print
for key in TNS:
    print(key, "-->", TNS[key]) 
    # for key "subject" what is the value 
    #"-->" just as symbol to indicate 

TNS["total"] = 0
#adding more into forloop 
#updating value in the dictionary 
for item in TNS.items():
    # each pair of key and value is an item 
    #each key value is "each"
    print(item) 
    for each in item:
        if(type(each)is list):
            # seeing what type of data each key is in dictionary
            print("this is not a string, but there are",len(each),"items in this list!!")

            for i in each:
                TNS["total"] = TNS["total"] + 1
        if (type(each)is str):
            print("there are",len(each),"characters in this string:", each)
#make sure each "if" statement is in forloop to function properly
#TERMINAL RESULTS
# ~~~~~~
# ~~~~~
# ~~~~~~
# ~~~~~~~
# ~~~~~~
# ~~~~~
# ~~~~~~
# subject --> theory
# course --> code as a liberal art
# department --> eugene lang
# students --> ['beimnet', 'badah', 'kirsten', 'miranda']
# desk --> ['apple', 'laptop', 'phone', 'charger']
# ('subject', 'theory')
# there are 7 characters in this string: subject
# there are 6 characters in this string: theory
# ('course', 'code as a liberal art')
# there are 6 characters in this string: course
# there are 21 characters in this string: code as a liberal art
# ('department', 'eugene lang')
# there are 10 characters in this string: department
# there are 11 characters in this string: eugene lang
# ('students', ['beimnet', 'badah', 'kirsten', 'miranda'])
# there are 8 characters in this string: students
# this is not a string, but there are 4 items in this list!!
# ('desk', ['apple', 'laptop', 'phone', 'charger'])
# there are 4 characters in this string: desk
# this is not a string, but there are 4 items in this list!!
# ('total', 8)
# there are 5 characters in this string: total




# from os import listdir, path 
# from PIL import Image, ExifTags 
# #ExifTags is a library in PIL to help you sift through info

# files = listdir("images")
# img = Image.open(path.join("images","0.jpg"))
# exifData = img.getexif ()
# #exif data is all the metadata (landscape, coordinates,etc)
# print(exifData) 
# for key in img.getexif().keys():
#     print(key,ExifTags.TAGS[key])



#terminal shows description of image (what phone, coordinates, date and time, etc)

