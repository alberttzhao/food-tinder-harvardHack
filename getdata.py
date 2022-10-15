import requests
import json

def get_data_func():
    url = 'https://api.yelp.com/v3/businesses/search'
    key = open(r"/Users/albertz/Desktop/Hack_Harvard_Project/food-tinder-harvardHack/yelpkey.txt").readlines()[0]
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


    import pandas as pd
    query = response.json()['businesses']

    results = {'Name': [], 'Rating': [], 'Pricing': []}
    for q in query:
        results['Name'].append(q['name'])
        results['Rating'].append(q['rating']) 
        try: 
            results['Pricing'].append(len(q['price']))
        except:
            results['Pricing'].append(None)
    
    print(pd.DataFrame(results))

get_data_func()
