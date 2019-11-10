"""
@author: sergio
"""
def change_format():
    imdb_list = list()
    tomato_list = list()
    metacritic_list = list()
    avg_list = list()

    with open('movie_ratings_reformatted.txt') as f:
        for line in f:
            imdb, tomato, metacritic = str(line).split(" ")
            imdb_list.append(imdb)
            tomato_list.append(tomato)
            metacritic_list.append(metacritic)
    
    for i in range(100):
        imdb_rating, imdb_scale = str(imdb_list[i]).split('/')
        imdb_rating = imdb_rating.replace('.','')
        imdb_rating = int(imdb_rating)

        tomato_rating = str(tomato_list[i]).replace('%','')
        tomato_rating = int(tomato_rating)
        
        metacritic_rating, metacritic_scale = str(metacritic_list[i]).split('/')
        metacritic_rating = int(metacritic_rating)

        avg_list.append(round((imdb_rating + tomato_rating + metacritic_rating) / 3))

    avg_doc = open("movie_ratings_avg.txt", 'w')

    for i in range(100):
        avg_doc.write(str(avg_list[i]) + "\n")
    avg_doc.close()
    

def main():
    change_format()

if __name__ == "__main__":
    main()