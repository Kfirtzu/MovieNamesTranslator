import requests
import json

class Omdb:

    def __init__(self):
        self.params = dict(apikey='cab4deef')
        self.baseurl = 'http://www.omdbapi.com/'
        print(self.baseurl)

    def get_movie(self, movie_name, plot='short'):
        self.params.update({'t': movie_name,'plot':plot})
        print(self.params)
        r = requests.get(self.baseurl,params=self.params)
        print(r)
        #print(r.text)
        #json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
        j_obj = json.loads(r.text)
        print(j_obj)
        print(j_obj['Title'])

if __name__ == '__main__':
    my_db = Omdb()
    print("I'm Omdb!")
    my_db.get_movie('Jack Reacher')
    #my_db.get_movie('Harry Potter')
