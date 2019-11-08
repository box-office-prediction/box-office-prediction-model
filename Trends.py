# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:53:08 2019

@author: deman
"""
from pytrends.request import TrendReq
import numpy as np
import matplotlib.pyplot as plt


pytrend = TrendReq()

kw_list=['Avengers: Endgame', 'Joker', 'It 2','1234567']
pytrend.build_payload(kw_list, timeframe = '2019-01-01 2019-11-01')




#pytrend.get_historical_interest(kw_list, year_start=2019, month_start=10, day_start=1, year_end=2019, month_end=11, day_end=6,  cat=0, geo='', gprop='', sleep=0)

interest_over_time_df = pytrend.interest_over_time()
del interest_over_time_df['isPartial']
a = np.array(interest_over_time_df['Avengers: Endgame'])
jokr = np.array(interest_over_time_df['Joker'])
it = np.array(interest_over_time_df['It 2'])





print(interest_over_time_df) #interest_over_time_df
