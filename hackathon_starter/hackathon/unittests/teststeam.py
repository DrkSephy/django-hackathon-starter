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
        with patch('hackathon.scripts.steam.gamesPulling) as mock_gamesPulling:
            jsonList = [{
				"appid": 4000,
				"name": "Garry's Mod",
				"playtime_forever": 0,
				"img_icon_url": "d9101cbeddcc4ff06c7fa1936c3f381b0bbf2e92",
				"img_logo_url": "dca12980667e32ab072d79f5dbe91884056a03a2",
				"has_community_visible_stats": true
			},
			{
				"appid": 6550,
				"name": "Devil May Cry 3: Special Edition",
				"playtime_forever": 217,
				"img_icon_url": "5c216acd743413bee9ae18c0d5302e5939ca689f",
				"img_logo_url": "b26ae9eee26c206b2b3bfab7d365f707e20854a3"
			},
			{
				"appid": 10500,
				"name": "Empire: Total War",
				"playtime_forever": 0,
				"img_icon_url": "dc10f7bad53d3d922c196d116b1c5d6a4b274768",
				"img_logo_url": "d60c77df97439e8434f0d0be9c3e2d9f39699991",
				"has_community_visible_stats": true
			},
			{
				"appid": 17460,
				"name": "Mass Effect",
				"playtime_forever": 1242,
				"img_icon_url": "57be81f70afa48c65437df93d75ba167a29687bc",
				"img_logo_url": "7501ea5009533fa5c017ec1f4b94725d67ad4936"
			},
			{
				"appid": 12810,
				"name": "Overlord II",
				"playtime_forever": 0,
				"img_icon_url": "cc38122745bd44454e7e122e86023fb35e652d9d",
				"img_logo_url": "7107ed1429c4be7637571fdf262f61af6bc7d4a2"
			},
			{
				"appid": 45700,
				"name": "Devil May Cry 4",
				"playtime_forever": 925,
				"img_icon_url": "1f869ad15ffdc1eb406c5d1635c9c0efb2e91f12",
				"img_logo_url": "5b274e94aec7806da9a1b5ba5334668781ff0fd2"
			},
			{
				"appid": 24980,
				"name": "Mass Effect 2",
				"playtime_forever": 4040,
				"img_icon_url": "e6f3b9b0762fd4d42a732abfc41887f6c5903a52",
				"img_logo_url": "d446fe6d77c9f434cd7fd871400b978fc01fb4e7"
			},
			{
				"appid": 4540,
				"name": "Titan Quest",
				"playtime_forever": 0,
				"img_icon_url": "d59f857aed0d38c69960a9d80e3d23e0863f4e01",
				"img_logo_url": "e82186f6efe8d5d593c2fb1b57f8b1e056e6d82e",
				"has_community_visible_stats": true
			},
			{
				"appid": 21100,
				"name": "F.E.A.R. 3",
				"playtime_forever": 0,
				"img_icon_url": "01b73115a3ff7315d14f0bcf7beff01ef76162b4",
				"img_logo_url": "d2fcf83ec76e845ed19f4ff8324304e2981af391",
				"has_community_visible_stats": true
			},
			{
				"appid": 620,
				"name": "Portal 2",
				"playtime_forever": 29,
				"img_icon_url": "2e478fc6874d06ae5baf0d147f6f21203291aa02",
				"img_logo_url": "d2a1119ddc202fab81d9b87048f495cbd6377502",
				"has_community_visible_stats": true
			},
			{
				"appid": 45760,
				"name": "Ultra Street Fighter IV",
				"playtime_forever": 111,
				"img_icon_url": "473fcea2eb516528608dff7f9e3e61009d76a282",
				"img_logo_url": "bdd481249e579f852056b51db32a6279444d4f47",
				"has_community_visible_stats": true
			},
			{
				"appid": 21090,
				"name": "F.E.A.R.",
				"playtime_forever": 0,
				"img_icon_url": "71f118282be5aaa34eb82506593130ecfcc6a90b",
				"img_logo_url": "df122e0ee9eb2a5371910ffda0f8a3382e09232e"
			},
			{
				"appid": 21110,
				"name": "F.E.A.R.: Extraction Point",
				"playtime_forever": 0,
				"img_icon_url": "153d4f89ef0bd59a0039c396ff963a31d4d5e71b",
				"img_logo_url": "df122e0ee9eb2a5371910ffda0f8a3382e09232e"
			},
			{
				"appid": 21120,
				"name": "F.E.A.R.: Perseus Mandate",
				"playtime_forever": 0,
				"img_icon_url": "7b1d0271f2735ca66e1cb681eb4da1a7c985d53f",
				"img_logo_url": "df122e0ee9eb2a5371910ffda0f8a3382e09232e"
			},
			{
				"appid": 16450,
				"name": "F.E.A.R. 2: Project Origin",
				"playtime_forever": 0,
				"img_icon_url": "6611d8b01c7a2cc3538c478c044d1e09f3140eaa",
				"img_logo_url": "41734347c3f05fe7dd797570130f5069c08f9d1b"
			},
			{
				"appid": 32800,
				"name": "The Lord of the Rings: War in the North",
				"playtime_forever": 0,
				"img_icon_url": "56dcf3fe99a90c25daae1cbe84319bb8af3c6ac5",
				"img_logo_url": "b90d899806ebaff87ed7d2cdc4d9e0a3f11b73b0",
				"has_community_visible_stats": true
			},
			{
				"appid": 107100,
				"name": "Bastion",
				"playtime_forever": 45,
				"img_icon_url": "8377b4460f19465c261673f76f2656bdb3288273",
				"img_logo_url": "d113d66ef88069d7d35a74cfaf2e2ee917f61133",
				"has_community_visible_stats": true
			},
			{
				"appid": 55230,
				"name": "Saints Row: The Third",
				"playtime_forever": 246,
				"img_icon_url": "ec83645f13643999e7c91da75d418053d6b56529",
				"img_logo_url": "1129528455a8b297fb6404cbb90e802a62881b11",
				"has_community_visible_stats": true
			},
			{
				"appid": 34270,
				"name": "SEGA Genesis & Mega Drive Classics",
				"playtime_forever": 4,
				"img_icon_url": "48a187fa87c58b798646a430d446dd36eeabd1a4",
				"img_logo_url": "212f55b3ea1a8c70427890896e93a37b49f57187",
				"has_community_visible_stats": true
			},
			{
				"appid": 71340,
				"name": "Sonic Generations",
				"playtime_forever": 520,
				"img_icon_url": "efda039147f0968bc726c547ff3809f98b69964a",
				"img_logo_url": "21ec1e24c31a50500bbddb8c8c8add451e6dcbe1",
				"has_community_visible_stats": true
			},
			{
				"appid": 72850,
				"name": "The Elder Scrolls V: Skyrim",
				"playtime_forever": 2431,
				"img_icon_url": "b9aca8a189abd8d6aaf09047dbb0f57582683e1c",
				"img_logo_url": "c5af3cde13610fca25cd17634a96d72487d21e74",
				"has_community_visible_stats": true
			},
			{
				"appid": 41070,
				"name": "Serious Sam 3: BFE",
				"playtime_forever": 0,
				"img_icon_url": "2e7a17d4b345ffb13ef3d9e39257c2659fe4a86b",
				"img_logo_url": "cc3a3c30187b5fbbd0a8861ad08b4f7d779ba239",
				"has_community_visible_stats": true
			},
			{
				"appid": 57400,
				"name": "Batman: Arkham City™",
				"playtime_forever": 1271,
				"img_icon_url": "4c208d1365ea5614326717ecfcfea1196ef48e70",
				"img_logo_url": "5456a41d4076244a6c593cbb260c3384493a7727",
				"has_community_visible_stats": true
			},
			{
				"appid": 200260,
				"name": "Batman: Arkham City GOTY",
				"playtime_forever": 592,
				"img_icon_url": "746ecf3ce44b2525eb7ad643e76a3b60913d2662",
				"img_logo_url": "9b229e12fd5ce27bd101d5862c19b1a6e3d01239",
				"has_community_visible_stats": true
			},
			{
				"appid": 108710,
				"name": "Alan Wake",
				"playtime_forever": 0,
				"img_icon_url": "ec7953511aaaf5a2c2093b872b5b43c6cab56462",
				"img_logo_url": "0f9b6613ac50bf42639ed6a2e16e9b78e846ef0a",
				"has_community_visible_stats": true
			},
			{
				"appid": 207490,
				"name": "Rayman Origins",
				"playtime_forever": 585,
				"img_icon_url": "1e155c2bc13e8793aed8bb61fdac798fe0d49de7",
				"img_logo_url": "ebfd3f8da2b0416d71724a2929740a72a6eaabf4"
			},
			{
				"appid": 41500,
				"name": "Torchlight",
				"playtime_forever": 130,
				"img_icon_url": "b2a2a43e401dce3c69898b67b1b8af4481d96b08",
				"img_logo_url": "e36226c6a0575e6e1838e1f915e91f8b31ab3008",
				"has_community_visible_stats": true
			},
			{
				"appid": 200710,
				"name": "Torchlight II",
				"playtime_forever": 1011,
				"img_icon_url": "40776762bb63c4eded37d1a2b4431a90aa57ea84",
				"img_logo_url": "fd37abb86628ff54ed304f75c2fb7cf75a4f6902",
				"has_community_visible_stats": true
			},
			{
				"appid": 205350,
				"name": "Mortal Kombat Kollection",
				"playtime_forever": 0,
				"img_icon_url": "048e463386c8f0049d6e08bbf8f5ebb5d232394f",
				"img_logo_url": "44281a64a93a583fdd2435036ac794e7dcc7beb8",
				"has_community_visible_stats": true
			},
			{
				"appid": 202750,
				"name": "Alan Wake's American Nightmare",
				"playtime_forever": 0,
				"img_icon_url": "313aabf37ed0b521ad969d3fe21768d31300f1ca",
				"img_logo_url": "d3593fa14e4ea8685dc6b1f71dbaa980c013ff02",
				"has_community_visible_stats": true
			},
			{
				"appid": 113200,
				"name": "The Binding of Isaac",
				"playtime_forever": 503,
				"img_icon_url": "383cf045ca20625db18f68ef5e95169012118b9e",
				"img_logo_url": "d9a7ee7e07dffed1700cb8b3b9482105b88cc5b5",
				"has_community_visible_stats": true
			},
			{
				"appid": 35140,
				"name": "Batman: Arkham Asylum GOTY Edition",
				"playtime_forever": 0,
				"img_icon_url": "e52f91ecb0d3f20263e96fe188de1bcc8c91643e",
				"img_logo_url": "172e0928b845c18491f1a8fee0dafe7a146ac129",
				"has_community_visible_stats": true
			},
			{
				"appid": 211420,
				"name": "Dark Souls: Prepare to Die Edition",
				"playtime_forever": 5309,
				"img_icon_url": "a24804c6c8412c8cd9d50efd06bf03fa58ff80a9",
				"img_logo_url": "d293c8e38f56de2c7097b2c7a975caca49029a8b",
				"has_community_visible_stats": true
			},
			{
				"appid": 204300,
				"name": "Awesomenauts",
				"playtime_forever": 9,
				"img_icon_url": "4996933171d0804bd0ceb7b9a0e224b3139d18ba",
				"img_logo_url": "a2eba6157703c60bfcc199f06df5f1568c9835bb",
				"has_community_visible_stats": true
			},
			{
				"appid": 204630,
				"name": "Retro City Rampage™ DX",
				"playtime_forever": 0,
				"img_icon_url": "423b87d4a5a00ff6e807558e565b0b515fadf61b",
				"img_logo_url": "3ca51d2767c5de3358c4f1824f1b362a9494983f",
				"has_community_visible_stats": true
			},
			{
				"appid": 214560,
				"name": "Mark of the Ninja",
				"playtime_forever": 1,
				"img_icon_url": "220f33169c93c2f6381cd785399fb52bfc79309f",
				"img_logo_url": "c20501309696e5bcda98e9e4f2649abc5720a1d1",
				"has_community_visible_stats": true
			},
			{
				"appid": 49520,
				"name": "Borderlands 2",
				"playtime_2weeks": 24,
				"playtime_forever": 7526,
				"img_icon_url": "a3f4945226e69b6196074df4c776e342d3e5a3be",
				"img_logo_url": "86b0fa5ddb41b4dfff7df194a017f3418130d668",
				"has_community_visible_stats": true
			},
			{
				"appid": 205950,
				"name": "Jet Set Radio",
				"playtime_forever": 644,
				"img_icon_url": "884cfa9f5f615e297f8c53a2010f1b63835e44b5",
				"img_logo_url": "3272dfd2e30df5629bfbaa851ea503e9ee28b75a",
				"has_community_visible_stats": true
			},
			{
				"appid": 213610,
				"name": "Sonic Adventure™ 2 ",
				"playtime_forever": 0,
				"img_icon_url": "0ff2b133493b0bf7f1c16a38a83e7053f0b90f2d",
				"img_logo_url": "b59ee5bd744212a79db6fd8f71aec6729671da2b",
				"has_community_visible_stats": true
			},
			{
				"appid": 205790,
				"name": "Dota 2 Test",
				"playtime_forever": 20,
				"img_icon_url": "",
				"img_logo_url": ""
			},
			{
				"appid": 218680,
				"name": "Scribblenauts Unlimited",
				"playtime_forever": 0,
				"img_icon_url": "e933a9993b7d0b905dbb37636a97339a2c277e0f",
				"img_logo_url": "c3f8420cd87dd772df8a35013e3538e964ecc2b8",
				"has_community_visible_stats": true
			},
			{
				"appid": 223220,
				"name": "Giana Sisters: Twisted Dreams",
				"playtime_forever": 115,
				"img_icon_url": "ac543243f2541e7a7728bf2165c5f3ebc57679fb",
				"img_logo_url": "9c8baddbab7938b5b995843d36526a30bd12bb1d",
				"has_community_visible_stats": true
			},
			{
				"appid": 4920,
				"name": "Natural Selection 2",
				"playtime_forever": 0,
				"img_icon_url": "df709ad4689cbfb82c2971be4adba431e755875f",
				"img_logo_url": "ab7b1142e17865e6d3472d3fd4b345620ec5f36f",
				"has_community_visible_stats": true
			},
			{
				"appid": 219950,
				"name": "NiGHTS into Dreams...",
				"playtime_forever": 0,
				"img_icon_url": "630fb86750aaa5d9ca713df086fa93d9804e9f02",
				"img_logo_url": "7316d46b1ce35a260ddedc6a1f7590a8b98dea92",
				"has_community_visible_stats": true
			},
			{
				"appid": 4560,
				"name": "Company of Heroes",
				"playtime_forever": 0,
				"img_icon_url": "64946619217da497c9b29bc817bb40dd7d28c912",
				"img_logo_url": "e12e8695c6766b47a089351dd9c4531e669c2a7b"
			},
			{
				"appid": 9340,
				"name": "Company of Heroes: Opposing Fronts",
				"playtime_forever": 0,
				"img_icon_url": "29725d719946c3e1aa4eea15d262c9fd789c1392",
				"img_logo_url": "830c99099ea2cfecfe74c41f376fc892a09dd181"
			},
			{
				"appid": 20540,
				"name": "Company of Heroes: Tales of Valor",
				"playtime_forever": 0,
				"img_icon_url": "64946619217da497c9b29bc817bb40dd7d28c912",
				"img_logo_url": "ed0c55412acea558d025a3e238e2b7341edc5c41"
			},
			{
				"appid": 43110,
				"name": "Metro 2033",
				"playtime_forever": 0,
				"img_icon_url": "a70fe6dc214f24107d20596f3040dbfa220ed42d",
				"img_logo_url": "df9a163ac1f28dfc84c93a6fc0dc51719eaef518",
				"has_community_visible_stats": true
			},
			{
				"appid": 50620,
				"name": "Darksiders",
				"playtime_forever": 925,
				"img_icon_url": "e429cee10d864faf2aae2ea9cd75e8e1942fbe08",
				"img_logo_url": "14bd29bc9b291081b63258e3bfbbf5bb655c2347",
				"has_community_visible_stats": true
			},
			{
				"appid": 55110,
				"name": "Red Faction: Armageddon",
				"playtime_forever": 0,
				"img_icon_url": "e59c7e741c05c9071176b270bdbb733afe55c751",
				"img_logo_url": "19f894d0e08dff8e284d4facc5968a1025da997d",
				"has_community_visible_stats": true
			},
			{
				"appid": 228200,
				"name": "Company of Heroes (New Steam Version)",
				"playtime_forever": 0,
				"img_icon_url": "df92dc239acb3cf5d3e3eba645f3df2aaf7f91ad",
				"img_logo_url": "87aa009e93d5aa56a55d0e9056708d018ddd6483",
				"has_community_visible_stats": true
			},
			{
				"appid": 201790,
				"name": "Orcs Must Die! 2",
				"playtime_forever": 0,
				"img_icon_url": "fabd8658e8e76f7c99c56f26b69d29882756f9b4",
				"img_logo_url": "c345d9b205f349f0e7f4e6cdf8af4d0b7d242505",
				"has_community_visible_stats": true
			},
			{
				"appid": 4570,
				"name": "Warhammer 40,000: Dawn of War - Game of the Year Edition",
				"playtime_forever": 5,
				"img_icon_url": "a4c7a8cce43d797c275aaf601d6855b90ba87769",
				"img_logo_url": "2068980dca52521b069abc109f976d72ba0b1651",
				"has_community_visible_stats": true
			},
			{
				"appid": 71230,
				"name": "Crazy Taxi",
				"playtime_forever": 0,
				"img_icon_url": "e71b220f8103e3515bd56de6a42395121e31e2cf",
				"img_logo_url": "be180e020c4e1ca0a13ec1a9006a1235b6a9eb50",
				"has_community_visible_stats": true
			},
			{
				"appid": 71240,
				"name": "SEGA Bass Fishing",
				"playtime_forever": 0,
				"img_icon_url": "fac67362e11293a673158e6d3c8c67693816868f",
				"img_logo_url": "6255f428036c011b325b40ebf1c53daa4db7e1f1",
				"has_community_visible_stats": true
			},
			{
				"appid": 71250,
				"name": "Sonic Adventure DX",
				"playtime_forever": 0,
				"img_icon_url": "6568d25b43e2d1d07fc16cbe3ac9278ca51c2fb3",
				"img_logo_url": "e8374c63e76724af4648cdea5331f4ae39af4d06",
				"has_community_visible_stats": true
			},
			{
				"appid": 71260,
				"name": "Space Channel 5: Part 2",
				"playtime_forever": 366,
				"img_icon_url": "82aec5f26e9d40c5275b1cd9bf692c4057c108ef",
				"img_logo_url": "fad43b313c2f6869c42bf0d7c4959363c5394d9a",
				"has_community_visible_stats": true
			},
			{
				"appid": 50650,
				"name": "Darksiders II",
				"playtime_forever": 1591,
				"img_icon_url": "a2d5549090144f1bfd9e00f1b460c1ad0aa9c366",
				"img_logo_url": "b0b8edfa57f332dc529c04b4dd2f5475227e71ac",
				"has_community_visible_stats": true
			},
			{
				"appid": 35720,
				"name": "Trine 2",
				"playtime_forever": 0,
				"img_icon_url": "061ecbbd7c70ae1c052377bad136c7759cbb708d",
				"img_logo_url": "7d7c3b93bd85ad1db2a07f6cca01a767069c6407",
				"has_community_visible_stats": true
			},
			{
				"appid": 226320,
				"name": "Marvel Heroes 2015",
				"playtime_forever": 0,
				"img_icon_url": "a0c1c35208af7b63759361305631da48539d45cc",
				"img_logo_url": "7121a66719963c4790d6169d38b9c65ad8f238bc",
				"has_community_visible_stats": true
			},
			{
				"appid": 225260,
				"name": "Brütal Legend",
				"playtime_forever": 0,
				"img_icon_url": "e3f25fba8538e5fb1ead751e767c2774df4fb0b4",
				"img_logo_url": "cc8b60ac1fa649c950ff7a9881b98709b8372f94",
				"has_community_visible_stats": true
			},
			{
				"appid": 210770,
				"name": "Sanctum 2",
				"playtime_forever": 0,
				"img_icon_url": "4cdfa1d19be460374a111b718ce3a204f21ea1dc",
				"img_logo_url": "333a8c65480bb85148bb3a185843a8520ae5d90f",
				"has_community_visible_stats": true
			},
			{
				"appid": 234710,
				"name": "Poker Night 2",
				"playtime_forever": 7,
				"img_icon_url": "b3073e6f089447a9cf1eeabf7579600061546322",
				"img_logo_url": "0b274bb5ade23104ce267a05ce7ac0f7aaa0248d",
				"has_community_visible_stats": true
			},
			{
				"appid": 31100,
				"name": "Wallace & Gromit Ep 1: Fright of the Bumblebees",
				"playtime_forever": 0,
				"img_icon_url": "1c8b457c265e36e6ac08d8d5ae5709124eae3025",
				"img_logo_url": "6b303e67e65d39cd3747ed21efb42de9ddb0d251"
			},
			{
				"appid": 31110,
				"name": "Wallace & Gromit Ep 2: The Last Resort",
				"playtime_forever": 0,
				"img_icon_url": "e6d415690e4c05b3d716030984346442f10e87e9",
				"img_logo_url": "7cda224cf65955e5e763ce8eff0b099add72f04e"
			},
			{
				"appid": 31120,
				"name": "Wallace & Gromit Ep 3: Muzzled!",
				"playtime_forever": 0,
				"img_icon_url": "70475b4d75934174a0fff9969315be9a4993c150",
				"img_logo_url": "3910a6ff5e48c5f7ed249b48387bc321504db73c"
			},
			{
				"appid": 31130,
				"name": "Wallace & Gromit Ep 4: The Bogey Man",
				"playtime_forever": 0,
				"img_icon_url": "9072b2096b4542529aa47f4115bff48ab781ff6e",
				"img_logo_url": "8a5313cf2bdd01a0516c56b3ce952428de85d430"
			},
			{
				"appid": 31220,
				"name": "Sam & Max 301: The Penal Zone",
				"playtime_forever": 335,
				"img_icon_url": "2c9c4ac6dfa50c4c479b6b436f04974a372588f7",
				"img_logo_url": "517196c999fe6316134332e749782154bde9adf5"
			},
			{
				"appid": 31230,
				"name": "Sam & Max 302: The Tomb of Sammun-Mak",
				"playtime_forever": 72,
				"img_icon_url": "e83fbb799f46b349586ca55fcf612350cc88ffe7",
				"img_logo_url": "517196c999fe6316134332e749782154bde9adf5"
			},
			{
				"appid": 31240,
				"name": "Sam & Max 303: They Stole Max's Brain!",
				"playtime_forever": 0,
				"img_icon_url": "bf1ebfe347a80e2ac31577e0569de3aa201cd17f",
				"img_logo_url": "517196c999fe6316134332e749782154bde9adf5"
			},
			{
				"appid": 31250,
				"name": "Sam & Max 304: Beyond the Alley of the Dolls",
				"playtime_forever": 0,
				"img_icon_url": "d4f834ac9d48cd59645f453d0cb30655dee6f629",
				"img_logo_url": "62ef5af2ce55bb787ff490126c110c41131043bc"
			},
			{
				"appid": 31260,
				"name": "Sam & Max 305: The City that Dares not Sleep",
				"playtime_forever": 0,
				"img_icon_url": "9e41c6d0c777cd0a7fb4e96da4f20d2227841725",
				"img_logo_url": "62ef5af2ce55bb787ff490126c110c41131043bc"
			},
			{
				"appid": 31270,
				"name": "Puzzle Agent",
				"playtime_forever": 0,
				"img_icon_url": "d0cae0b07b2512302968bd7625a9bf12cebdfba8",
				"img_logo_url": "f1bd7dd0bae1026b17c61a605a567ed68e683fef"
			},
			{
				"appid": 31280,
				"name": "Poker Night at the Inventory",
				"playtime_forever": 0,
				"img_icon_url": "7d50bd1f5e7cfe68397e9ca0041836ad18153dfb",
				"img_logo_url": "d962cde096bca06ee10d09880e9f3d6257941161",
				"has_community_visible_stats": true
			},
			{
				"appid": 31290,
				"name": "Back to the Future: Ep 1 - It's About Time",
				"playtime_forever": 0,
				"img_icon_url": "a9a9b1683209e3223779ad2315e4bf03e27619d7",
				"img_logo_url": "252a22c149c29a2d93fcb0080f3ee9d2dbbd9a2f"
			},
			{
				"appid": 94500,
				"name": "Back to the Future: Ep 2 - Get Tannen!",
				"playtime_forever": 0,
				"img_icon_url": "d5382aedd7594e088a078341034e4b369210ec9a",
				"img_logo_url": "ae0d863314d6111e6debaef7c9cdcf2940738b1e"
			},
			{
				"appid": 94510,
				"name": "Back to the Future: Ep 3 - Citizen Brown",
				"playtime_forever": 0,
				"img_icon_url": "a51c4795b44f689628bd76bc64cad310385ba1a2",
				"img_logo_url": "7fe46585ad7fbc8fedb38db7f8dd8608be5a46ee"
			},
			{
				"appid": 94520,
				"name": "Back to the Future: Ep 4 - Double Visions",
				"playtime_forever": 0,
				"img_icon_url": "5a7fd98c15742b9fca4e443b5eaadf953a6c83d3",
				"img_logo_url": "ac9fc7c15ae656d200299003ce22ab84185e54e4"
			},
			{
				"appid": 94530,
				"name": "Back to the Future: Ep 5 - OUTATIME",
				"playtime_forever": 0,
				"img_icon_url": "3d034831533383bc5a58787763925660684de8c4",
				"img_logo_url": "76361dfc1ef09dbb7f6572a6da7ab38a811f54af"
			},
			{
				"appid": 94590,
				"name": "Puzzle Agent 2",
				"playtime_forever": 0,
				"img_icon_url": "d558eb6bddeb55f5f145822f3949ab50bc02aff9",
				"img_logo_url": "b7aac2e076fb1c5178681e2cab0f8bae4380c96d",
				"has_community_visible_stats": true
			},
			{
				"appid": 94600,
				"name": "Hector: Ep 1",
				"playtime_forever": 0,
				"img_icon_url": "aa0a113e80b8cdeff47a523a87dd2fad1f43d73e",
				"img_logo_url": "fae3324a5c43647dda98be23bf1db4480c031273"
			},
			{
				"appid": 94610,
				"name": "Hector: Ep 2",
				"playtime_forever": 0,
				"img_icon_url": "0bfad503074efc1c46755d05d36be4755945f8fe",
				"img_logo_url": "52a3e61842a22bf75f6bf6d355400d5b3776f9b4"
			},
			{
				"appid": 94620,
				"name": "Hector: Ep 3",
				"playtime_forever": 0,
				"img_icon_url": "aa0a113e80b8cdeff47a523a87dd2fad1f43d73e",
				"img_logo_url": "97ec609986c7672a3928e7dca14d9aead4cbf65f"
			},
			{
				"appid": 236090,
				"name": "Dust: An Elysian Tail",
				"playtime_forever": 563,
				"img_icon_url": "3779535aba1ad565d504a7d52c6dd5c9eeb47fb2",
				"img_logo_url": "544fd60b00696d8c3402828da7055fea64d619ca",
				"has_community_visible_stats": true
			},
			{
				"appid": 229480,
				"name": "Dungeons & Dragons: Chronicles of Mystara",
				"playtime_forever": 91,
				"img_icon_url": "270699bf34b75a6789370de8b0cb98e163832f71",
				"img_logo_url": "cb7b16b064562469c375a22d9d07a7ab11abdab6",
				"has_community_visible_stats": true
			},
			{
				"appid": 208610,
				"name": "Skullgirls ∞Endless Beta∞",
				"playtime_forever": 292,
				"img_icon_url": "7bf859db736b8825045b0cc79acc4bb7be8cd7b9",
				"img_logo_url": "33974b81779c888b3b4d9c4b91d86ef0907b11f3",
				"has_community_visible_stats": true
			},
			{
				"appid": 237110,
				"name": "Mortal Kombat Komplete Edition",
				"playtime_forever": 365,
				"img_icon_url": "3b9c627b90f42cf650d5848e2fdd779fa4e6eb19",
				"img_logo_url": "307dc1eacffd54e5a7a02b663cec1c5105059811",
				"has_community_visible_stats": true
			},
			{
				"appid": 245170,
				"name": "Skullgirls",
				"playtime_forever": 1152,
				"img_icon_url": "7bf859db736b8825045b0cc79acc4bb7be8cd7b9",
				"img_logo_url": "ca3f7bd4fbb3cf73855ebce91b6dafc2104d651b",
				"has_community_visible_stats": true
			},
			{
				"appid": 222940,
				"name": "THE KING OF FIGHTERS XIII STEAM EDITION",
				"playtime_forever": 322,
				"img_icon_url": "de8d9bf86ae8983464d69743b55cef3992330ccf",
				"img_logo_url": "9f2bec35f18bfc1a80ffab64bc51a09a880343b6",
				"has_community_visible_stats": true
			},
			{
				"appid": 250760,
				"name": "Shovel Knight",
				"playtime_forever": 1,
				"img_icon_url": "9b8866653bcaf20db1424653df8560205939cdba",
				"img_logo_url": "23fca16e3df2ed731136574b320988406eb0f712",
				"has_community_visible_stats": true
			},
			{
				"appid": 250900,
				"name": "The Binding of Isaac: Rebirth",
				"playtime_forever": 95,
				"img_icon_url": "16d46c8630499bfc54d20745ac90786a302cd643",
				"img_logo_url": "c7a76988c53e7f3a3aa1cf224aaf4dbd067ebbf9",
				"has_community_visible_stats": true
			},
			{
				"appid": 111900,
				"name": "Guardians of Middle-earth",
				"playtime_forever": 0,
				"img_icon_url": "5ab636ac90b8476892d6e0ae377624d5b934f600",
				"img_logo_url": "08a7116bebd1bf44bb8e86495358dca14224d223",
				"has_community_visible_stats": true
			},
			{
				"appid": 234670,
				"name": "NARUTO SHIPPUDEN: Ultimate Ninja STORM 3 Full Burst",
				"playtime_forever": 1405,
				"img_icon_url": "ddd956cc6ec3370449f96298653d4119c5666fff",
				"img_logo_url": "12895039c12ec92be72faa2d13acb88886b8cb97",
				"has_community_visible_stats": true
			},
			{
				"appid": 42910,
				"name": "Magicka",
				"playtime_forever": 0,
				"img_icon_url": "0eb97d0cd644ee08b1339d2160c7a6adf2ea0a65",
				"img_logo_url": "8c59c674ef40f59c3bafde8ff0d59b7994c66477",
				"has_community_visible_stats": true
			},
			{
				"appid": 212480,
				"name": "Sonic & All-Stars Racing Transformed",
				"playtime_forever": 0,
				"img_icon_url": "95767af7b08d7ecebf1e9cb1ed1c92c98e4c084f",
				"img_logo_url": "351603b89e1863831c84aacab7bf3a315f03443b",
				"has_community_visible_stats": true
			},
			{
				"appid": 261640,
				"name": "Borderlands: The Pre-Sequel",
				"playtime_2weeks": 838,
				"playtime_forever": 1157,
				"img_icon_url": "af5ef05eac8b1eb618e4f57354ac7b3e918ab1bd",
				"img_logo_url": "df64c72fd335a03dbcc0a19b1f81acc8db1b94ba",
				"has_community_visible_stats": true
			},
			{
				"appid": 39150,
				"name": "FINAL FANTASY VIII",
				"playtime_forever": 119,
				"img_icon_url": "e2b0371cd72160603e7ecaaf95b238a46ba254e6",
				"img_logo_url": "0c912769e975586cdcfe4a6b008d538f1f96a032",
				"has_community_visible_stats": true
			},
			{
				"appid": 235460,
				"name": "METAL GEAR RISING: REVENGEANCE",
				"playtime_forever": 1268,
				"img_icon_url": "ad0f84fe48b57f3861b6c6d743f26b98d670c21f",
				"img_logo_url": "a21384421dafa03783e3672a5f4754f70e63235e",
				"has_community_visible_stats": true
			},
			{
				"appid": 550,
				"name": "Left 4 Dead 2",
				"playtime_forever": 0,
				"img_icon_url": "7d5a243f9500d2f8467312822f8af2a2928777ed",
				"img_logo_url": "205863cc21e751a576d6fff851984b3170684142",
				"has_community_visible_stats": true
			},
			{
				"appid": 236430,
				"name": "DARK SOULS™ II",
				"playtime_forever": 8872,
				"img_icon_url": "8d5b3da903efb047d4efb670c08714a4d1071e83",
				"img_logo_url": "d16871e0aa9196e5e7d865f76fbed278a0309e85",
				"has_community_visible_stats": true
			},
			{
				"appid": 282900,
				"name": "Hyperdimension Neptunia Re;Birth1",
				"playtime_forever": 1647,
				"img_icon_url": "0cd228210df4f44ef8e77f62b18d1a9af81a72d4",
				"img_logo_url": "c2835cfa39dbaf8e7e1f668e4bf491855a274947",
				"has_community_visible_stats": true
			},
			{
				"appid": 254700,
				"name": "resident evil 4 / biohazard 4",
				"playtime_forever": 737,
				"img_icon_url": "535bfea3332662271f1e3a972832bc0b4aba5a38",
				"img_logo_url": "532d72710af44f29cc123c5796e95e0382461ee5",
				"has_community_visible_stats": true
			},
			{
				"appid": 231430,
				"name": "Company of Heroes 2",
				"playtime_forever": 0,
				"img_icon_url": "9efafff369d37ea19c44139de4476e6c63319b6b",
				"img_logo_url": "2c413e4cc731862e0b3307ed9c23b1cd20087130",
				"has_community_visible_stats": true
			},
			{
				"appid": 317170,
				"name": "Company of Heroes 2 - Beta",
				"playtime_forever": 0,
				"img_icon_url": "9efafff369d37ea19c44139de4476e6c63319b6b",
				"img_logo_url": "62afc50b5f0970c1070951f56a7dd0c0b943b013",
				"has_community_visible_stats": true
			},
			{
				"appid": 294810,
				"name": "BlazBlue: Continuum Shift Extend",
				"playtime_forever": 82,
				"img_icon_url": "244644a6721480f40e4de61e4bb7a337d999e435",
				"img_logo_url": "b7105e9443e1f3bed7bb3fd1599a140e75dcf2c6",
				"has_community_visible_stats": true
			},
			{
				"appid": 294860,
				"name": "Valkyria Chronicles™",
				"playtime_forever": 65,
				"img_icon_url": "176c6dcafc9bf0fbb87f9adeb224df88c8248a66",
				"img_logo_url": "08316e1d6a45d8e13de7f5e1a1480cf4efff15cf",
				"has_community_visible_stats": true
			},
			{
				"appid": 285440,
				"name": "Crimzon Clover  WORLD IGNITION",
				"playtime_forever": 8,
				"img_icon_url": "8f4f6490c9b48e8d6e2b688c4a097f9bdd8fb56d",
				"img_logo_url": "72ab0aac6800b9ec9f79571d6f425f0e687d04ca",
				"has_community_visible_stats": true
			},
			{
				"appid": 314030,
				"name": "Guilty Gear X2 #Reload",
				"playtime_forever": 99,
				"img_icon_url": "bde7b6e8d891b310fad62d25a0cf009c979db84c",
				"img_logo_url": "94edca39fa971bc8beeb0066afc99993246a9976"
			},
			{
				"appid": 206420,
				"name": "Saints Row IV",
				"playtime_forever": 205,
				"img_icon_url": "b5e8448a3e2ea31ddf3595addae4e1eee2375c0d",
				"img_logo_url": "49d796621c286130a8ddeea918d9aae8c8441455",
				"has_community_visible_stats": true
			},
			{
				"appid": 21690,
				"name": "Resident Evil 5 / Biohazard 5",
				"playtime_forever": 782,
				"img_icon_url": "26108f5caff3638c9f522dd79ee84a12761f373a",
				"img_logo_url": "e277ab70fff98bb2300a39bf8e2371a746fe50b1",
				"has_community_visible_stats": true
			},
			{
				"appid": 222480,
				"name": "Resident Evil Revelations / Biohazard Revelations UE",
				"playtime_forever": 476,
				"img_icon_url": "5725845fe83f846a04135034c5be55aef008c725",
				"img_logo_url": "cf242207e0e06251f55baf2f89c37ded12c79329",
				"has_community_visible_stats": true
			},
			{
				"appid": 323470,
				"name": "DRAGON BALL XENOVERSE",
				"playtime_2weeks": 24,
				"playtime_forever": 815,
				"img_icon_url": "810b2bab6e3197b5d63d3abffcebafaac8dc6312",
				"img_logo_url": "f8724eeddf94534d66b8057cf770a9cd8318a14a",
				"has_community_visible_stats": true
			},
			{
				"appid": 730,
				"name": "Counter-Strike: Global Offensive",
				"playtime_forever": 62,
				"img_icon_url": "69f7ebe2735c366c65c0b33dae00e12dc40edbe4",
				"img_logo_url": "d0595ff02f5c79fd19b06f4d6165c3fda2372820",
				"has_community_visible_stats": true
			},
			{
				"appid": 222440,
				"name": "THE KING OF FIGHTERS 2002 UNLIMITED MATCH",
				"playtime_2weeks": 1,
				"playtime_forever": 1,
				"img_icon_url": "c9235efbfa66ad95a6ece092a7860ca8b92cfa6f",
				"img_logo_url": "787a8b76a5c9348784f50798403b2672e488c557",
				"has_community_visible_stats": true
			},
			{
				"appid": 247000,
				"name": "Talisman: Digital Edition",
				"playtime_forever": 0,
				"img_icon_url": "ab50e24b04d5fa8faf219fe622199061b57bcf20",
				"img_logo_url": "73b7daee45a29a5dfe5c0efef72223943bf8722f",
				"has_community_visible_stats": true
			}]
        self.assertEqual(gamesPulling(steamnum,APIKEY),jsonList)