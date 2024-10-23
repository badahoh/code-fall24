import sys
word_list = sys.argv 
data = [ 'badah', 'wants', 'to', 'code', 'better' ]
index = int(sys.argv)
print( data[index] )

#pop removes the element from the list at the specified index. i.e 0
word_list.pop(0)


word_list.sort()
print(word_list)

