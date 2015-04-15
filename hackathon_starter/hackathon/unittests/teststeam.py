import unittest
from mock import Mock, patch, MagicMock
from django.conf import settings
from hackathon.scripts.steam import *


class SteamTests(unittest.TestCase):

    def setup(self):
        self.API_URL = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
        self.APIKEY = '231E98D442E52B87110816C3D5114A1D'
        self.userID = 'Marorin'
        self.steamnum = '76561197997115778'

    def testGetUserIDNum(self):
        '''Test for steam.py method'''
        
        # Pulling from setUp
        userID = self.userID
        API_URL = self.API_URL
        APIKEY = self.APIKEY   
 
        # constructing the URL
        self.url = API_URL + '?' + APIKEY + '&' + userID

        with patch('hackathon.scripts.steam.steamIDpulling') as mock_steamIDPulling:
            # Mocking the return value of this method.
            mock_steamIDpulling = 76561197997115778
        self.assertEqual(steamIDPulling(userID,APIKEY),mock_steamIDpulling)

    def testgamespulling(self):
        '''Test gamesPulling method'''
        # Using test account due to huge JSON from normal one. 
        steamnum = self.steamnum
        with patch("requests.get") as mock_gamespulling:
            mock_gamespulling.returnvalue = [{"response": {"game_count": 0}}]
        self.assertEqual(gamesPulling(steamnum,APIKEY), mock_gamespulling.returnvalue)
