# pylint: disable=C0303

import requests
import json

SteamUN = "Marorin"
key = '231E98D442E52B87110816C3D5114A1D'

def gamesPulling(steamID,key):
    # Returns the JSON data from the Steam API based of one's 
    # Steam ID number and returns a dictionary of gameids and minutes played.
    steaminfo = {
        'key': key, 
        'steamid': steamID,
        'format':'JSON',
        'include_appinfo':'1'
    }
    r = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/', params=steaminfo)
    d = json.loads(r.content)
    return d['response']['games']
 
def steamIDPulling(SteamUN,key):
    #Pulls out and returns the steam id number for use in steam queries.
    steaminfo = {'key': key,'vanityurl': SteamUN}
    a = requests.get('http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/', params=steaminfo)
    k = json.loads(a.content)
    SteamID = k['response']['steamid']
    
    return SteamID
def steamlibrarypull(steamID, key):
#Pulls out a CSV of Steam appids.
    steaminfo = {
        'key': key,
        'steamid': steamID,
        'format':'JSON',
        'include_appinfo':'1'
    }
    r = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/', params=steaminfo)
    d = json.loads(r.content)
    response = d['response']['games']
    games = {}
    for game in response:
        getprice = requests.get('http://store.steampowered.com/api/appdetails/?appids=%d&filters=price_overview&cc=us' % game['appid'])
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
