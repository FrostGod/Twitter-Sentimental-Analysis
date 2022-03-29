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


#Sentiment Analysis
def percentage(part,whole):
    return 100 * float(part)/float(whole)

def get_tweets(Topic):
    # keyword = input("Please enter keyword or hashtag to search: ")
    # noOfTweet = int(input ("Please enter how many tweets to analyze: "))
    noOfTweet = 10
    tweets = api.search_tweets(q=Topic, lang="en", count=noOfTweet)
    l = []
    cnt = 1
    for tweet in tweets:
        tweet.text = tweet.text.replace("\n", " ")
        l.append([cnt, tweet.text])
        cnt += 1
    return l
    # positive = 0
    # negative = 0
    # neutral = 0
    # polarity = 0
    # tweet_list = []
    # neutral_list = []
    # negative_list = []
    # positive_list = []
    # cnt = 0
    # for tweet in tweets:
    #     cnt += 1
    #     tweet_list.append(tweet.text)
    #     analysis = TextBlob(tweet.text)
    #     score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    #     neg = score['neg']
    #     neu = score['neu']
    #     pos = score['pos']
    #     comp = score['compound']
    #     polarity += analysis.sentiment.polarity
    #     if neg > pos:
    #         negative_list.append(tweet.text)
    #         negative += 1
    #     elif pos > neg:
    #         positive_list.append(tweet.text)
    #         positive += 1
    #     elif pos == neg:
    #         neutral_list.append(tweet.text)
    #         neutral += 1
    # print(cnt)
    # positive = percentage(positive, noOfTweet)
    # negative = percentage(negative, noOfTweet)
    # neutral = percentage(neutral, noOfTweet)
    # # polarity = percentage(polarity, noOfTweet)
    # positive = format(positive, '.1f')
    # negative = format(negative, '.1f')
    # neutral = format(neutral, '.1f')
    # print(positive, negative, neutral)

