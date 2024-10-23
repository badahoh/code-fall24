#3 
import markovify

text = open("coding_notes.txt").read()

generator = markovify.Text(text)

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")

# terminal response fun fun 
## Thus we see fit. As someone who’s been using different softwares as designs as their own. Thus we see fit. Using a semicolon and colon. I’ve always thought of how everything is interconnected to one another. Thus we see fit. It made me trace back to all the technologies are unaffected by their presence. Using a semicolon and colon. If that is the way it is. The first part of the one big truth — the truth is all that matters. 


# result after changing range (5) and number in paragraph (90)
# 
# As someone who’s been using different softwares as designs as their own. In pursuit of the one big truth — the truth is all that matters. Thus we see fit. The first part of my creative processes I guess I’ve been living in but have yet to grasp. Using a semicolon and colon. 

# #
#4 
### I want to write a code that would gather lyrics from my favorite album and is able to differentiate certain to write a new set of lyrics for a song . Using Markov was really fascinating although I can't competely grasp how the code collects the words and structures the sentences that it does. But after I learn how it does I want to manipulate the code to be more specific and intentional when selecting certain words and phrases to conduct a new song. 