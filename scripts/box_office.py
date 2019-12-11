"""
@author: sergio
"""
import requests
from bs4 import BeautifulSoup

#this function scrapes box office mojo for box office
def mojo_scrape(movie_id):
    response = requests.get("https://www.boxofficemojo.com/title/{}/?ref_=bo_se_r_1".format(movie_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_money = soup.find_all("span", {"class": "money"})
    print(movie_money)
    domestic = movie_money[0].get_text()
    domestic = str(domestic).replace('$','').replace(',','')
    domestic = int(domestic)
    international = movie_money[1].get_text()
    international = str(international).replace('$','').replace(',','')
    international = int(international)
    #this checks whether the international field is empty, if it is, just take domestic into account
    #avoids error
    if (domestic == international):
        total = domestic
    else:
        total = domestic + international
    print(total)
    return total

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

    bo_doc = open("movie_total_bo.txt", 'w')

    for i in range(len(movie_list)):
        total_bo = mojo_scrape(movie_list[i])
        total_bo = str(total_bo).replace('$','').replace(',','')
        print(movie_list[i])
        print(total_bo)
        bo_doc.write(total_bo + "\n")

    bo_doc.close()


if __name__ == "__main__":
    main()