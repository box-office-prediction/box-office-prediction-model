"""
@author: sergio
"""
import requests
from bs4 import BeautifulSoup

#this function scrapes imdb for budget
def imdb_scraper(movie_id):
    response = requests.get("https://www.imdb.com/title/{}/?ref_=fn_al_tt_1".format(movie_id))
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_details = soup.find("div", {"id": "titleDetails"}).find_all("div", {"class": "txt-block"}) 
    budget = movie_details[6].get_text() 
    test = budget.split("\n")[1].split(":")[0]
    if test == "Budget":
        budget = budget.split("\n")[1].split(":")[1] 
    else:
        budget = "No Budget"
    movie_id = str(movie_id).replace("/title/","").replace("/","")
    return budget

    #this function get all movie IMDB ID's
def get_ids():
    movie_list = []
    with open('movie_ids.txt') as f:
        for line in f:
            line = str(line).strip('\n')
            movie_list.append(line)
    return movie_list

def main():
    movie_list = get_ids()

    budget_doc = open("movie_budget.txt", 'w')

    for i in range(len(movie_list)):
        budget = imdb_scraper(movie_list[i])
        budget = str(budget).replace('$','').replace(',','')
        print(movie_list[i])
        print(budget)
        budget_doc.write(budget + "\n")

    budget_doc.close()

if __name__ == "__main__":
    main()