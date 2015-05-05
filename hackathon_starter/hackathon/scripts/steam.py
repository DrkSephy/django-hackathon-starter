'''This script contains methods belonging to the Steam web API
that can collect information based on an user's gaming library.'''
import requests
import json

def gamespulling(steamid, apikey):
    '''Returns the JSON data from the Steam API based of one's
    Steam ID number and returns a dictionary of
    gameids and minutes played.'''
    steaminfo = {
        'key': apikey,
        'steamid': steamid,
        'format':'JSON',
        'include_appinfo':'1'
    }
    apiurl = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
    req = requests.get(apiurl, params=steaminfo)
    data = json.loads(req.content)
    return data['response']['games']

def steamidpulling(steamun, apikey):
    '''Pulls out and returns the steam id number for use in steam queries.'''
    steaminfo = {'key': apikey, 'vanityurl': steamun}
    apiurl = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'
    req = requests.get(apiurl, params=steaminfo)
    data = json.loads(req.content)
    steamid = data['response']['steamid']
    return steamid

def steamlibrarypull(steamid, apikey):
    '''Pulls out a CSV of Steam appids.'''
    steaminfo = {
        'key': apikey,
        'steamid': steamid,
        'format':'JSON',
        'include_appinfo':'1'
    }
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
    req = requests.get(url, params=steaminfo)
    data = json.loads(req.content)
    response = data['response']['games']
    games = {}
    for game in response:
        url = 'http://store.steampowered.com/api/appdetails/?appids=%d&filters=price_overview&cc=us'
        getprice = requests.get(url % game['appid'])
        if getprice.status_code == 200:
            rjson = json.loads(getprice.text)
            # use the appid to fetch the value and convert to decimal
            # appid is numeric, cast to string to lookup the price
            try:
                price = rjson[str(game['appid'])]['data']['price_overview']['initial'] * .01
            except KeyError:
                pass
            games[game['name']] = {'price': price, 'appid': game['appid']}
    return games
