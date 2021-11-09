#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:04:42 2020

@author: anirban
"""
import pandas as pd
import chatbot_common


__file_name__ = 'QAconsolidated(GVSU)v10.xlsx'
__sheet_name__ = 'Sheet1'
__intent_column__ = 'INTENT'
__mainutterance_column__ = 'MAINUTTERANCE'
__phrasal_column__ = 'PHRASAL'


def detect_duplicates():
    data = read_excel_data 
    dfObj = pd.DataFrame(data)
    dup_shape = dfObj.pivot_table(index=['PHRASAL'], aggfunc='size')
    return dup_shape.sort_values(ascending=False)
    

if __name__ == '__main__':
    project = input ('Enter the project name: ')
    chatbot_common.project = project
    file_name = input('Enter file name: ')
    excel_data = pd.ExcelFile(project+"/"+file_name)
    read_excel_data = pd.read_excel(excel_data, sheet_name='Sheet1')
    fill_na = read_excel_data.ffill(axis = 0)
    groupby_mainutterance = fill_na.groupby('MAINUTTERANCE').groups
    for group in groupby_mainutterance:
        print(group) 
        print()
        #print(group)
        #group['MAINUTTERANCE'].isin(group['PHRASAL'])
    #checking_value = read_excel_data['exist'].values.tolist()
    #query = set(checking_value)
    #if False in read_excel_data['exist']:
        #print("the utterance is not there in phrasal")
    #else:
        #print("All utterances are mapped with phrasal and mainutterances column.")
    phrasals = excel_data.parse('Sheet1')[__phrasal_column__]
    new_duplicate_sentence = detect_duplicates()
    #new_duplicate_sentence = new_duplicate_sentence[new_duplicate_sentence > 1] 
    #identified_phrasals = list(new_duplicate_sentence.index.values)
    #print("We have identified %s mutliple times in the file." %identified_phrasals)
    '''df1 = read_excel_data.dropna(subset=[__intent_column__])
    df_phrasal_groups = df1.groupby(__phrasal_column__)
    multi_phrasal_warning = []
    multi_intent_warning = []
    for phrasal, phrasal_df in df_phrasal_groups:
        if phrasal_df[__intent_column__].nunique() != 1:
            multi_intent_warning.append('ERROR: \'{}\' have been mapped to multiple intents({})'.format(phrasal, phrasal_df[__intent_column__].unique()))
        elif len(phrasal_df) > 1:
            multi_phrasal_warning.append('WARNING: \'{}\' have been cited {} times with intent \'{}\''.format(phrasal, len(phrasal_df), phrasal_df[__intent_column__].iloc[0]))
    if multi_intent_warning:
        print ('\n'.join(multi_intent_warning))
    if multi_phrasal_warning:
        print ('\n'.join(multi_phrasal_warning))'''