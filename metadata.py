import omdb
import os

def get_ids():
    movie_list = []
    with open('movie_ids.txt') as f:
        for line in f:
            line = str(line).strip('\n')
            movie_list.append(line)
    return movie_list

def main():

    API_KEY = os.environ('OMDB_KEY')
    omdb.set_default('apikey', API_KEY)

    movie_list = get_ids()

    metadata = open("movie_metadata.txt", 'w')

    for  i in range(len(movie_list)):
        res = omdb.get(imdbid=movie_list[i], fullplot=False, tomatoes=True)
        print(res)
        metadata.write(str(res) + "\n")

    metadata.close()

if __name__ == "__main__":
    main()