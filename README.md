Django Hackathon Starter
------------------------

A boilerplate application for Django web applications.

If you've attented hackathons, you already know how much time can be wasted figuring out what language to pick, which web framework to choose, which APIs to incorporate, and figuring out OAuth authentication. Django Hackathon Starter aims to provide these features out of the box, allowing the team to save hours of time getting these pieces together.

Even if you are not using this for a hackathon, Django Hackathon Starter is sure to save any developer hours or even days of development time and can serve as a learning guide.

Basic Authentication / OAuth Signin

![Login](https://github.com/DrkSephy/drksephy.github.io/blob/master/img/login.png)

API Examples

![API Examples](https://github.com/DrkSephy/drksephy.github.io/blob/master/img/api_examples.png)

Twitter Example

![Twitter Tweets](https://github.com/DrkSephy/drksephy.github.io/blob/master/img/twitter.png)


Getting Started
---------------
To get up and running, simply do the following:

    git clone https://github.com/DrkSephy/django-hackathon-starter.git
    cd django-hackathon-starter
    # Install the requirements
    pip install -r requirements.txt
    # Install bower
    npm install -g bower
    bower install
    mv bower_components/ hackathon_starter/hackathon/static
    # Perform database migrations
    python manage.py makemigrations
    python manage.py migrate

**NOTE**: We highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via pip.

**NOTE**: To get you up and running quickly, we have provided dummy API keys for use. We highly recommend setting up your own keys and replacing them within `settings.py`. 

    
Getting API Keys
----------------
# YELP #

1. Register an account on [Yelp.com](http://www.yelp.com/).
2. Visit the [Yelp for developers page](https://www.yelp.com/developers/manage_api_keys).
3. You will obtain the following: `CONSUMER KEY`, `CONSUMER SECRET`, `TOKEN`, `TOKEN_SECRET`. 
4. Within `settings.py`, add the following:
    * `YELP_CONSUMER_KEY` = `Yelp Consumer Key`
    * `YELP_CONSUMER_SECRET` = `Yelp Consumer Secret`
    * `YELP_TOKEN` = `Yelp Token`
    * `YELP_TOKEN_SECRET` = `Yelp Token Secret`

# MEETUP #

1. Register an account on [Meetup.com](http://www.meetup.com/).
2. Visit [Meetup OAuth Consumers page](https://secure.meetup.com/meetup_api/oauth_consumers/).
    * Enter a project name for the `consumer name` field.
    * For `redirect url` field, enter: `http://127.0.0.1:8000/hackathon/`.
3. Within `settings.py`, add the following:
    * `MEETUP_CONSUMER_KEY` = `Meetup key`
    * `MEETUP_CONSUMER_SECRET` = `Meetup secret key` 

# TWILIO 

1. Register an account on [Twilio.com](https://www.twilio.com/).
2. Get your [Twilio Number](https://www.twilio.com/user/account/phone-numbers/incoming).
3. [Setup the numbers](https://www.twilio.com/user/account/phone-numbers/incoming) you want to be able to send messages to. 
4. Grab your `account_sid` and `auth_token` [here](https://www.twilio.com/user/account/voice-messaging).
5. Within `scripts/twilioapi.py`:
    * Replace `account_sid` with your own Twilio `account_sid`.
    * Replace `auth_token` with your own Twilio `auth_token`. 

# GITHUB #

1. Register an account on [Github.com](http://www.github.com/).
2. Visit [Github developer applications page](https://github.com/settings/developers).
3. Click on **Register new application**.
    * Enter `Application name` and `Homepage URL` field.
    * For `redirect url` field, enter: `http://127.0.0.1:8000/hackathon/`.
4. Click **Register application**.
5. Within `settings.py`, add the following:
    * `GITHUB_CLIENT_ID` = `Github-client-id`
    * `GITHUB_CLIENT_SECRET` = `Github-client-secret`

# TWITTER #

1. Register an account on [Twitter.com](http://www.twitter.com/).
2. Visit [Twitter application management page](https://apps.twitter.com/).
3. Click on **Create New App**.
    * Enter `Application name`, `Description`, and `Website` field.
    * For `Callback URL` field, enter: `http://127.0.0.1:8000/hackathon/`.
4. Click **Create your Twitter application**.
5. Go to the **Permissions** tab.
6. Under *Access*, select **Read and Write* type.
7. Go to **Keys and Access Tokens ** tab.
8. Under *Your Access Token*, click on **Create my access token** to generate access tokens.
9. Within `settings.py`, add the following:
    * `TWITTER_CONSUMER_KEY` = `Twitter-consumer-key`
    * `TWITTER_CONSUMER_SECRET` = `Twitter-consumer-secret`
    * `TWITTER_ACCESS_TOKEN` = `Twitter-access-token`
    * `TWITTER_ACCESS_TOKEN_SECRET` = `Twitter-access-token-secret`

# INSTAGRAM #

1. Register an account on [Instagram.com](http://www.instagram.com/).
2. Visit [Instagram manage clients page](https://instagram.com/developer/clients/manage/).
3. Click on **Register a New Client**.
    * Enter `Application name`, `Description`, and `Website URL` field.
    * For `Redirect URI` field, enter: `http://127.0.0.1:8000/hackathon/`.
4. Within `settings.py`, add the following:
    * `INSTAGRAM_CLIENT_ID` = `Instagram-client-id`
    * `INSTAGRAM_CLIENT_SECRET` = `Instagram-client-secret`

# LINKEDIN #

1. Register an account on [Linkedin.com](http://www.linkedin.com/).
2. Visit [Linkedin developer Network page](https://www.linkedin.com/secure/developer).
3. Click on **Add New Application**.
    * Enter `Company Info`, `Application Info`, and `Contact Info` section.
    * Under `OAuth User Agreement` section, select scopes needed.
    * For `OAuth 2.0 Redirect URLs` field, enter: `http://127.0.0.1:8000/hackathon/`.
4. Click **Add Application**.
5. Within `settings.py`, add the following:
    * `LINKEDIN_CLIENT_ID` = `Linkedin-client-id`
    * `LINKEDIN_CLIENT_SECRET` = `Linkedin-client-secret`

# FACEBOOK #

1. Register an account on [Facebook.com](http://www.facebook.com.com/).
2. Visit [Facebook Developer Network page](https://developers.facebook.com/).
3. After logging in, Click on **My Apps** and then on **Add a New App+**.
    * Choose Website as the platform and add the **name** for your project.
    * Click on **Create New Facebook APP ID** and choose the **Category** of your application
    * Click **Create App ID**
4. After the captcha, scroll down past the quick start and add http://localhost:8000/'.
5. Within your `views.py` add the **App ID** in `yourappid` underneath the view for your facebook application.

# STEAM #

1. Register an account on [Steam](https://store.steampowered.com/join/).
2. Visit [Steam Community developers page](https://steamcommunity.com/login/home/?goto=%2Fdev%2Fapikey).
3. After logging in, add the **Domain Name** as the name of your application and **key** is shown.
4. Within your `views.py` add the **Key** in `key` underneath the view for your steam application.

# NY TIMES #

1. Register an account on [NY Times Developer Network](http://developer.nytimes.com/docs).
2. Click on [Register](https://myaccount.nytimes.com/register).
3. After logging in, click on **APIs** (http://developer.nytimes.com/apps/register) 
    *Write in the **Name** of your application and click each **sub-API** that you will use.
    * Agree to the **Terms of Service** and click on **Register Application**
4. Within your `settings.py` add the following:
    * `POPAPIKEY` = `Most Popular API`
    * `TOPAPIKEY` = `Top Stories API`

# QUANDL #
1. Register an account on [Quandl](https://www.quandl.com/)
2. After logging in, click on **Me** and then **Account settings** to find the API key. 
3. Within your `settings.py`add `QUANDLAPIKEY` = `Key` 
