"""
Django settings for hackathon_starter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'keuhh=0*%do-ayvy*m2k=vss*$7)j8q!@u0+d^na7mi2(^!l!d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hackathon',
    'bootstrapform',
    # 'django_openid',
    'django_nose',
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django_openid_consumer.SessionConsumer',
)

ROOT_URLCONF = 'hackathon_starter.urls'

WSGI_APPLICATION = 'hackathon_starter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=hackathon/scripts',
]

CORS_ORIGIN_ALLOW_ALL = True

############
#   KEYS   #
############

GITHUB_CLIENT_ID = 'client_id=2404a1e21aebd902f6db'
GITHUB_CLIENT_SECRET = 'client_secret=3da44769d4b7c9465fa4c812669148a163607c23'

TUMBLR_CONSUMER_KEY = 'TGxxAMUuLpvgYra68PeRtH4UUnsJd8d3ntZhR8bU0fDwC4fehI'
TUMBLR_CONSUMER_SECRET ='mWBOpPMJmo8LqEOjupTQ1caK2wNaplotvdzdwvEkKaLYpD7RIH'

INSTAGRAM_CLIENT_ID = '2daf8c0dd76c446aaaac1b401d410ae6'
INSTAGRAM_CLIENT_SECRET = 'ceacfcb7e16040d98fd47fcd00ec7a97'

GOOGLEMAP_API_KEY = 'AIzaSyA7tttML91EGZ32S_FOOoxu-mbxN9Ojds8'
YAHOO_CONSUMER_KEY = 'dj0yJmk9bUtPVmVpZEczZWp5JmQ9WVdrOWQxbDJkMjFhTmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1iOQ--'
YAHOO_CONSUMER_SECRET = '630e59649caf71255679853ca3f6b0580c571e98'
YAHOO_APP_ID = 'wYvwmZ64'

TWITTER_CONSUMER_KEY = 'sTvmcutkPQ7P4NitMtxeyR4Jt'
TWITTER_CONSUMER_SECRET = '489Q36W631BK0jQn7KtCWRzJ79WLrAkYviJmA24w6UHGLWa2nj'
TWITTER_ACCESS_TOKEN = '3226837321-ewyUwHUswg1IDoQaJ0Bz33Z9A3G65WIo1bB4pSx'
TWITTER_ACCESS_TOKEN_SECRET = 'utp3MR71pGt8ZPuB8ZIVV2RKolzg9ovZOU4ai1ihRW4XM'

MEETUP_CONSUMER_KEY = 'p50vftdqq72tgotpaeqk5660un'
MEETUP_CONSUMER_SECRET = 'i5l00ln2r4mcf161n6451hjoj8'

BITBUCKET_CONSUMER_KEY = 'nQcSHrjPzaXRq7HjtJ'
BITBUCKET_CONSUMER_SECRET = 'd8XzR8EzgADW9GnyQGb3pZE7rWBtc2RA'

LINKEDIN_CLIENT_ID = '77xt0usvr67436'
LINKEDIN_CLIENT_SECRET = 'DsbisvbSPzGx8wRY'

YELP_CONSUMER_KEY = 'EXMisJNWez_PuR5pr06hyQ'
YELP_CONSUMER_SECRET = 'VCK-4cDjtQ9Ra4HC5ltClNiJFXs'
YELP_TOKEN = 'AWYVs7Vim7mwYyT1BLJA2xhNTs_vXLYS'
YELP_TOKEN_SECRET = 'Rv4GrlYxYGhxUs14s0VBfk7JLJY'

POPAPIKEY = 'be4cd251d8a4f1a3362689088bdb0255:0:71947444'
TOPAPIKEY = 'c9655598e1fd4ff591f6d46f2321260e:17:71947444'

QUANDLAPIKEY = 'fANs6ykrCdAxas7zpMz7'

FACEBOOK_APP_ID = '885847011479129'
FACEBOOK_APP_SECRET = '9a81d5797b87885ef608463086a5c4ac'

GOOGLE_PLUS_APP_ID = '52433353167-5hvsos5pvd2i2dt62trivbqvfk4qc2pv.apps.googleusercontent.com'
GOOGLE_PLUS_APP_SECRET = 'mv1ZcpHqMF6uX7NRTLDC2jXR'

DROPBOX_APP_ID = '8et85bx2ur6b1fb'
DROPBOX_APP_SECRET = 'xx0virsvtghxlui'

FOURSQUARE_APP_ID = '2V342MA2PZQEKABT450WJQKKRHV0QPFMOUBA1ZHXKWZ5YZ1Y'
FOURSQUARE_APP_SECRET = 'PC0O1JQWP24EAPPLXNRIJVVBN5D2DW3XD5GJGGSQWIESYN1B'
