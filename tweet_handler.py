# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:39:11 2018

@author: danie
"""

import tweepy
import json

consumer_key = 'So62vN1g4kNaNTPhv79yWLoU1'
consumer_secret = 'blzEA9UaMpaczTL5HD3EqReKOSBGfdZXUIC00nP8POjMwtezj3'
access_token = '720704846135857152-INYIXn3M9mHrMU2uHQhs3D7nE4Lc5HA'
access_secret = 'TV1jg6lBs3bmUnwaBkMA2MEl1pZzFdQkTCvir3vD9P2P9'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Parsing 
        decoded = json.loads(data)
        if 'extended_tweet' in decoded.keys():
            if 'text' in decoded['extended_tweet']:
                text = decoded['extended_tweet']['text']
            else:
                text = decoded['text']
        else:
            text = decoded['text']
        data = {
            str(decoded['id'])  : text
        }

        print(data)
        
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    #Hashtag to stream
    stream.filter(track=["#electionresults2018"])
    
"""
import tweepy
import json

# Specify the account credentials in the following variables:
consumer_key = 'So62vN1g4kNaNTPhv79yWLoU1'
consumer_secret = 'blzEA9UaMpaczTL5HD3EqReKOSBGfdZXUIC00nP8POjMwtezj3'
access_token = '720704846135857152-INYIXn3M9mHrMU2uHQhs3D7nE4Lc5HA'
access_token_secret = 'TV1jg6lBs3bmUnwaBkMA2MEl1pZzFdQkTCvir3vD9P2P9'


# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Python"! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['Python'])
"""