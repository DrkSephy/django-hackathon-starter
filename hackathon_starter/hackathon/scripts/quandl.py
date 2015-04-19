'''Module containing a handful of methods for
aggregating data from markets throughout the world'''

import requests
import simplejson as json

def dowjonesIndustrialAvg(apikey):
    '''Returns JSON data of the Dow Jones Average.'''
    parameters = {'rows' : 1, 'auth_token' : apikey}
    apiurl = 'https://www.quandl.com/api/v1/datasets/BCB/UDJIAD1.json?'
    reap = requests.get(apiurl, params=parameters)
    desu = json.loads(reap.content)
    return desu

def snp500IndexPull(apikey):
    '''Returns JSON data of the S&P 500 Index.'''
    parameters = {'rows' : 1, 'auth_token' : apikey}
    apiurl = 'https://www.quandl.com/api/v1/datasets/YAHOO/INDEX_GSPC.json?'
    reap = requests.get(apiurl, params=parameters)
    desu = json.loads(reap.content)
    return desu

def nasdaqPull(apikey):
    '''Returns JSON data of the Nasdaq Index.'''
    parameters = {'rows' : 1, 'auth_token' : apikey}
    apiurl = 'https://www.quandl.com/api/v1/datasets/GOOG/NASDAQ_SWTX.json?'
    reap = requests.get(apiurl, params=parameters)
    desu = json.loads(reap.content)
    return desu
