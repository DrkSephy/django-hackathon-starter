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

def getPopulationEstimate(url):
	req = requests.get(url)
	#print len(req.text)
	print req.text

getPopulationEstimate('http://api.census.gov/data/2013/pep/monthlynatchar5?get=AGE,SEX,DATE,RACE5,HISP&key=1286203d2772de1f09f13392cc42a0197b2cd414')