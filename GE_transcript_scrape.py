# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:01:39 2018

@author: Mike

This file web scrapes Alpha Vantage for GE Earnings calls.  I picked GE because it has been (or was) a solid
company for the last 30+ years.  Also, I highly admire Jack Welsch for his ability to see the big picture
and grow GE like he did.

This program scrapes the site using a random User-Agent from a list (300 User-Agents) from Chrome, Firefox and IE

The program scrapes two documents:
1) Title: General Electric Company (GE) Presents At Electrical Products Group Conference (Transcript)
   Date of document: May 23, 2018  4:42 PM ET
   
2) Title: General Electric's (GE) CEO John Flannery on Q1 2018 Results - Earnings Call Transcript
   Date of document: Apr. 20, 2018  3:04 PM ET
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
from urllib.request import Request
from time import sleep
import pandas as pd
import random

## Base URL >> Seeking Alpha
url_base = "https://seekingalpha.com/"
## Dictonary >> of the rest of the urls >> for transcripts
trans_dict = {"GE_conf":"article/4176676-general-electric-company-ge-presents-electrical-products-group-conference-transcript",
             "GE_earn_Q1_18":"article/4164470-general-electrics-ge-ceo-john-flannery-q1-2018-results-earnings-call-transcript"}

url = url_base + list(trans_dict.values())[0]


### Function to clean up HTML tags inside body
def html_clean(text):
    cleaner = re.compile('<[^<]+?>')    
    cleaned_text = re.sub(cleaner, "", text)
    return cleaned_text

### Text File writing data to 
file_name = "seek_alpha_ws_test.txt"
f=open(file_name, "w")
#doc_title = "This is a test to scrape seeking alpha\n"
doc_title = "+-+-+-+-+-+-+-+-+-+\n"
f.write(doc_title)

#### Reading in the list of user agents
user_agent_list = pd.read_csv("user_agents.txt", delimiter = "|")
user_agent_list = list(user_agent_list.iloc[:,0])

### Used to get articles Articles >> Which would be like containers
req = Request(url, headers={
    'User-Agent': (random.choice(user_agent_list))})
uClient = uReq (req)  # sends GET request to URL
page_html = uClient.read ()  # reads returned data and puts it in a variable
uClient.close ()  # close the connection
page_soup = soup(page_html, "html.parser")
articles = page_soup.find("article") # For article body


#### This loop goes through the different url's in dictonrary
for key in range(len(trans_dict.values())):
    my_url = url_base + list(trans_dict.values())[key]
    print(my_url)
    req = Request(my_url, headers={
    'User-Agent': (random.choice(user_agent_list))})
    uClient = uReq (req)  # sends GET request to URL
    page_html = uClient.read ()  # reads returned data and puts it in a variable
    uClient.close ()  # close the connection
    ### Getting Articles >> Which would be like containers
    page_soup = soup(page_html, "html.parser")
    articles = page_soup.find("article") # For article body
    for article in articles:

        title_container = articles.find("h1", {"itemprop":"headline"}) # Title container
        title = title_container.text # Extracts title from container
    
        time_container = articles.find("time", {"itemprop":"datePublished"}) # Time container
        time = time_container.text # Extracts the Date and Time article was published
    
        body_container = articles.findAll("p")
        body = str(body_container) # Converts body_container resultset >> to a string
        body = html_clean(body) # Cleaning out the HTML tags
        body = body.replace("&amp;", "&")
        
    f.write("Title: \n"+title+"\nDate of document: \n"+time+"\nContent: \n"+body+"\n+-+-+-+-+-+-+-+-+-+\n")
    sleep(7)

f.close()