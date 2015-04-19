'''Module containing a handful of methods for 
aggregating data from markets throughout the world'''

import requests
import simplejson as json
from datetime import datetime

APIKEY = ' fANs6ykrCdAxas7zpMz7'

def DOWJonesIndustrialavg(APIKEY):
    #Returns JSON data of the Dow Jones Average. 
    parameters = {
    'rows' : 1, 
    'auth_token' : APIKEY,
    }
    r = requests.get('https://www.quandl.com/api/v1/datasets/BCB/UDJIAD1.json?',params=parameters)
    d = json.loads(r.content)
    return d['data']
def SnP500Indexpull(APIKEY):
    #Returns JSON data of the S&P 500 Index. 
    parameters = {
    'rows' : 1, 
    'auth_token' : APIKEY,
    }
    r = requests.get('https://www.quandl.com/api/v1/datasets/YAHOO/INDEX_GSPC.json?',params=parameters)
    d = json.loads(r.content)
    return d['data']
def Nasdaqpull(APIKEY):
    #Returns JSON data of the Nasdaq Index. 
    parameters = {
    'rows' : 1, 
    'auth_token' : APIKEY,
    }
    r = requests.get('https://www.quandl.com/api/v1/datasets/GOOG/NASDAQ_SWTX.json?',params=parameters)
    d = json.loads(r.content)
    return d['data']
# print DOWJonesIndustrialavg(APIKEY)