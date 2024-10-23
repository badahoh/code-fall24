import random
import sys 

#import pprint 
## "pretty print" to print dictionary in a clearer way 

filename = sys.argv[1]
text = open(filename).read().lower().split()
markovDictionary = {}	



# use this function to get indexes for words
def getIndexForWord(wordFromLoop, nextPossibleWordsAmount): 
    possibleWordIndexes = []
    allWords = []
    for index, word in enumerate(text):
        if word == wordFromLoop:
            possibleWordIndexes.append(index)
    # print(wordFromLoop, "indexes:", possibleWordIndexes)
    return possibleWordIndexes[nextPossibleWordsAmount]





# build dictionary
totalWords = len(text)
for word in text:
    if not word in markovDictionary:
        markovDictionary[word] = []

    if text.index(word) == (totalWords - 1): break

    nextPossibleWordsAmount = len(markovDictionary[word]) 
    textIndex = getIndexForWord(word, nextPossibleWordsAmount)

    if word == text[(totalWords - 1)]:
        continue
    else:
        nextWord = text[textIndex + 1]
        markovDictionary[word].append(nextWord)

# print(markovDictionary)
# pprint.pprint(markovDictionary)
## allows printing big data objects into becoming more legible 



# generate text from dictionary
chosenWord = random.choice(text)
generatedText = []
for i in range(80): # 
    if chosenWord == text[(totalWords - 1)]:
        chosenWord = text[0]
    else:
        generatedText.append(chosenWord)
        nextWord = random.choice(markovDictionary[chosenWord])
        chosenWord = nextWord

finalPrintOut = " ".join(generatedText)

print("\n\n\n")
print(finalPrintOut)
print("\n\n\n")

# generating something new of probability of words by reading through text 