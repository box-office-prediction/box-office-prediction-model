"""
@author: sergio
"""
import csv
import datetime

def reformat_release():
    old_format = list()
    new_format = list()
    with open('movie_release.csv') as fh:
        rd = csv.DictReader(fh, delimiter=':')
        for row in rd:
            old_format.append(str(row['value']).replace("'","").replace('"','').replace('}','').strip())
        print(old_format)

    release_doc = open("movie_release_reformatted.txt", 'w')

    for i in range(len(old_format)):
        release_doc.write(datetime.datetime.strptime(old_format[i], '%d %b %Y').strftime('%m/%d/%Y') + "\n")
        new_format.append(datetime.datetime.strptime(old_format[i], '%d %b %Y').strftime('%m/%d/%Y'))

    print(new_format)
    release_doc.close()


def reformat_ratings():
    old_format = list()
    new_format = list()
    with open('movie_ratings.csv') as fh:
        rd = csv.DictReader(fh, delimiter=':')
        for row in rd:
            print(str(row))
            old_format.append(str(row['value1']).replace("'","").replace('{','').replace('}','').replace('[]','').replace(']','').replace('Source','').strip()
            + " " + str(row['value2']).replace("'","").replace('{','').replace('}','').replace('[]','').replace(']','').replace('Source','').strip()
            + " " + str(row['value3']).replace("'","").replace('{','').replace('}','').replace('[]','').replace(']','').replace('Source','').strip())
        print(old_format)

    ratings_doc = open("movie_ratings_reformatted.txt", 'w')

    for i in range(len(old_format)):
        ratings_doc.write(old_format[i] + "\n")


    ratings_doc.close()

def main():
    reformat_release()
    reformat_ratings()

if __name__ == "__main__":
    main()