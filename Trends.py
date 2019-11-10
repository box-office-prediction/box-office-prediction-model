# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:53:08 2019

@author: deman
"""
from pytrends.request import TrendReq
import numpy as np



pytrend = TrendReq()
p = 'C:/Users/deman/.spyder-py3/Senior Research/box-office-prediction-model/movie_titles2.txt'
t = open('output.txt', 'w+')
with open(p, 'r') as f:
    list2 = []
    for item in f:
        number = 0 
        while number < 1:
            list2.append(str(item))
            number += 1
    #print(list2)
    #list1 = ['Avengers: Endgame', 'Joker', 'It 2']
    movies = []
    x = 0
    for i in list2:
        scores = []
        movies.append(i)
        kw_list=['Twitter', i]
        pytrend.build_payload(kw_list, timeframe = '2019-01-01 2019-11-04')
        interest_over_time_df = pytrend.interest_over_time()
        del interest_over_time_df['isPartial']
        a = np.array(interest_over_time_df[i])
        temp = 0
        for i in a:
            if i > temp:
                temp = i
                scores.append(temp)
                
        #t.write(str(temp))
        #t.write(movies[x])
        print(temp)
        print(movies[x])    
        
        x += 1
       
    
t.close()






#print(interest_over_time_df) 
#avng = np.array(interest_over_time_df['Avengers: Endgame'])
#jokr = np.array(interest_over_time_df['Joker'])
#it = np.array(interest_over_time_df['It 2'])
