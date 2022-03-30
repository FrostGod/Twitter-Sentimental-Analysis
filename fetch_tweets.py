# Import Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
# nltk.download('vader_lexicon')
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

# Authentication
consumerKey = "fgZXX9izK3wmATj8CBS1uUB1S"
consumerSecret = "crLXaX0MD9ukTA1ZQ7Z778Xw3uPyqtl6qYJPfguWypRwqA5jEj"
accessToken = "1507690242706653185-FAkodS3rLgOZWjmJQhMEv56JMeF0PI"
accessTokenSecret = "gRrHu56lifvuNC7DV0ZVmBvoAU9hWpWo9d1RcN7mHrf6P"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def get_tweets(Topic):
    noOfTweet = 10
    tweets = api.search_tweets(q=Topic, lang="en", count=noOfTweet)
    l = []
    cnt = 1
    for tweet in tweets:
        tweet.text = tweet.text.replace("\n", " ")
        l.append([cnt, tweet.text])
        cnt += 1
    return l

