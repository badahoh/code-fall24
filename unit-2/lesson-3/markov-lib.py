import markovify
# # look at documentation for markofivy here: https://github.com/jsvine/markovify

text = open("2-text-artist.txt").read()

generator = markovify.Text(text, state_size=3) 
# normal state size is two 

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")