Django Hackathon Starter
------------------------

A boilerplate application for Django web applications.

If you've attented hackathons, you already know how much time can be wasted figuring out what language to pick, which web framework to choose, which APIs to incorporate, and figuring out OAuth authentication. Django Hackathon Starter aims to provide these features out of the box, allowing the team to save hours of time getting these pieces together.

Even if you are not using this for a hackathon, Django Hackathon Starter is sure to save any developer hours or even days of development time and can serve as a learning guide for web developers.

<h4 align="center">Basic Authentication / OAuth Signin </h4>

![Login](http://i.imgur.com/sEIHsIS.png)

<h4 align="center">API Examples </h4>

![API Examples](http://i.imgur.com/zFqKcVa.png)

Table of Contents
-----------------

- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Obtaining API Keys](#getting-api-keys)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

Features
--------
* User Registration
* Sphinx Documentation
* Django Nosetests
* Integration with Django Rest Framework
* Basic Authentication with username and password
* **OAuth 2.0 Authentication**
    * Github
    * LinkedIn
    * Instagram
    * Facebook
    * Google+
    * Dropbox
    * Foursquare
* **OAuth 1.0a Authentication** 
    * Twitter
    * Tumblr
* **API Examples**
    * Yelp API
    * Github API
    * Instagram API
    * Tumblr API
    * Twitter API
    * Twilio API
    * Meetup API
    * Steam API
    * Quandl Stock API
    * New York Times API
    * LinkedIn API
    * Facebook API
    * Google+ API
    * Dropbox API
    * Foursquare API

<hr>


Pre-requisites
--------------

This project relies on `bower` for front-end dependencies, which in turn requires [npm](https://www.npmjs.com/). `npm` is now bundled with `NodeJS`, which you can download and install [here](https://nodejs.org/download/).

For Python-specific libraries, this project relies on [pip](https://pypi.python.org/pypi/pip). The easiest way to install `pip` can be [found here](https://pip.pypa.io/en/latest/installing.html).

Getting Started
---------------
To get up and running, simply do the following:

    $ git clone https://github.com/DrkSephy/django-hackathon-starter.git
    $ cd django-hackathon-starter

    # Install the requirements
    $ pip install -r requirements.txt

    # Install bower
    $ npm install -g bower
    $ bower install

    # Perform database migrations
    $ python manage.py makemigrations
    $ python manage.py migrate


**NOTE**: We highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via [pip](https://pypi.python.org/pypi/pip).

<hr>

Getting API Keys
----------------

<img src="https://rentpost.com/blog/wp-content/uploads/2015/01/yelp.png" width="200">

1. Register an account on [Yelp.com](http://www.yelp.com/)
2. Visit the [Yelp for developers page](https://www.yelp.com/developers/manage_api_keys)
3. You will obtain the following: `CONSUMER KEY`, `CONSUMER SECRET`, `TOKEN`, `TOKEN_SECRET`
4. Within `settings.py`, add the following:
    * `YELP_CONSUMER_KEY` = `Yelp Consumer Key`
    * `YELP_CONSUMER_SECRET` = `Yelp Consumer Secret`
    * `YELP_TOKEN` = `Yelp Token`
    * `YELP_TOKEN_SECRET` = `Yelp Token Secret`

<hr>

<img src="https://lh5.ggpht.com/4RfLjWcvlfdFWfxeDcpZxJLWhDytkQhQd2qLSqMhForQoILXf9HqmMD6DNmpbzJzaQ=w300" width="200">

1. Register an account on [Meetup.com](http://www.meetup.com/)
2. Visit [Meetup OAuth Consumers page](https://secure.meetup.com/meetup_api/oauth_consumers/)
    * Enter a project name for the `consumer name` field
    * For `redirect url` field, enter: `http://127.0.0.1:8000/hackathon/`
3. Within `settings.py`, add the following:
    * `MEETUP_CONSUMER_KEY` = `Meetup key`
    * `MEETUP_CONSUMER_SECRET` = `Meetup secret key`

<hr>

<img src="https://tctechcrunch2011.files.wordpress.com/2012/11/twilio-logo-6a141664f35a78e9ac08eed627c2a859.png" width="300">  

1. Register an account on [Twilio.com](https://www.twilio.com/)
2. Get your [Twilio Number](https://www.twilio.com/user/account/phone-numbers/incoming)
3. [Setup the numbers](https://www.twilio.com/user/account/phone-numbers/incoming) you want to be able to send messages to
4. Grab your `account_sid` and `auth_token` [here](https://www.twilio.com/user/account/voice-messaging)
5. Within `scripts/twilioapi.py`:
    * Replace `account_sid` with your own Twilio `account_sid`
    * Replace `auth_token` with your own Twilio `auth_token`

<hr>

<img src="http://3.bp.blogspot.com/-gSyd39LDMRk/TzpVnaZ7ELI/AAAAAAAAEfg/9w1iB-mn5ZM/s1600/github-socialcoding-logo.png" width="300">

1. Register an account on [Github.com](http://www.github.com/).
2. Visit [Github developer applications page](https://github.com/settings/developers)
3. Click on **Register new application**.
    * Enter `Application name` and `Homepage URL` field
    * For `redirect url` field, enter: `http://127.0.0.1:8000/hackathon/`
4. Click **Register application**.
5. Within `settings.py`, add the following:
    * `GITHUB_CLIENT_ID` = `Github-client-id`
    * `GITHUB_CLIENT_SECRET` = `Github-client-secret`

<hr>

<img src="https://g.twimg.com/Twitter_logo_blue.png" width="100">

1. Register an account on [Twitter.com](http://www.twitter.com/)
2. Visit [Twitter application management page](https://apps.twitter.com/)
3. Click on **Create New App**
    * Enter `Application name`, `Description`, and `Website` field
    * For `Callback URL` field, enter: `http://127.0.0.1:8000/hackathon/`
4. Click **Create your Twitter application**
5. Go to the **Permissions** tab
6. Under *Access*, select **Read and Write** type
7. Go to **Keys and Access Tokens** tab
8. Under *Your Access Token*, click on **Create my access token** to generate access tokens
9. Within `settings.py`, add the following:
    * `TWITTER_CONSUMER_KEY` = `Twitter-consumer-key`
    * `TWITTER_CONSUMER_SECRET` = `Twitter-consumer-secret`
    * `TWITTER_ACCESS_TOKEN` = `Twitter-access-token`
    * `TWITTER_ACCESS_TOKEN_SECRET` = `Twitter-access-token-secret`

<hr>

<img src="http://thinkpynk.com/wp-content/uploads/2015/04/instagram-logo.png" width="200">

1. Register an account on [Instagram.com](http://www.instagram.com/).
2. Visit [Instagram manage clients page](https://instagram.com/developer/clients/manage/)
3. Click on **Register a New Client**
    * Enter `Application name`, `Description`, and `Website URL` field
    * For `Redirect URI` field, enter: `http://127.0.0.1:8000/hackathon/`
4. Within `settings.py`, add the following:
    * `INSTAGRAM_CLIENT_ID` = `Instagram-client-id`
    * `INSTAGRAM_CLIENT_SECRET` = `Instagram-client-secret`

<hr>

<img src="http://blogs.kenan-flagler.unc.edu/wp-content/uploads/2013/10/LinkedIn-Logo-2C.png" width="200">

1. Register an account on [Linkedin.com](http://www.linkedin.com/).
2. Visit [Linkedin developer Network page](https://www.linkedin.com/secure/developer)
3. Click on **Add New Application**
    * Enter `Company Info`, `Application Info`, and `Contact Info` section
    * Under `OAuth User Agreement` section, select scopes needed
    * For `OAuth 2.0 Redirect URLs` field, enter: `http://127.0.0.1:8000/hackathon/`
4. Click **Add Application**
5. Within `settings.py`, add the following:
    * `LINKEDIN_CLIENT_ID` = `Linkedin-client-id`
    * `LINKEDIN_CLIENT_SECRET` = `Linkedin-client-secret`

<hr>

<img src="http://www.freelargeimages.com/wp-content/uploads/2014/11/Facebook_logo-6.jpg" width="200">

1. Register an account on [Facebook.com](http://www.facebook.com.com/)
2. Visit [Facebook Developers page](https://developers.facebook.com/)
3. After logging in, Click on **My Apps** and then on **Add a New App**
    * Choose W**ebsite** as the platform and add the **name** for your project
    * Give your app a name.
    * Choose the category your app falls into.
    * Click **Create App ID**
    * Skip the quickstart process and you will be redirected to the app dashboard.
4. Copy the **app ID** and the **app secret**.
5. From the left menu choose the **Settings** option.
6. Click on **Add Platform** and choose **Website** once again.
7. Under **site URL**, specift the URL to be redirected after authentication is complete.
8. Click save.
9. In ```settings.py``` change the following values:
    * ```FACEBOOK_APP_ID = your_app_id```
    * ```FACEBOOK_APP_SECRET = your_app_secret```


<hr>

<img src="http://icons.iconarchive.com/icons/marcus-roberto/google-play/512/Google-plus-icon.png" width="200" />

1. Register an account on [Google.com](https://accounts.google.com/signup).
2. Navigate to [Google Developer Console](https://console.developers.google.com/project).
3. Click on **Create Project**, give your app a name and click **Create** (this might take a few sceonds).
4. You will be redirected to the project dashboard. From the left menu choose **APIs & auth** and then choose **APIs**.
5. Choose the API you would like to use (the built in example uses **Google+ API**).
6. Click on **Enable API**.
7. From the side menu, under **APIs & auth** select **consent screen**.
    * Fill your app name under **Product Name**.
    * Hit **save** button on the bottom.
8. From the side menu, under **APIs & auth** select credentials:
    * Click on **Create new Client ID**.
    * Under **Authorized JavaScript origins** specify you app base address (e.g ```http://localhost:8000```).
    * Under **Authorized redirect URIs** specify the URL to be redirected after authentication is complete.
    * Hit **Create Client ID** button (this might also take a few seconds).
9. Copy your new generated ```client_id``` and ```client_secret```:
10. Under ```settings.py``` change the following values:
    * ```GOOGLE_PLUS_APP_ID = your_client_id```
    * ```GOOGLE_PLUS_APP_SECRET = your_client_secret```

<hr>

<img src="https://cf.dropboxstatic.com/static/images/brand/logotype-vflFbF9pY.png" width="200">

1. Register an account on [Dropbox.com](http://www.dropbox.com).
2. Navigate to [Dropbox Developers](https://www.dropbox.com/developers).
3. From the side menu, select **App Console** and click on **Create app**.
4. Configure the app permissions. This example uses the following configuration:
    * App type- Dropbox API app
    * My app needs access to files already on Dropbox.
    * My app needs access to a user's full Dropbox.
    * **Note:** This kind of configuration will require you to submit your app for approval.
5. Give your app a name and click the **Create app button**.
6. You will be redirected to the app console:
    * Under **Redirect URIs** specify the URL to be redirected after authentication is complete (e.g ```http://locahost:8000/home```) and click **add**.
    * Copy your ```App key``` and ```App secret```.
7. Under ```settings.py``` change the following values:
    * ```DROPBOX_APP_ID = your_app_id```
    * ```DROPBOX_APP_SECRET = your_app_secret```
<hr>

<img src='http://www.atlantamusicguide.com/wp-content/uploads/foursquare-logo.png' width="200">

1. Register and account on [Foursquare.com](https://foursquare.com).
2. Navigate to [Foursquare For Developers](https://developer.foursquare.com).
3. From the top menu bar select **My Apps** and you will be redirected to the app dashboard.
4. Hit **Create a New App**:
    * Give your app a name.
    * Under **Download / welcome page url**, specify your app main url (e.g ```http://www.localhost:8000```).
    * Under **Redirect URI**, specify the URL to be redirected after authentication is complete (e.g ```http://locahost:8000/home```) and click **add**.
    * Scroll all the way to the botttom and hit **Save Changes**.
5. From the App page you were redirected to, copy your ```App key``` and ```App secret```.
6. Under ```settings.py``` change to following values:
    * ```FOURSQUARE_APP_ID = your_client_id```
    * ```FOURSQUARE_APP_SECRET = your_app_secret```
<hr>


<img src="https://secure.assets.tumblr.com/images/logo_page/img_logotype_34465d_2x.png" width="200">

1. Register an account on Tumblr.com.
2. Visit Tumblr applications page.
3. Click on Register Application.
    * Enter your application information.
    * For Default callback URL field, enter: http://127.0.0.1:8000/hackathon/.
4. Click Register.
5. Within settings.py, add the following:
    * TUMBLR_CONSUMER_KEY = `Tumblr-consumer-key`
    * TUMBLR_CONSUMER_SECRET = `Tumblr-consumer-secret`

<hr>


<img src="http://games.overpress.it/wp-content/uploads/sites/7/2014/10/steam-logo-10.jpg" width="200">

1. Register an account on [Steam](https://store.steampowered.com/join/)
2. Visit [Steam Community developers page](https://steamcommunity.com/login/home/?goto=%2Fdev%2Fapikey)
3. After logging in, add the **Domain Name** as the name of your application and **key** is shown
4. Within your `views.py` add the **Key** in `key` underneath the view for your steam application


<hr>

<img src="http://upload.wikimedia.org/wikipedia/commons/7/77/The_New_York_Times_logo.png" width="200">

1. Register an account on [NY Times Developer Network](http://developer.nytimes.com/docs)
2. Click on [Register](https://myaccount.nytimes.com/register)
3. After logging in, click on **APIs** (http://developer.nytimes.com/apps/register)
    Write in the **Name** of your application and click each **sub-API** that you will use
    * Agree to the **Terms of Service** and click on **Register Application**
4. Within your `settings.py` add the following:
    * `POPAPIKEY` = `Most Popular API`
    * `TOPAPIKEY` = `Top Stories API`

<hr>

<img src="http://qph.is.quoracdn.net/main-qimg-45312af6930eb01c3c68db9bb30bcad8?convert_to_webp=true" width="200">

1. Register an account on [Quandl](https://www.quandl.com/)
2. After logging in, click on **Me** and then **Account settings** to find the API key
3. Within your `settings.py`add `QUANDLAPIKEY` = `Key`

<hr>

Project Structure
-----------------


| Name                               | Description                                                 |
| ---------------------------------- |:-----------------------------------------------------------:|
| **hackathon_starter**/settings.py | Django settings module containing database and API keys/tokens|
| **hackathon**/admin.py            | Registered models for Django's admin page|
| **hackathon**/models.py           | Django models and profiles for user login|
| **hackathon**/tests.py            | Integration tests|
| **hackathon**/urls.py             | Django Hackathon Starter URL dispatcher|
| **hackathon**/views.py            | Django views file|
| **hackathon**/serializers.py      | Allows JSON representation for Django Model fields|
| **hackathon**/forms.py            | Basic form fields|
| **hackathon/static/**             | Front-end JavaScript / CSS files|
| **hackathon/unittests**           | Unit tests|
| **hackathon/scripts/**            | API Example scripts|
| **hackathon/scripts/**github.py   | Script for interacting with Github API   |
| **hackathon/scripts/**instagram.py| Script for interacting with Instagram API|
| **hackathon/scripts/**linkedin.py | Script for interacting with LinkedIn API |
| **hackathon/scripts/**meetup.py   | Script for interacting with Meetup API |
| **hackathon/scripts/**nytimes.py  | Script for interacting with New York Times API |
| **hackathon/scripts/**quandl.py   | Script for interacting with Quandl API |
| **hackathon/scripts/**scraper.py  | Basic web scraper for getting sales from Steam            |
| **hackathon/scripts/**facebook.py | Script for interacting with Facebook API |
| **hackathon/scripts/**dropbox.py  | Script for interacting with Dropbox API |
| **hackathon/scripts/**foursquare.py | Script for interacting with Foursquare API |
| **hackathon/scripts/**googlePlus.py | Script for interacting with Google+ API |
| **hackathon/scripts/**steam.py                      | Script for interacting with Steam API   |
| **hackathon/scripts/**tumblr.py                     | Script for interacting with Tumblr API  |
| **hackathon/scripts/**twilioapi.py                  | Script for interacting with Twilio API  |
| **hackathon/scripts/**twitter.py                    | Script for interacting with Twitter API |
| **hackathon/scripts/**yelp.py                       | Script for interacting with Yelp API |
| **hackathon/templates/**hackathon/                  | Templates for API examples |
| **hackathon/templates/**hackathon/base.html         | Base template, contains navbar |

Contributing
------------

We welcome contributions of all kinds. If you would like to know what work is needed to be done, check the [issue tracker](https://github.com/DrkSephy/django-hackathon-starter/issues). Before sending a pull request, please open an issue. This project follows the [pep-0008](https://www.python.org/dev/peps/pep-0008/) style guide.


LICENSE
-------

The MIT License (MIT)

Copyright (c) 2015 David Leonard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
