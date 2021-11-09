#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Anirban
"""
import pandas as pd

import chatbot_common

def get_new_word_report(samples:list):
    new_words = {}
    clean_samples= []
    for sample in samples:
        clean_samples += [chatbot_common.clean_text(sample).split()]
    new_words_lists = chatbot_common.get_new_words(samples)
    for new_words_list, sample, i in zip(new_words_lists, samples,range(len(samples))):
        for new_word in new_words_list:
            if new_word in new_words:
                new_words[new_word] += [{'position': i+2, 'utterance': sample}]
            else:
                new_words[new_word] = [{'position': i+2, 'utterance': sample}]
    return new_words

if __name__ == '__main__':
    import json
    project = input ('Enter the project name: ')
    chatbot_common.project = project
    chatbot_common.load_model()
    __sheet_name__ = 'Sheet1'
    __phrasal_column__ = 'PHRASAL'
    file_name = input('Enter file name: ')
    excel_data = pd.ExcelFile(file_name)
    phrasals = excel_data.parse('Sheet1')[__phrasal_column__]
    new_phrasal_words = get_new_word_report(phrasals)
    print(json.dumps(new_phrasal_words, indent= 2))
    
