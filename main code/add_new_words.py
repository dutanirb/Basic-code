#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:18:14 2020

@author: sambhasan
"""

import numpy as np
import pandas as pd

from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.keyedvectors import KeyedVectors 
from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count

import chatbot_common

def get_new_word_embedding(new_word:str, samples:list):
    clean_samples= []
    for sample in samples :
        clean_samples += [chatbot_common.clean_text(sample).split()]
    cleaned_new_word = chatbot_common.clean_text(new_word)
    if cleaned_new_word != new_word:
        print('New word \'{}\' cleaned to \'{}\''.format(new_word, cleaned_new_word))
    new_word = cleaned_new_word
    new_words_lists = chatbot_common.get_new_words(samples)
    new_words_set = {word for sample in new_words_lists for word in sample}
    if all(new_words_lists):
        print('One or more samples does not have new any word\n{}'.format(new_words_lists))
        return False, False
    elif len(new_words_set) != 1:
        print('ERROR: multiple new words encountered\n{}'.format(new_words_lists))
        return False, False
    elif new_word not in new_words_set:
        print('New word passed does not match the word passed.\npassed: {}\nfound: {}'.format(new_word,new_words_set.pop()))
        return False, False
    glove2word2vec(glove_input_file= chatbot_common.__glove_file__, word2vec_output_file="gensim_glove_vectors.txt")
    glove_model = KeyedVectors.load_word2vec_format("gensim_glove_vectors.txt", binary=False)
    model1 = Word2Vec(clean_samples, min_count = 1, workers=cpu_count())
    embedding = np.round(model1[new_word][0:50], 4)
    return new_word, embedding

def add_new_words(project, new_words_file):
    chatbot_common.project = project
    chatbot_common.load_model()    
    new_words_df = pd.read_table(new_words_file)
    for word, samples in new_words_df.iterrows():
        if word in chatbot_common.model:
            continue
        new_word, embedding = get_new_word_embedding(word, samples)
        if not new_word:
            print('Adding word \'{}\' FAILED'.format(word))
            continue
        chatbot_common.add_word_to_model(new_word, embedding)
    chatbot_common.update_model()

if __name__ == '__main__':
    project = input('Enter project directory name: ')
    new_words_file = input ('Enter new words file name: ')
    add_new_words(project, new_words_file)
