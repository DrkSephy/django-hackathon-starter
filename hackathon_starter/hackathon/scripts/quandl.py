'''Module containing a handful of methods for
aggregating data from markets throughout the world'''

import requests
import json

def fetchData(apikey, url):
    '''Returns JSON data of the Dow Jones Average.'''
    parameters = {'rows' : 1, 'auth_token' : apikey}
    req = requests.get(url, params=parameters)
    data = json.loads(req.content)
    parsedData = []
    stockData = {}
    for datum in data:
        stockData['name'] = data['name']
        stockData['description'] = data['description']
        stockData['data'] = data['data']
        stockData['code'] = data['code']
    parsedData.append(stockData)
    return parsedData
