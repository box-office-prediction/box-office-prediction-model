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
    group_doc = open("budget_total.csv", 'w')
    budget_list = list()
    bo_list = list()

    with open('movie_budget.txt') as f:
        for line in f:
            budget_list.append(line)
    
    with open('movie_total_bo.txt') as f:
        for line in f:
            bo_list.append(line)

    for i in range(100): 
        group_doc.write(str(budget_list[i]).replace("\n","") + "," + bo_list[i])
    
    group_doc.close()

def sort_group():
    sorted_list = list()
    sorted_date = open("budget_total_sorted.csv", 'w')
    
    with open('budget_total.csv') as fh:
        rd = csv.reader(fh,delimiter=',')
        for row in rd:
            sorted_list.append(str(sorted(rd, key=lambda row: int(row[0]), reverse=False)).replace('[','')
            .replace(']','').replace("'","").strip())
    
    for i in range(len(sorted_list)):
        sorted_date.write(sorted_list[i] + "\n")

    sorted_date.close()


def scatter_plot():
    #read data from csv
    data = pd.read_csv('budget_total_sorted.csv')
    data_date = data['budget']
    data_money = data['boxoffice']
    plt.scatter(data_date, data_money, s=2)
    plt.xlabel('Budget')
    plt.ylabel('Box Office')
    plt.title('Budget')
    plt.savefig('graph_budget_scatter.png')

def main():
    #group_data()
    #sort_group()
    scatter_plot()

if __name__ == "__main__":
    main()