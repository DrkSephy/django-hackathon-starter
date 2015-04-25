'''module containing a handful of methods for aggregating
data from the NY Times.'''

import requests
import json

def fetcharticle(apikey, url):
    '''returns the JSON data of the most
    popular articles by view from the past 24 hours.'''
    req = requests.get(url)
    data = json.loads(req.content)
    parsedData = []
    stockData = {}
    for datum in data:
    	stockData = ['title'] = data['title']
    	stockData = ['abstract'] = data['abstract']
    	stockData = ['section'] = data['section']
    	stockData = ['byline'] = data['byline']
    	stockData = ['views'] = data['views']
    parsedData.append(stockData)
    return parsedData
