import requests
import json

def get_data_func(location, preference, distance, price):

    
    url = 'https://api.yelp.com/v3/businesses/search'
    key = open(r"/Users/albertz/Desktop/Hack_Harvard_Project/food-tinder-harvardHack/yelpkey.txt").readlines()[0]
    headers = {
        'Authorization': 'Bearer %s' % key
    }

    parameters = {'location': location,
                'term': preference,
                'radius': distance,  
                'limit': 10,
                'price': price,
                'sort_by': 'rating'
                }

    response = requests.get(url, headers=headers, params=parameters)
    response

    response.json()


    import pandas as pd
    query = response.json()['businesses']

    results = {'Name': [], 'Rating': [], 'Pricing': [], 'Address': []}
    for q in query:
        results['Name'].append(q['name'])
        try: 
            results['Rating'].append(q['rating'])
        except:
            results['Rating'].append(None)
        try: 
            results['Address'].append(q['location']['address1'])
        except:
            results['Address'].append(None)
        try: 
            results['Pricing'].append(len(q['price']))
        except:
            results['Pricing'].append(None)
    
    length_data = len(pd.DataFrame(results))
    return pd.DataFrame(results), length_data

# get_data_func(location = "sleeper hall", preference = "chinese", distance = 20000, price = 1, time = ' ')