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
TUMBLR_CONSUMER_KEY = 'KrSbAc9cYLmIgVAn1D21FjRR97QWsutNMxkPDFBxo8CMWtMk4M'
TUMBLR_CONSUMER_SECRET ='lKWMtL2Lj8zr5pY51PVqT8ugeoG0DjrdgoFewM0QTSyJ12jP8d'
INSTAGRAM_CLIENT_ID = '77dc10b9e3624e908ce437c0a82da92e'
INSTAGRAM_CLIENT_SECRET = '8bcf3139857149aaba7acaa61288427f'

GOOGLEMAP_API_KEY = 'AIzaSyA7tttML91EGZ32S_FOOoxu-mbxN9Ojds8'
YAHOO_CONSUMER_KEY = 'dj0yJmk9bUtPVmVpZEczZWp5JmQ9WVdrOWQxbDJkMjFhTmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1iOQ--'
YAHOO_CONSUMER_SECRET = '630e59649caf71255679853ca3f6b0580c571e98'
YAHOO_APP_ID = 'wYvwmZ64'

TWITTER_CONSUMER_KEY = 'MS8DNyi5HX9HhJgigL24VEkqA'
TWITTER_CONSUMER_SECRET = '1QdaLTNyrGIoZUniToou5bqax8mo7yuzIm7o4XjxzMhBE4UPY1'
TWITTER_ACCESS_TOKEN = '43035062-zulNy9FQtEb2i9DeRGQen62HEDf21hpwWcRVAEOOy'
TWITTER_ACCESS_TOKEN_SECRET = 'EEssSDgD4JbXzksmWHW1stBVxNtwfj1nq5Pd2Plkm17wj'

MEETUP_CONSUMER_KEY = 'p50vftdqq72tgotpaeqk5660un'
MEETUP_CONSUMER_SECRET = 'i5l00ln2r4mcf161n6451hjoj8'

BITBUCKET_CONSUMER_KEY = 'nQcSHrjPzaXRq7HjtJ'
BITBUCKET_CONSUMER_SECRET = 'd8XzR8EzgADW9GnyQGb3pZE7rWBtc2RA'

LINKEDIN_API_KEY = '7895bbnlh1k0mn'
LINKEDIN_SECRET_KEY = '7CjUx1xTsF2WDRAI'
LINKEDIN_USER_TOKEN = '806caefc-84a9-40cd-a706-445b08afec02'
LINKEDIN_USER_SECRET = '7c0e25c3-d858-4c36-8c6e-a787403bb59b'

YELP_CONSUMER_KEY = 'EXMisJNWez_PuR5pr06hyQ'
YELP_CONSUMER_SECRET = 'VCK-4cDjtQ9Ra4HC5ltClNiJFXs'
YELP_TOKEN = 'AWYVs7Vim7mwYyT1BLJA2xhNTs_vXLYS'
YELP_TOKEN_SECRET = 'Rv4GrlYxYGhxUs14s0VBfk7JLJY'
