import requests
import json
SteamUN = "Marorin"
# steamID = SteamIDpulling(SteamUN)
key = '231E98D442E52B87110816C3D5114A1D'

def gamespulling(steamID,key):
    # Returns the XML data from the Steam API based of one's Steam ID number and returns a dictionary of gameids and minutes played.
    steaminfo = {'key': key, 'steamid': steamID,'format':'JSON','include_appinfo':'1'}
    r = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/',params=steaminfo)  
    d = json.loads(r.content)
    # print d['response']['games']
    # print r.json()
    return d['response']['games']
 
def steamIDpulling(SteamUN,key):
    #Pulls out and returns the steam id number for use in steam queries.
    steaminfo = {'key': key,'vanityurl': SteamUN}
    a = requests.get('http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/',params=steaminfo)
    k = json.loads(a.content)
    SteamID = k['response']['steamid']
    print SteamID
    return SteamID
# steampulling(steamID)
steamID = steamIDpulling(SteamUN, key)
gamespulling(steamID,key)