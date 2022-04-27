#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:40:58 2020

@author: Anirban
"""

import csv
import pandas as pd
import numpy as np
import re

__special_char_re__ = re.compile('[/(){}\[\]\|@,;-]')
__other_char_re__ = re.compile('[^0-9a-z #+_]')

project = '.'
glove_file = 'dict_file.csv'
model = {}

def clean_text(text):
#        text: a string ;  return: modified initial string
    text = text.lower() # lowercase text
    text = __special_char_re__.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text.
    text = __other_char_re__.sub('', text) # substitute the matched string in BAD_SYMBOLS_RE with nothing. 
    text = " ".join(text.split())
    return text

def load_model():
    global model
    print("Loading Glove Model")
    # model = pd.read_table(gloveFile, sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE)
    model= {}
    try:
        with open(project + '/' + glove_file,'r', encoding="utf8") as f:
            for line in f:
                splitLine = line.split()
                word = splitLine[0]
                embedding = np.array([float(val) for val in splitLine[1:]])
                model[word] = embedding
    except Exception as e:
        print ('Loading {} failed. ERROR: {}'.format(project + '/' + glove_file, e))
        print ('Loading vanilla glove data.')
        with open('./vanilla/glove.6B.50d.txt','r', encoding="utf8") as f:
            for line in f:
                splitLine = line.split()
                word = splitLine[0]
                embedding = np.array([float(val) for val in splitLine[1:]])
                model[word] = embedding
                
    print("Done.",len(model)," words loaded!")
    
def get_new_words(samples):
    new_words_list = []
    clean_samples= []
    for sample in samples :
        clean_samples += [clean_text(sample).split()]
    for sample in clean_samples:
        new_words = []
        for word in sample:
            if word not in model:
                new_words.append(word)
        new_words_list.append(new_words)
    return new_words_list

def add_word_to_model(word:str, embedding:list):
    global model
    if word in model:
        print ('{} already in model. NOT UPDATING!!')
        return
    model[word] = embedding
    print('{} successfully added to model'.format(word))
    
def update_model():
    pd.DataFrame.from_dict(data=model, orient='index').to_csv(project + '/' + glove_file, header=False, sep = " ", quoting=csv.QUOTE_NONE)
    # with open(gloveFile,'r', encoding="utf8") as f:
    #     for word in model:
    #         f.write('{} {}\n'.format(word, ' '.join(model[word])))
    #     f.flush()
    print ('Model update success')
    
#-----------------------------------------------------------------------------#
