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

    hackthon-starter $ nosetests unittests/ --cover-package=scripts/ --with-coverage

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

## Code evaluation

In order to write clean code with a consistent style guide, we'll be using `Pylint` to maintain our code. Pylint will display a ton of messages regarding things that should be fixed. A sample output from running `pylint views.py` is shown below:

    (web)λ pylint views.py
    No config file found, using default configuration
    ************* Module hackathon.views
    C:  7, 0: Trailing whitespace (trailing-whitespace)
    W: 11, 0: Found indentation with tabs instead of spaces (mixed-indentation)
    W: 12, 0: Found indentation with tabs instead of spaces (mixed-indentation)
    W: 15, 0: Found indentation with tabs instead of spaces (mixed-indentation)
    C: 59, 0: Wrong continued indentation.
                'hackathon/register.html',
                ^     | (bad-continuation)
    C: 60, 0: Wrong continued indentation.
                {'user_form': user_form, 'registered': registered} )
                ^     | (bad-continuation)
    C: 60, 0: No space allowed before bracket
                {'user_form': user_form, 'registered': registered} )
                                                                   ^ (bad-whitespace)
    C: 69, 0: Line too long (103/100) (line-too-long)
    C:116, 0: Exactly one space required after comma
        return render(request,'hackathon/steam.html', {"game": game })
                             ^ (bad-whitespace)
    C:116, 0: No space allowed before bracket
        return render(request,'hackathon/steam.html', {"game": game })
                                                                    ^ (bad-whitespace)
    C:  1, 0: Missing module docstring (missing-docstring)
    W:  7, 0: Relative import 'scripts.steam', should be 'hackathon.scripts.steam' (relative-import)
    C: 10, 0: Missing function docstring (missing-docstring)
    C: 14, 0: Missing function docstring (missing-docstring)
    W: 14, 9: Unused argument 'request' (unused-argument)
    C: 17, 0: Missing function docstring (missing-docstring)
    C: 21, 0: Missing function docstring (missing-docstring)
    C: 62, 0: Missing function docstring (missing-docstring)
    C:103, 0: Missing function docstring (missing-docstring)
    C:110, 0: Missing function docstring (missing-docstring)
    C:113, 4: Invalid variable name "SteamUN" (invalid-name)
    C:114, 4: Invalid variable name "steamID" (invalid-name)
    C:118, 0: Missing function docstring (missing-docstring)
    W:  4, 0: Unused RequestContext imported from django.template (unused-import)
    W:  4, 0: Unused loader imported from django.template (unused-import)


    Report
    ======
    53 statements analysed.

    Statistics by type
    ------------------

    +---------+-------+-----------+-----------+------------+---------+
    |type     |number |old number |difference |%documented |%badname |
    +=========+=======+===========+===========+============+=========+
    |module   |1      |NC         |NC         |0.00        |0.00     |
    +---------+-------+-----------+-----------+------------+---------+
    |class    |0      |NC         |NC         |0           |0        |
    +---------+-------+-----------+-----------+------------+---------+
    |method   |0      |NC         |NC         |0           |0        |
    +---------+-------+-----------+-----------+------------+---------+
    |function |8      |NC         |NC         |0.00        |0.00     |
    +---------+-------+-----------+-----------+------------+---------+



    External dependencies
    ---------------------
    ::

        django
          \-contrib
          | \-auth (hackathon.views)
          \-http (hackathon.views)
          \-shortcuts (hackathon.views)
          \-template (hackathon.views)
            \-loader (hackathon.views)
        hackathon
          \-forms (hackathon.views)
          \-scripts
            \-steam (hackathon.views)



    Raw metrics
    -----------

    +----------+-------+------+---------+-----------+
    |type      |number |%     |previous |difference |
    +==========+=======+======+=========+===========+
    |code      |59     |59.00 |NC       |NC         |
    +----------+-------+------+---------+-----------+
    |docstring |1      |1.00  |NC       |NC         |
    +----------+-------+------+---------+-----------+
    |comment   |29     |29.00 |NC       |NC         |
    +----------+-------+------+---------+-----------+
    |empty     |11     |11.00 |NC       |NC         |
    +----------+-------+------+---------+-----------+



    Duplication
    -----------

    +-------------------------+------+---------+-----------+
    |                         |now   |previous |difference |
    +=========================+======+=========+===========+
    |nb duplicated lines      |0     |NC       |NC         |
    +-------------------------+------+---------+-----------+
    |percent duplicated lines |0.000 |NC       |NC         |
    +-------------------------+------+---------+-----------+



    Messages by category
    --------------------

    +-----------+-------+---------+-----------+
    |type       |number |previous |difference |
    +===========+=======+=========+===========+
    |convention |18     |NC       |NC         |
    +-----------+-------+---------+-----------+
    |refactor   |0      |NC       |NC         |
    +-----------+-------+---------+-----------+
    |warning    |7      |NC       |NC         |
    +-----------+-------+---------+-----------+
    |error      |0      |NC       |NC         |
    +-----------+-------+---------+-----------+



    Messages
    --------

    +--------------------+------------+
    |message id          |occurrences |
    +====================+============+
    |missing-docstring   |9           |
    +--------------------+------------+
    |mixed-indentation   |3           |
    +--------------------+------------+
    |bad-whitespace      |3           |
    +--------------------+------------+
    |unused-import       |2           |
    +--------------------+------------+
    |invalid-name        |2           |
    +--------------------+------------+
    |bad-continuation    |2           |
    +--------------------+------------+
    |unused-argument     |1           |
    +--------------------+------------+
    |trailing-whitespace |1           |
    +--------------------+------------+
    |relative-import     |1           |
    +--------------------+------------+
    |line-too-long       |1           |
    +--------------------+------------+



    Global evaluation
    -----------------
    Your code has been rated at 5.28/10

## Contributors

* David Leonard
* Eswari Swarna
* Marco Quezada 
* Wan Kim Mok
