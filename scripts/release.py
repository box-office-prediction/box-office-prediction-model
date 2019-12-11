"""
@author: sergio
"""
from omdbapi.movie_search import GetMovie
import os

def release(movie_title):
    API_KEY = os.environ('OMDB_KEY')
    movie = GetMovie(title=movie_title, api_key=API_KEY)

    release = movie.get_data('Released')

    return release

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

    release_doc = open("movie_release.csv", 'w')

    for i in range(len(movie_list)):
        rating = release(movie_list[i])
        rating = str(rating).replace('$','').replace(',','')
        print(movie_list[i])
        print(rating)
        release_doc.write(rating + "\n")
        

    release_doc.close()

if __name__ == "__main__":
    main()