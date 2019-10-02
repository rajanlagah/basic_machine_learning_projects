# sentiment_analysis

Steps
  - create twitter app
  - install dependencies 
  
# Created app 
https://developer.twitter.com/en/apps/16834664 sentiment_analysis_rox

# Install dependencies

- pip install tweepy 
  for accessing twetter api
- pip install textblob
  for sentimantal analysis 
  
 # exloring textBlob 
  ```
  from textblob import TextBlob
  wiki = TextBlob("I am leaning new things. I am sure will create something")
  wiki.sentiment.polarity
  
  // op
  0.3181818181818182
  ```
  
 wiki.sentiment.polarity give number b/w (-1,1) -1 for sad and 1 for happy  
