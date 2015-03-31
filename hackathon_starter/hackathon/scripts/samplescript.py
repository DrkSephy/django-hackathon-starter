# Sample dummy script
# This script is just to create this directory
import requests

def getSomeData(url):
	# Get some data
	req = requests.get(url) 
	# Print the JSON
	print req.json
	return req