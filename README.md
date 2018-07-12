# Sentiment_Analysis_Earnings_Calls
Sentiment Analysis on publically traded companies earnings conference calls , to get an overall sentiment of the earnings calls from GE (General Electric) company executives.

The two conference calls are:
1) Title: General Electric Company (GE) Presents At Electrical Products Group Conference (Transcript) <br />
   Date of document: May 23, 2018  4:42 PM ET <br />
   
2) Title: General Electric's (GE) CEO John Flannery on Q1 2018 Results - Earnings Call Transcript <br />
   Date of document: Apr. 20, 2018  3:04 PM ET <br />

The files in this folder do as follows : <br />
1) GE_transcript_scrape.py >> This scrapes seeking alpha for two of GE's last earnings calls <br />
2) GE_sent_analysis.py >> This provides an overall sentiment analysis of each document <br />
3) seek_alpha_ws_test.txt >> This is the output from GE_transcript_scrape.py <br />
4) user_agents.csv >> A csv of 300 scraped User-agents from Chrome, Firefox and IE >> So the site thinks the program is a browser <br />
