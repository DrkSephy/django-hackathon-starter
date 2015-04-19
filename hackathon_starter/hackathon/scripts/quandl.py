'''Module containing a handful of methods for
aggregating data from markets throughout the world'''

import requests
import simplejson as json

APIKEY = ' fANs6ykrCdAxas7zpMz7'

def dowjonesindustrialavg(APIKEY):
    '''Returns JSON data of the Dow Jones Average.'''
    parameters = {'rows' : 1, 'auth_token' : APIKEY}
    apiurl = 'https://www.quandl.com/api/v1/datasets/BCB/UDJIAD1.json?'
    reap = requests.get(apiurl, params=parameters)
    desu = json.loads(reap.content)
    return desu['data']

def snp500indexpull(APIKEY):
    '''Returns JSON data of the S&P 500 Index.'''
    parameters = {'rows' : 1, 'auth_token' : APIKEY}
    apiurl = 'https://www.quandl.com/api/v1/datasets/YAHOO/INDEX_GSPC.json?'
    reap = requests.get(apiurl, params=parameters)
    desu = json.loads(reap.content)
    return desu['data']

def nasdaqpull(APIKEY):
    '''Returns JSON data of the Nasdaq Index.'''
    parameters = {'rows' : 1, 'auth_token' : APIKEY}
    apiurl = 'https://www.quandl.com/api/v1/datasets/GOOG/NASDAQ_SWTX.json?'
    reap = requests.get(apiurl, params=parameters)
    desu = json.loads(reap.content)
    return desu['data']
    