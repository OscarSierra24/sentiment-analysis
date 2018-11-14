# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:39:11 2018

@author: danie
"""

import tweepy
import json
import os
import connect_db
from mongoengine import Document
from db_schema import Tweet
from words_filter import Words_filter
from sentiment_azure import sentiment

CONSUMER_KEY = os.environ['CONSUMER_KEY']#'So62vN1g4kNaNTPhv79yWLoU1'
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']#'blzEA9UaMpaczTL5HD3EqReKOSBGfdZXUIC00nP8POjMwtezj3'
OAUTH_TOKEN = os.environ['OAUTH_TOKEN']#'720704846135857152-hhGcmCCst5jag6GznKJw6zEwanItklv'
OAUTH_TOKEN_SECRET = os.environ['OAUTH_TOKEN_SECRET']#'UJnFf8EzQPJ4BNyB0jz5jvAomsufqMLKhbxF0T0gAwQAQ'


def auth(key, secret, token, token_secret):
    auth = tweepy.OAuthHandler(key, secret)
    auth.set_access_token(token, token_secret)
    return auth
    api = tweepy.API(auth)
    return api

def get_trends(api):
    #Uses United states code
    trends1 = api.trends_place(23424977) # 1 is for WW trends
    data = trends1[0] 
    trends = data['trends']
#    grab the name from each trend
    names = [trend['name'] for trend in trends]
    return names

if __name__ == '__main__':
    wf = Words_filter()
    
    #l = StdOutListener()
    auth = auth(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    OAUTH_TOKEN,
    OAUTH_TOKEN_SECRET
    )

    n = int(input("Number of tweets to get per hashtag: "))
    api  = tweepy.API(auth)
    for topic in get_trends(api):
        print(f"Gathering {n} tweets for {topic}")
        count = 0
        tmp_tweets = []
        for tweet in tweepy.Cursor(api.search,q=topic,lang="en").items():
            
            if count >= n:
                break
            # Parsing 
            decoded = tweet._json
            if 'extended_tweet' in decoded.keys():
                if 'text' in decoded['extended_tweet']:
                    text = decoded['extended_tweet']['full_text']
                else:
                    text = decoded['text']
            else:
                text = decoded['text']
            data = {
                'tweet_id'  : str(decoded['id']),
                'text': wf.filter(text),
                'topic':topic
            }
            tmp_tweets.append(data)
            count+=1

        tmp_tweets = sentiment(tmp_tweets)
        for data in tmp_tweets:
            Tweet(**data).save()