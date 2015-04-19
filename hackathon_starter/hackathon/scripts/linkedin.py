import requests
import simplejson as json


consumer_key    = "7895bbnlh1k0mn"
consumer_secret = "7CjUx1xTsF2WDRAI"
oauth_token  	= "60b8f2c4-28b6-498d-a645-9dffb8baf47d"
oauth_secret	= "3114e3d4-d725-482d-a11c-2e7607025a27"

def getUserInfo():
	req = requests.get("https://api.linkedin.com/v1/people/~")
	jlist = []
	jlist.append(json.loads(req.content))
	parsedData = []
	userData = {}
	for data in jlist: 
		userData['firstname'] = data['firstname']
		userData['lasttname'] = data['lastname']
		userData['email'] = data['email']
		userData['connections'] = data['connections']
		
	parsedData.append(userData)

	return parsedData