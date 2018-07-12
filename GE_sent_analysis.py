# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:17:27 2018

@author: Mike
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:38:29 2018

@author: Mike
Running vader sentiment on "seek_alpha_ws_test.txt" >> A web scrape of 2 Earnings calls for GE

"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA
import re


analyzer = SIA()

#### Reading the whole documnet >> VaderSent reads the whole documnet >> Creates a list that stores sentiment values
sent_sentence = []
doc_line_count = []
#doc_list = []
file = "seek_alpha_ws_test.txt"
with open(file, "r") as fileinput:
    #sent_sentence = []
    for line in fileinput:
        #if re.search("Content:", line):
        if re.search("\[", line):
            line_count = None
            line = line.rstrip() # Strips the white space
            split_line = line.split(".")
            line_count = len(split_line)
            doc_line_count.append(line_count)
            for sent_line in split_line:
                sentiment = analyzer.polarity_scores(sent_line)
                sent_sentence.append(sentiment)
                #doc_list.append(sent_sentence)


#### Getting the docs from sent_sentence >> indexing by doc_line_count
ge_doc_1 = sent_sentence[0:446] #General Electric Company (GE) Presents At Electrical Products Group Conference (Transcript)
ge_doc_2 = sent_sentence[446:] #General Electric's (GE) CEO John Flannery on Q1 2018 Results - Earnings Call Transcript


#### This function is a loop that breaks down the list >> which has a dictonary inside
#### It takes the keys and puts each value into a corresponding list

###### For ge_doc_2
def doc_sent(doc):
    positive = []
    negative = []
    neutral = []
    compound = []
    i = 0
    for i in range(len(doc)):
       positive.append(doc[i]["pos"])
       negative.append(doc[i]["neg"])
       neutral.append(doc[i]["neu"])
       compound.append(doc[i]["compound"])
    
    
    ### Gets an average for the corresponding sentiment
    positive = sum(positive)/len(positive)
    negative = sum(negative)/len(negative)
    neutral = sum(neutral)/len(neutral)
    compound = sum(compound)/len(compound)
    
    ### Rounds the sentiment and turns it into a percent
    positive = round((positive *100),2)
    negative = round((negative *100),2)
    neutral = round((neutral *100),2)
    compound = round((compound *100),2)
    positive = "Positive: ", positive
    negative = "Negative: ", negative
    neutral = "Neutral: ", neutral
    compound = "Compound: ", compound
    return positive,negative,neutral,compound

## Creating variables that hold the sentiment from each corresponding document from the doc_sent function
GE_doc_1_sentiment = doc_sent(ge_doc_1)
GE_doc_2_sentiment = doc_sent(ge_doc_2)

## Seeing the results for each documents sentiment
print(GE_doc_1_sentiment)
print(GE_doc_2_sentiment)