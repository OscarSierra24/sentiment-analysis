# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:24:32 2018

@author: daniela
"""
import tweepy
import json

CONSUMER_KEY = 'So62vN1g4kNaNTPhv79yWLoU1'
CONSUMER_SECRET = 'blzEA9UaMpaczTL5HD3EqReKOSBGfdZXUIC00nP8POjMwtezj3'
OAUTH_TOKEN = '720704846135857152-hhGcmCCst5jag6GznKJw6zEwanItklv'
OAUTH_TOKEN_SECRET = 'UJnFf8EzQPJ4BNyB0jz5jvAomsufqMLKhbxF0T0gAwQAQ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)


def get_trends():
    #Uses United states code
    trends1 = api.trends_place(23424977) # 1 is for WW trends
    data = trends1[0] 
    trends = data['trends']
#    grab the name from each trend
    names = [trend['name'] for trend in trends]
    return names
