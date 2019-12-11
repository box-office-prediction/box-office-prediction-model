"""
@author: sergio
"""
import numpy as np
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import (WEEKLY, DateFormatter, rrulewrapper, RRuleLocator, drange)

def group_data():
    group_doc = open("trends_total.csv", 'w')
    release_list = list()
    bo_list = list()

    with open('trends.txt') as f:
        for line in f:
            release_list.append(line)
    
    with open('movie_total_bo.txt') as f:
        for line in f:
            bo_list.append(line)

    for i in range(100): 
        group_doc.write(str(release_list[i]).replace("\n","") + "," + bo_list[i])
    
    group_doc.close()


def sort_group():
    sorted_list = list()
    sorted_date = open("trends_total_sorted.csv", 'w')
    with open('trends_total.csv') as fh:
        rd = csv.reader(fh,delimiter=',')
        for row in rd:
            sorted_list.append(str(sorted(rd, key=lambda row: int(row[0]), reverse=False)).replace('[','')
            .replace(']','').replace("'","").strip())
    
    for i in range(len(sorted_list)):
        sorted_date.write(sorted_list[i] + "\n")

    sorted_date.close()


def scatter_plot():

    #read data from csv
    data = pd.read_csv('trends_total_sorted.csv')
    data_date = data['trends']
    data_money = data['boxoffice']
    plt.scatter(data_date, data_money, s=5)
    plt.xlabel('Trends')
    plt.ylabel('Box Office')
    plt.title('Trends')
    plt.savefig('graph_trends_scatter.png')

def main():
    #group_data()
    #sort_group()
    scatter_plot()

if __name__ == "__main__":
    main()