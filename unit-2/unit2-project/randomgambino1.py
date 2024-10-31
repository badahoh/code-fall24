import pprint
import random

file = open("babyboy.txt").read().lower()

markovDictionary = {}

words = file.replace("\n"," ").split()

#pprint.pprint(words)

for (i, word) in enumerate(words):
    # i is index (placement of word), word is word in the lyric
   # print(i, word)
    
    if i == len(words) - 1:
       # print(i, len(words))
        # length of words (array)
        # if i is equal to length of words then stop the code 
        break

    next_word = words[i+1]
   # print( word, next_word)
    
    if word in markovDictionary:
        markovDictionary[word].append(next_word)
    else:
        markovDictionary[word] = [next_word]

# # print(markovDictionary)
# # use pretty print library to see dictionary more clearly
#pprint.pp(markovDictionary)
# 

# generate text from dictionary
chosenWord = random.choice(words)
generatedText = []
for i in range(66): # 
    if chosenWord == words[(len(words) - 1)]:
        chosenWord = words[0]
    else:
        generatedText.append(chosenWord)
        nextWord = random.choice(markovDictionary[chosenWord])
        chosenWord = nextWord

finalPrintOut = " ".join(generatedText)

print("\n\n\n")
print(finalPrintOut)
print("\n\n\n")

newfile = open("gambino1.txt", "w") #write
newfile.write(finalPrintOut) #taking outcome of generated text and saving it as a txt file
newfile.close()

# generating something new of probability of words by reading through text 