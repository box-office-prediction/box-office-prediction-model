# box-office-prediction-model

This is a project made by Sergio Armenta and Tommy Manfredi as part of their CSC-450 Senior Research course. The goal is this research is to create a box office prediction model using multiple regression. Budget, ratings and search volume data were scraped, refactored and analyzed to create this model. 

This repo is divided into three folders. Data is a collection of csv and txt files which contain data created and used by our code. Graphs contains a series of scatter plots made to analyze the model's results. Scripts contains all python scripts used to create this model. These folders serve to organize the data and improve readibility. 

As a disclaimer, running some of the scripts at their current state will fail because they have not been reconfigured to look for data inside the data folder. At the time of the scripts' creation, all files were under the same folder.

The project began by obtaining a list of the top hundred grossing movies 2019. A text file of the movies' titles was created. Using the box_office.py and budget.py, we were able to obtain these metrics. metadata.py was used to scrape OMDB for the movies' metadata. ratings.py and release.py serve to scrape the data of those metrics. reformat.py is used to reformat the dates for movies' release and ratings_avg.py is used to get the average number for the multiple rating scores. Trends.py is used to scrape Google Trends for search volume data. 

Next, the graph_budget.py, graph_release.py, graph_ratings.py and graph_trends.py serve to create the scatter plots found in the graphs folder.

Finally, regression.py makes linear regression models for all metrics and a combined multiple regression model using statsmodel. 