### part 1 
#an argument is a value that is passed to a function or method when it is called. Arguments are the input data that a function needs to perform its tasks.
import sys 
print( sys.argv) 
#asking for arguments in the program 

print(len(sys.argv)) 



#part 2 
import sys 

data = [ 643, 452, 230, 219, 962, 532]

#wanting program to print 643 
#on terminal put python3 (filename) arguments.py 0 to find first number on the list
index = int(sys.argv[1])
# argv = arguments vector [1] = second number on the list 
# int= number (turn that into a number on the list)
print( data[index])


#part 3 
import sys 

data = [643, 452, 230, 219, 962, 532]

if len(sys.argv) < 2: 
    print("you forgot to type an argument")
    exit()

    index = int(sys.argv[1]) 


    import sys 
    from PIL import Image 

    img = Image.open( sys.argv[1]) 

    print("You typed the filename:" + sys.argv[1])
    print("This is a " + img.format)
    print(img.format_description)
    print(" Size :" + str(img.size))
#put in terminal python3 arguments.py image-2.jpg 
# first argument is arguments.py and second argument is image itself 