'''module containing a handful of methods for aggregating
data from the NY Times.'''

import requests
import json

def fetcharticle(apikey, url):
    '''returns the JSON data of the most
    popular articles by view from the past 24 hours.'''
    parameters = {'api-key' : apikey}
    req = requests.get(url, params=parameters)
    data = json.loads(req.content)
    parsedData = []
    for datum in data['results']:
        newData = {
            "title": datum["title"],
            "abstract": datum["abstract"],
            "section": datum["section"],
            "byline": datum["byline"],
        }
        parsedData.append(newData)
    return parsedData
