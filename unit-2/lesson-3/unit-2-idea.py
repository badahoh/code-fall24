# unit 2 project 
#  I want to write a code that would gather lyrics from few different albums and is able to differentiate certain to write a new set of lyrics for a song . Using Markov was really fascinating although I can't competely grasp how the code collects the words and structures the sentences that it does. But after I learn how it does I want to manipulate the code to be more specific and intentional when selecting certain words and phrases to conduct new songs for a new album.  
# Using notes for markov-no-lib file to collect probabilities of similar lyrics and avoiding repetition and inserting previous codes like randomness and generating random chosen words to insert in specific places. 
# import random 
# import sys 

#import pprint 
## "pretty print" to print dictionary in a clearer way  

#import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

caeser_response = requests.get("https://open.spotify.com/album/4uP43hIpmEEDuW7aOfiU2C")
gambino_response = requests.get("https://open.spotify.com/album/01MRGgNbfWrE291tQjw9ta")
sun_response = requests.get("https://open.spotify.com/album/2WtfCHRb8cy4a2x8vOMVkM")

# print(caeser_response)
# print(gambino_response)
# print(sun_response) 
print(response.text[:500]) 