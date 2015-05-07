# pylint: disable=invalid-name

'''
Yelp.py contains methods for
authenticating the user and
retrieving data from Yelp's API.
'''

import simplejson as json
import oauth2
import requests

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = 'EXMisJNWez_PuR5pr06hyQ'
CONSUMER_SECRET = 'VCK-4cDjtQ9Ra4HC5ltClNiJFXs'
TOKEN = 'AWYVs7Vim7mwYyT1BLJA2xhNTs_vXLYS'
TOKEN_SECRET = 'Rv4GrlYxYGhxUs14s0VBfk7JLJY'

def requestData(location):
    '''
    Authenticates a request and returns
    data from Yelp API.
    '''
    data = []
    url = 'http://api.yelp.com/v2/business/' + location + '?'

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(method="GET", url=url)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    req = requests.get(signed_url)
    content = json.loads(req.content)
    data.append(content)
    return data
