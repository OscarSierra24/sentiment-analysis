#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:26:44 2018

@author: oscar
"""

with open('english_dictionary.txt') as words:
    a = words.read().split()
    
for i in range(len(a)):
    a[i] = a[i].lower()
    #print(a[i])

file = open("lala.txt","w")
for i in range(len(a)):
    file.write(a[i]) 
file.close()