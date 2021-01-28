streamfield-stress-test
=======================

An example project for testing complex streamfields against the new Telepath form rendering code

## Installation

To test the old and new code side by side, it makes sense to set up two virtualenvs to swap between. In the 'old' virtualenv:

    pip install wagtail==2.12rc1
    
In new virtualenv, check out the `feature/streamfield` branch of the wagtail git repo and build / install with:

    nvm use
    npm install --no-save
    npm run build
    pip install -e .

From the root of the streamfield-stress-test project:

    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py load_initial_data
    ./manage.py create_stream_page
    ./manage.py runserver

`create_stream_page` can be repeated as many times as desired to create multiple test pages.
