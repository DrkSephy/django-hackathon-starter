'''
Module containing a handful of methods for 
aggregating U.S. Census data. 
'''

import requests
import simplejson as json

########################
# CENSUS API CONSTANTS #
########################

API_BASE_URL = 'http://api.census.gov/data/2013/pep/natstprc'

def getPopulationEstimate():
	url = 'http://api.census.gov/data/2013/pep/natstprc18?get=POPEST18PLUS2013&for=us&key=1286203d2772de1f09f13392cc42a0197b2cd414'
	req = requests.get(url)
	print req.text

getPopulationEstimate()