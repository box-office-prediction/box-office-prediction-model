"""
@author: sergio
"""
from omdbapi.movie_search import GetMovie
import os

def ratings(movie_title):
    API_KEY = os.environ('OMDB_KEY')
    movie = GetMovie(title=movie_title, api_key=API_KEY)

    ratings = movie.get_data('Ratings')

    return ratings

#this function get all movie titles
def get_titles():
    movie_list = []
    with open('movie_titles.txt') as f:
        for line in f:
            line = str(line).strip('\n')
            movie_list.append(line)
    return movie_list

def main():
    movie_list = get_titles()

    ratings_doc = open("movie_ratings.csv", 'w')

    for i in range(len(movie_list)):
        rating = ratings(movie_list[i])
        rating = str(rating).replace('$','').replace(',','')
        print(movie_list[i])
        print(rating)
        ratings_doc.write(rating + "\n")
        

    ratings_doc.close()

if __name__ == "__main__":
    main()