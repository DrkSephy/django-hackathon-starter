Django Hackathon Starter
------------------------

A boilerplate application for Django web applications.

If you've attented hackathons, you already know how much time can be wasted figuring out what language to pick, which web framework to choose, which APIs to incorporate, and figuring out OAuth authentication. Django Hackathon Starter aims to provide these features out of the box, allowing the team to save hours of time getting these pieces together.

Even if you are not using this for a hackathon, Django Hackathon Starter is sure to save any developer hours or even days of development time and can serve as a learning guide for web developers.

<h4 align="center">Basic Authentication / OAuth Signin </h4>

![Login](https://github.com/DrkSephy/drksephy.github.io/blob/master/img/login.png)

<h4 align="center">API Examples </h4>

![API Examples](https://github.com/DrkSephy/drksephy.github.io/blob/master/img/api_examples.png)

<h4 align="center">Twitter Example </h4>

![Twitter Tweets](http://i.imgur.com/tHZrgoK.png)

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
* Basic Authentication with username and password
* **OAuth 2.0 Authentication** for Github, LinkedIn and Instagram
* **OAuth 1.0a Authentication** for Twitter and Tumblr
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

**NOTE**: To get you up and running quickly, we have provided dummy API keys for use. We highly recommend setting up your own keys and replacing them within `settings.py`. 


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
2. Visit [Facebook Developer Network page](https://developers.facebook.com/)
3. After logging in, Click on **My Apps** and then on **Add a New App+**
    * Choose Website as the platform and add the **name** for your project
    * Click on **Create New Facebook APP ID** and choose the **Category** of your application
    * Click **Create App ID**
4. After the captcha, scroll down past the quick start and add `http://localhost:8000/`
5. Within your `views.py` add the **App ID** in `yourappid` underneath the view for your facebook application.


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

<img src="http://planetcassandra.org/blogs/Upload/Postddfdbb6f-16ed-4e1c-8e29-ff2cf0cb43a1/quandl.png" width="200">

1. Register an account on [Quandl](https://www.quandl.com/)
2. After logging in, click on **Me** and then **Account settings** to find the API key 
3. Within your `settings.py`add `QUANDLAPIKEY` = `Key` 

<hr>

Project Structure
-----------------


| Name                               | Description                                                 |
| ---------------------------------- |:-----------------------------------------------------------:|
| **hackathon_starter**/settings.py | Django settings module containing database and API keys/tokens.|
| **hackathon**/admin.py            | Registered models for Django's admin page.|
| **hackathon**/models.py           | Django models and profiles for user login.|
| **hackathon**/tests.py            | Integration tests.|
| **hackathon**/urls.py             | Django Hackathon Starter URL dispatcher.|
| **hackathon**/views.py            | Django views file.|
| **hackathon**/serializers.py      | Allows JSON representation for Django Model fields.|
| **hackathon**/forms.py            | Basic form fields.|
| **hackathon/static/**             | Front-end JavaScript / CSS files.|
| **hackathon/unittests**           | Unit tests.|
| **hackathon/scripts/**            | API Example scripts.|
| **hackathon/scripts/**github.py   | Script for interacting with Github API.   |
| **hackathon/scripts/**instagram.py| Script for interacting with Instagram API.|
| **hackathon/scripts/**linkedin.py | Script for interacting with LinkedIn API. |
| **hackathon/scripts/**meetup.py   | Script for interacting with Meetup API. |
| **hackathon/scripts/**nytimes.py  | Script for interacting with New York Times API. |
| **hackathon/scripts/**quandl.py   | Script for interacting with Quandl API. |
| **hackathon/scripts/**scraper.py  | Basic web scraper for getting sales from Steam.            |
| **hackathon/scripts/**steam.py                      | Script for interacting with Steam API.   |
| **hackathon/scripts/**tumblr.py                     | Script for interacting with Tumblr API.  |
| **hackathon/scripts/**twilioapi.py                  | Script for interacting with Twilio API.  |
| **hackathon/scripts/**twitter.py                    | Script for interacting with Twitter API. |
| **hackathon/scripts/**yelp.py                       | Script for interacting with Yelp API. |
| **hackathon/templates/**hackathon/                  | Templates for API examples. |
| **hackathon/templates/**hackathon/base.html         | Base template, contains navbar. |
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


