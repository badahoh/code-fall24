 
# * = everything under that file
from unit1lesson2 import *

#1 Write some code to find the smallest number in this list. What is it?

#.sort() means its sorting the list 
number_list.sort()
print(number_list[0])
       #answer is 175 
#square bracket for 0 or it will error 


#2 Write some code to find the smallest number in this list that is greater that 500. What is it?

n = number_list[0] 

if number_list[1] < 500:
    n = number_list[1]
    
for n in number_list: 
    if n > 500: 
        print(n)
        break #stops loop on first variable (make sure to indent or it will error)
    #answer nshows 501  


#3 % is remainder when one number is divided by another (ie. 10 % 3 equals 1)
for n in number_list: 
    # finding smallest even number x % 2 on the list 
    if n % 2 == 0: 
    #first = is checking for even number and second = is checking for smallest one  
        print(n) 
        break 
    #break is stopping at first answer on the list
    #answer is 176  


#4 what is the lastb word alphabetically? ]

word_list.sort()
print(word_list)
#first word on the list is academy
#answer is violation 
#sort list words in alphabetical order 

#5 write code to find longest word  
word_list.sort(key=len)
#length = len
#key access values in dictionary  and is similar to an index in a list
word_list.reverse()
print(word_list[0]) 
#answer came out as rehabilitation

