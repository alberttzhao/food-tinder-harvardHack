import requests
import json

def get_data_func():
    url = 'https://api.yelp.com/v3/businesses/search'
    key = open(r"/USERS/albertz/Desktop/Hack_Harvard_Project/yelpkey.txt").readlines()[0]
    headers = {
        'Authorization': 'Bearer %s' % key
    }

    parameters = {'location': '275 Babcock Street, Boston, MA, 02215',
                'term': 'Restaurant',
                'radius': 5000,  
                'limit': 10,
                }

    response = requests.get(url, headers=headers, params=parameters)
    response

    response.json()

    query = response.json()['businesses']
    for q in query:
        print('Restaurant: {}'.format(q['name']))
        print('Rating: {}'.format(q['rating']))


get_data_func()

