Django Hackathon Starter
------------------------

## What is Django Hackathon Starter

> Django Hackathon Starter aims to be a project which will aggegrate data from several APIs, producing a RESTful API which can be consumed by a client (also intended to be built). 

Our deployment can be found [here](http://django-hackathon-starter.herokuapp.com/hackathon/).

## Running this project

In order to run this project, do the following:

    # Install the requirements
    pip install -r requirements.txt

    # Perform database migrations
    python manage.py migrate

    # Run the server
    python manage.py runserver

## Front End dependencies

This project relies on Bower for all front end libraries, to avoid pushing up large libraries such as `jQuery` and `Bootstrap`. **Under no circumstance should any front-end libraries manually be pushed up to the repository.** To install `bower`, you will need to install `npm`, which now comes bundled with `node.js`. To install `npm`, simply install [node as follows](https://github.com/joyent/node/wiki/installing-node.js-via-package-manager). 

First, install `bower`:

    npm install -g bower

Then:

    # In the same directory as requirements.txt
    bower install

This will download and extract all the packages listed within `bower.json`. 

Then:

    # move bower_components into static folder
    mv bower_components/ hackathon_starter/hackathon/static

To install the front-end dependencies for the AngularJS client, do the following:

    cd public
    bower install
    # Rename bower_components folder to vendor
    mv bower_components/ vendor/


## Testing

This project aims to be as close to 100% tested as possible. For a good guide to testing using Python and `Mock`, `Nosetests` and `Unittests` libraries, please [read here](http://docs.python-guide.org/en/latest/writing/tests/).

To run the tests:

    hackthon-starter $ python manage.py test hackathon/unittests/

## Code evaluation

In order to write clean code with a consistent style guide, we'll be using `Pylint` to maintain our code. Pylint will display a ton of messages regarding things that should be fixed. 


## RESTful endpoints

Using the `Django REST framework`, the current RESTful endpoints exist:

    http://127.0.0.1:8000/hackathon/snippets/

The list will appear empty at first, since the database model `Snippets` will be empty. To populate it with some sample data, run the following:

    python manage.py shell
    from hackathon.models import Snippet
    from hackathon.serializers import SnippetSerializer
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser

    snippet = Snippet(code='foo = "bar"\n')
    snippet.save()

    snippet = Snippet(code='print "hello, world"\n')
    snippet.save()

The above will open the Django shell, and allow you to create objects and save them to the database. If you then navigate to the URL above, you will see the JSON output of the database model, `Snippet`. 

## Django JSON Response Endpoints

As of `Django 1.7x`, there is a new method called `JsonResponse` which allows the user to send JSON data to a URL which makes it available to be consumed by any client. The following endpoints exist:

* `http://127.0.0.1:8000/hackathon/steamDiscountedGames/`: JSON output containing steam discounts data
* `http://127.0.0.1:8000/hackathon/instagramUser/`: JSON output containing data from an Instagram user through OAuth
* `http://127.0.0.1:8000/hackathon/githubUser/`: JSON output containing data from a Github User

## AngularJS Client

As of `April 11th, 2015`, there is now a sample AngularJS client which pulls data from the Django sample API endpoint: `http://127.0.0.1:8000/hackathon/snippets/`. To test it, do the following:

* Within the `public/` directory, run `python -m SimpleHTTPServer 80`. You may need `sudo` on your respective Operating System.
* Navigate to: `http://localhost/#/snippets`. Here you will see whatever content was stored within the database model, `Snippet`. If nothing shows up, go back to the `RESTful endpoints` step to populate your database with some `Snippet` objects. 

The following other links are available on the AngularJS Client:

* `http://localhost/#/githubUser`: Pulls JSON response for Github data from Django 
* `http://localhost/#/steamSales`: Pulls JSON response for Steam sales data from Django

## Ionic Client

As of `April 11th, 2015`, there is now a sample Ionic application which works on iOS. This application pulls data from the Django sample API endpoint: `http://127.0.0.1:8000/hackathon/snippets/`. In order to successfully run this project, you must do the following:

    # Make sure django-hackathon-starter is running
    python manage.py runserver

    # Install cordova and ionic
    # On a Mac, you'll need to use sudo
    npm install -g cordova ionic 

    cd ionic

    # Add support for the iOS platform
    ionic platform add ios

    # Build the project
    ionic build ios

Running the final command, `ionic build ios` will generate an `.xcodeproj` file within `platforms/ionic`. You can open it and then run it, which you should then see a list of all the `Snippet` objects from the Django Hackathon Starter database. 

You can also test the project in the browser by doing the following:

    cd ionic
    ionic serve 

Running `ionic serve` will automatically open up your web browser and run the application.


## Building the documentation

In order to build the documentation for this project:

    $ cd hackathon_starter
    $ make html

The output is stored within `_build/html`. Open up `index.html` to view the documentation.

## Contributors

* David Leonard
* Eswari Swarna
* Marco Quezada 
* Wan Kim Mok
