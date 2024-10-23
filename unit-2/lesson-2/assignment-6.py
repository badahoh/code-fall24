#1
import requests 

#import sys 

from bs4 import BeautifulSoup 

arts_response = requests.get("https://www.arts.gov/grants/research-awards/publicly-available-data-sources")

arts_soup_html = BeautifulSoup(arts_response.text, "html.parser")
# HTML parsing is the process of taking raw HTML code, reading it, and generating a DOM tree object structure from it

arts_soup_text = arts_soup_html.get_text()

arts_data = open ('arts.txt', 'w')
# 'w' means open this text in write mode 
arts_data.write(arts_soup_text)
arts_data.close()

#2 
# #arts_data.sort(key=len)
# arts_list= sys.argv
# arts_list.sort(key=len)
# print(arts_list) 
    #  #  tried sorting for longest word on the website but gave nothing 

def getTitles(soupdata):  
   titles = soupdata.select("h2")
   if titles:
     for t in titles:
       print(t.text)
      
print("Arts........")
getTitles(arts_soup_html)

# terminal prints 
# /Users/badaoh/code-fall24/unit-2/path/to/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
#   warnings.warn(
# Arts........
# Breadcrumb
# Universities and Non-Profit Organizations 


#WBM_response = requests.get("https://web.archive.org/")
# #WBM wayback machine 

#print(archive_response)
# terminal response <Response [503]>

# archive_soup_html = BeautifulSoup(archive_response.text, "html.parser")
# WBM_soup_html = BeautifulSoup(WBM_response.text, "html.parser")

# archive_soup_text = archive_soup_html.get_text()
# WBM_soup_text = WBM_soup_html.get_text()

# archive_data = open('archive.txt', 'w')
# archive_data.write(archive_soup_text)
# archive_data.close()

# WBM_data = open('archive-WBM.text', 'w')
# WBM_data.write(WBM_soup_text)
# WBM_data.close() 

# def getTitles(soupdata):  
#   titles = soupdata.select("h2")
#   if titles:
#     for t in titles:
#       print(t.text)
      
# print("Archive........")
# getTitles(archive_soup_html)
# print("Wayback Machine.........")
# getTitles(WBM_soup_html)


# # only printed /Users/badaoh/code-fall24/unit-2/path/to/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
#   warnings.warn(
# Archive........
# Wayback Machine.........   for archive website

