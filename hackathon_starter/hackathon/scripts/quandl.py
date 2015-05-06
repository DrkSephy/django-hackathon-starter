'''Module containing a handful of methods for
aggregating data from markets throughout the world'''

import requests
import json

def fetchData(apikey, url):
    '''Returns JSON data of the Dow Jones Average.'''
    parameters = {'rows' : 1, 'column' : 1, 'auth_token' : apikey}
    req = requests.get(url, params=parameters)
    data = json.loads(req.content)
    parsedData = []
    stockData = {}
    if data['code'] == 'COMP':
        stockData['name'] = data['name']
        stockData['description'] = '''The NASDAQ Composite Index measures all
        NASDAQ domestic and international based common type stocks listed \
        on The NASDAQ Stock Market.'''
        stockData['data'] = data['data'][0][1]
        stockData['code'] = data['code']
    else:
        stockData['name'] = data['name']
        stockData['description'] = data['description']
        stockData['data'] = data['data'][0][1]
        stockData['code'] = data['code']
    parsedData.append(stockData)
    return parsedData

def fetchstockData(apikey, url):
    '''Returns Stock related JSON data of the stock url placed there.'''
    parameters = {'rows' : 1, 'auth_token' : apikey}
    req = requests.get(url, params=parameters)
    data = json.loads(req.content)
    parsedData = []
    stockData = {}
    stockData['name'] = data['name']
    stockData['open'] = data['data'][0][1]
    stockData['high'] = data['data'][0][2]
    stockData['low'] = data['data'][0][3]
    stockData['close'] = data['data'][0][4]
    stockData['code'] = data['code']
    parsedData.append(stockData)
    return parsedData

def rdiffData(apikey, url):
    '''Returns data of the difference of the stock URL placed there.'''
    parameters = {'rows' : 1, 'column' : 1, 'transformation': 'rdiff', 'auth_token' : apikey}
    req = requests.get(url, params=parameters)
    data = json.loads(req.content)
    parsedData = []
    stockData = {}
    stockData['rdiff'] = data['data'][0][1]
    parsedData.append(stockData)
    return parsedData
