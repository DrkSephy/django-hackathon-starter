'''Module containing a handful of methods for
aggregating data from markets throughout the world'''

import requests
import json

def dowjonesIndustrialAvg(apikey):
    '''Returns JSON data of the Dow Jones Average.'''
    parameters = {'rows' : 1, 'auth_token' : apikey}
    apiurl = 'https://www.quandl.com/api/v1/datasets/BCB/UDJIAD1.json?'
    req = requests.get(apiurl, params=parameters)
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

def snp500IndexPull(apikey):
    '''Returns JSON data of the S&P 500 Index.'''
    parameters = {'rows' : 1, 'auth_token' : apikey}
    apiurl = 'https://www.quandl.com/api/v1/datasets/YAHOO/INDEX_GSPC.json?'
    req = requests.get(apiurl, params=parameters)
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

def nasdaqPull(apikey):
    '''Returns JSON data of the Nasdaq Index.'''
    parameters = {'rows' : 1, 'auth_token' : apikey}
    apiurl = 'https://www.quandl.com/api/v1/datasets/NASDAQOMX/COMP.json?'
    req = requests.get(apiurl, params=parameters)
    data = json.loads(req.content)
    return data
