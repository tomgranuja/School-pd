#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#from pandas import set_option ##
#set_option("display.max_rows", 16)
#LARGE_FIGSIZE = (12, 8)
FILE1='Alumnos_con_Cursos13_20161018_1028.csv'

def file_name_to_date(data_file):
    date = '-'.join(data_file.split('.')[0].split('_')[3:5])
    date = pd.to_datetime(date) #Timestamp type
    return date

def df_maker(data_file):
    table=pd.read_table(data_file, sep=',', encoding='latin1')
    date = file_name_to_date(data_file)
    date_col = [date for i in range(table.shape[0])] #future date column
    date_series = pd.Series(date_col)
    #Adding a new Timestamp column named 'date'
    table.loc[:,'date'] = pd.Series(date_col)
    table.set_index('date', inplace=True) #making it the index (useful??)
    return table

alumnos = df_maker(FILE1)

if __name__ == '__main__':
    print('{} rows in dataframe:'.format(len(alumnos)))
    print(alumnos.head(16))
    print('...')
