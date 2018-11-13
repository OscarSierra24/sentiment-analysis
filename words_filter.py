#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:26:46 2018

@author: oscar
"""

import re
from Levenshtein import distance
from nltk import TweetTokenizer

class Words_filter:
    def __init__(self):
        self.english_dict = self._load_english_dict('english_dictionary.txt')
        self.twitter_dict = self._load_twitter_dict('twitter_dictionary.txt')
        
    def _load_english_dict(self, route):
        dictionary = {}
        with open(route) as words:
            aux = words.read().split()
        for i in range(len(aux)):
            dictionary[aux[i]] = 1
        return dictionary

#stores a dictionary with k,v where k = twitter slang and v = corrected words    
    def _load_twitter_dict(self, route):
        dictionary = {}
        with open(route) as words:
            aux = words.read().split('\n')

            for i in range(len(aux)-1):
                tmp = aux[i].split(";") 
                dictionary[tmp[0]] = tmp[1]
        return dictionary


    def get_correction(self, word):
      return min(self.english_dict, key=lambda x: distance(word, x))
    
    def filter(self, string):
        result = "" 
        for word in TweetTokenizer().tokenize(string):
            if len(word) < 1:
                result+=word
            #for word in word_tokenize(string):#filter(None, re.split("[., \-!?:]+", string)):
            #if its # or @  
            #print("word:", word)
            if len(word) >= 1:
                #if its a hashtag separate words
                if word[0] == "#":
                    aux = ""    
                    for char in word:
                        #separate
                        if char == "#":
                            pass
                        elif char.isupper():#perroAs
                            #if its in the english dictionary
                            if aux in self.english_dict:
                                result+= " " + aux
                                
                            #if its part of the twitter slang
                            elif aux in self.twitter_dict:
                                result+=" " + self.twitter_dict[aux]          
                            #if, by discarting we concluded that the word could be misspelled, then apply a levenshtein distance:
                            else:   
                                if len(word) > 3:
                                    result+=" " + self.get_correction(word)
                                else:
                                    result+=" " + word

                            aux=char.lower()
                        
                        else:
                            aux+=char.lower()
                    word = aux        
                
                #if its a name keep it that way
                elif word[0] == "@":
                    result+=word+" "
                    continue

            #if word is a website link:
            if len(word) >= 5 and word[0:5] == "https":
                result+=word+" "
                continue
                

            #if its in the english dictionary
            if word.lower() in self.english_dict:
                result+= word.lower()
                
                
            #if its part of the twitter slang
            elif word.lower() in self.twitter_dict:
                result+=self.twitter_dict[word.lower()]          
            #if, by discarting we concluded that the word could be misspelled, then apply a levenshtein distance:
            else:
                if len(word) > 3:
                    result+=self.get_correction(word)
                else:
                    result+=word
            result+=" "
        return result
        
if __name__=="__main__":
    string = "RT @RRN3: Well if THIS doesn't say everything then nothing does."
    words_filter = Words_filter()
    print(words_filter.filter(string))
    '''
    WordsFilter = Words_filter()
    text = "'text': RT @RRN3: Well if THIS doesn't say everything then nothing does.\n#blacklivesmatter\n#CountEveryVote\n#EveryVoteCounts\n#MLK #BLM #ElectionResu\u2026"
    print(text)
    '''