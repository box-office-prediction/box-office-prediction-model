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

#this function groups metric and box office data
def group_data():
    group_doc = open("release_total.csv", 'w')
    release_list = list()
    bo_list = list()

    with open('movie_release_reformatted.txt') as f:
        for line in f:
            release_list.append(line)
    
    with open('movie_total_bo.txt') as f:
        for line in f:
            bo_list.append(line)

    for i in range(100): 
        group_doc.write(str(release_list[i]).replace("\n","") + "," + bo_list[i])
    
    group_doc.close()

#this function sorts the data to be able to create scatter plot
def sort_group():
    sorted_list = list()
    sorted_date = open("release_total_sorted.csv", 'w')
    with open('release_total.csv') as fh:
        rd = csv.reader(fh,delimiter=',')
        for row in rd:
            sorted_list.append(str(sorted(rd, key=lambda row: datetime.strptime(row[0], "%m/%d/%Y"), reverse=False)).replace('[','')
            .replace(']','').replace("'","").strip())
    
    for i in range(len(sorted_list)):
        sorted_date.write(sorted_list[i] + "\n")

    sorted_date.close()

#this function creates the scatter plot
def scatter_plot():

    #read data from csv
    data = pd.read_csv('release_total_sorted.csv')
    data_date = data['datetime']
    data_money = data['boxoffice']
    plt.scatter(data_date, data_money, s=5)
    plt.xlabel('Date')
    plt.ylabel('Box Office')
    plt.title('Release Date')
    plt.xticks(["01/04/2019","02/01/2019","03/01/2019","04/05/2019","05/03/2019","06/07/2019","07/03/2019","08/02/2019","09/06/2019","10/04/2019"],fontsize=7,rotation=30)
    plt.savefig('graph_release_scatter.png')

def main():
    #group_data()
    #sort_group()
    scatter_plot()

if __name__ == "__main__":
    main()