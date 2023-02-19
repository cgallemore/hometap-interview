# Hometap Interview

## Running Locally

Create a new virtualenv, for example if using virtualenv

    virtualenv ~/.virtualenvs/hometap

Now activate the virtualenv and install the project requirements
    
    . ~/.virtualenvs/hometap/bin/activate
    pip install -r requirements.txt

You can now run the Flask app locally, to do so you can do the following:

    ./run.sh

There is a basic healh endpoint you can hit to verify, in your browser go to http://127.0.0.1:5000/api/health and you should see the following:

```json
{
    "status": "UP",
    "version": "1.0.0"
}
```

The property details endpoint is at http://127.0.0.1:5000/api/property/details.  The endpoint has two required paramters:

    address: The street address for the property
    zipcode: The zipcode for the property

Currently the API will return a 400 with an error message if both of those are not
present.  An example, with the params is http://127.0.0.1:5000/api/property/details?address=100%20Main%20St&zipcode=55555

## Running tests

This project uses pytest and you can simply run the the tests script like so, which will also show the coverage report:

    ./tests.sh

## Project Structure

    ```
    - README.md
    - requirements.txt: All requirements for running the app and running tests
    - run.sh: Script to run the flask app for local development and debugging
    - tests.sh: Script to run tests and print coverage report
    - hometap_interview: Root python module for the app
        - app.py: Flask app setup and configuration
        - config.py: Flask configurations
        - exceptions.py: Custom exceptions for the app
        - version.py: Maintains the version of the app
        - clients: module to organize all third party clients
            - house_canary.py: The API client for interfacing with the HouseCanary API
        - views: module to organize all the Flask views/routes
            - health.py: Route for a basic health check
            - property_details: Routes for retrieving property details information
        tests: All pytest tests are organized here
            - conftest.py: pytest configureation and fixtures
            - test_clietns.py: All tests for testing the hometap_interview/clients module
            - test_views.py: All tests for testing the hometap_interview/views module
    ```

## Implmentation Details

- Flask is the webframework used, written with Python 3.10.x
- Pytest and pytest-cov for unit tests and coverage
- Used Beeceptor to mock out the property details endpoint for the House Canary API.  It matches on the path starting with /property/details
  and will return the same JSON data as described in the HouseCanary API.  The root url is `https://cgallemore.free.beeceptor.com`.  When running
  the app locally, the DevConfig updates the `HOUSE_CANARY_URL` with this mock endpoint.
