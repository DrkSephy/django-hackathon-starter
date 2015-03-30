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

This project relies on Bower for all front end libraries, to avoid pushing up large libraries such as `jQuery` and `Bootstrap`. To install `bower`, you will need to install `npm`, which now comes bundled with `node.js`. To install `npm`, simply install [node as follows](https://github.com/joyent/node/wiki/installing-node.js-via-package-manager). 

First, install `bower`:

    npm install -g bower

Then:

    bower install

This will download and extract all the packages listed within `bower.json`. **Under no circumstance should any front-end libraries manually be pushed up to the repository.**

Two routes have currently been set up, which are located at:

    # First test route
    http://127.0.0.1:8000/hackathon/

    # Second test route
    http://127.0.0.1:8000/hackathon/test


## Testing

This project aims to be as close to 100% tested as possible. For a good guide to testing using Python and `Mock`, `Nosetests` and `Unittests` libraries, please [read here](http://docs.python-guide.org/en/latest/writing/tests/).

To run the tests:

    hackthon-starter $ nosetests --with-coverage --cover-package=hackathon/

You will see an output as shown below:

    Name                                   Stmts   Miss  Cover   Missing
    --------------------------------------------------------------------
    hackathon/__init__.py                      0      0   100%
    hackathon/admin.py                         3      3     0%   1-5
    hackathon/forms.py                         9      9     0%   1-11
    hackathon/migrations/0001_initial.py       6      6     0%   2-14
    hackathon/migrations/__init__.py           0      0   100%
    hackathon/models.py                        6      6     0%   1-11
    hackathon/scripts/__init__.py              0      0   100%
    hackathon/scripts/samplescript.py          5      5     0%   3-10
    hackathon/scripts/steam.py                17     17     0%   1-24
    hackathon/tests.py                         1      0   100%
    hackathon/urls.py                          3      3     0%   1-5
    hackathon/views.py                        52     52     0%   1-120
    --------------------------------------------------------------------
    TOTAL                                    102    101     1%
    ----------------------------------------------------------------------
    Ran 0 tests in 0.194s

## Contributors

* David Leonard
* Eswari Swarna
* Marco Quezada 
* Wan Kim Mok
