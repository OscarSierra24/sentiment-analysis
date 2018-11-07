#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:26:46 2018

@author: oscar
"""

def load_english_dict(route):
    with open('words.txt') as words:
        return set(words.read().split())
    
def load_tweeter_dict():
    pass

english_dict = load_english_dict('words.txt')
print(english_dict)