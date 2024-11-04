import random 
import pprint 
import markovify

#text = open("sunceasergambino.txt").read()

#generator = markovify.Text(text)

# with open("sunceasergambino.txt") as f: 
#     text = f.read()

# generator = markovify.NewLineText(text) 


with open("sunceasergambino.txt") as f:
    text = f.read()

generator = markovify.Text(text)

paragraph = ""

for i in range(20):
    paragraph += str(generator.make_short_sentence(350))
    paragraph += " "
    word_to_replace = "I'm" "i'm" "i"
    new_word = "you're" "you're" "you"
    paragraph = paragraph.replace(word_to_replace, new_word)

print("\n\n\n")
print(paragraph)
print("\n\n\n") 

newfile = open("essay2.txt", "w") #write
newfile.write(paragraph) #taking outcome of generated text and saving it as a txt file
newfile.close()