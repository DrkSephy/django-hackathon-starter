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
    newsData = {}
    for datum in data:
    	newsData['title'] = data['results']['title']
    	newsData['abstract'] = data['results']['abstract']
    	newsData['section'] = data['results']['section']
    	newsData['byline'] = data['results']['byline']
    	newsData['views'] = data['results']['views']
    parsedData.append(newsData)
    return parsedData
