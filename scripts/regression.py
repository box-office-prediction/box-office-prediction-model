"""
@author: sergio
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import (WEEKLY, DateFormatter, rrulewrapper, RRuleLocator, drange)
import statsmodels.api as sm
from sklearn import datasets


def linear_budget():
    data = pd.read_csv('budget_total_sorted.csv')
    y = data["budget"]
    X = data["boxoffice"]

    y = sm.add_constant(y)
    
    # Note the difference in argument order
    model = sm.OLS(X, y).fit()

    # Print out the statistics
    print(model.summary())


def linear_ratings():
    data = pd.read_csv('ratings_total.csv')
    y = data["ratings"]
    X = data["boxoffice"]

    y = sm.add_constant(y)
    
    # Note the difference in argument order
    model = sm.OLS(X, y).fit()

    # Print out the statistics
    print(model.summary())

def linear_trends():
    data = pd.read_csv('trends_total.csv')
    y = data["trends"]
    X = data["boxoffice"]

    y = sm.add_constant(y)
    
    # Note the difference in argument order
    model = sm.OLS(X, y).fit()

    # Print out the statistics
    print(model.summary())


def multiple_regression():
    data = pd.read_csv('multiple_regression.csv',delimiter=",")
    y = data[["budget","ratings","trends"]]
    X = data["boxoffice"]

    #y = data[["budget","trends"]]
  

    print('x =', X.shape)
    print('y =', y.shape)

    y = sm.add_constant(y)

    # Note the difference in argument order

    model = sm.OLS(X, y).fit()
    predictions = model.predict(y) # make the predictions by the model
    print(predictions)

    # Print out the statistics
    #print(model.summary())


def group_data():
    group_doc = open("multiple_regression1.csv", 'w')
    budget_list = list()
    ratings_list = list()
    trends_list = list()

    with open('movie_budget.txt') as f:
        for line in f:
            budget_list.append(line)

    with open('movie_ratings_avg.txt') as f:
        for line in f:
            ratings_list.append(line)

    with open('movie_trends.txt') as f:
        for line in f:
            trends_list.append(line)

    for i in range(100): 
        group_doc.write(str(budget_list[i]).replace("\n","") + "," + str(ratings_list[i]).replace("\n","") + "," + str(trends_list[i]).replace("\n","") + "\n")
    
    group_doc.close()


def main():
    #linear_budget()
    #linear_ratings()
    #linear_trends()
    #group_data()
    multiple_regression()

if __name__ == "__main__":
    main()