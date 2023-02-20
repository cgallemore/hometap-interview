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

## Suggested Next Steps

Based on refining the scope and requirments the items below are suggestions for completing an MVP:

- Authentication: The project doesn't currently have any authentication and I'd recommend adding that.  Assuming we already have an authnetication service, integrating with
  that would be my first option, otherwise there are some options like Basic Auth, OAuth, etc that we would want to look into and make a decision on.
- CORS: A clarifying question I'd have for product on the scope and requirements is if the web app was going to consume the app from the client side and if so, we would need
  to add CORS support to this service.
- Thinking more broadly, do we have other API's that are public facing as well, and if so are we exposing each of these individually?  If so, would a better API Gateway strategy
  make more sense here?  For example, using something like Kong would allow us as a business to have a single API Gateway for all API's we would need to expose publicly.  Additionally
  Kong would also provide additionaly functionally like authentication, CORS, rate limiting, etc that might be desirable for all API's reducing what would need to be implemented in
  each service.
- Monitoring/Alerting: For an MVP I'd want to ensure this service has the proper alerts/monitors configured.  Ideally, this is integrating with existing tools and patterns we already 
  have.  Tools I've used in the past for this are Sentry, DataDog, New Relic, etc.
- Analytics: Open question, are there any type of analytics we want to track and monitor?  If so, would want to be sure to add that as part of the deliverable as well.
- Performance:  
  - Assuming this is just a service to proxy requests to other third party services, I might chose to utilize an async approach with an ASGI web server.  Most python
    frameworks support this already, and given the app would be I/O bound, an asnyc approach makes sense. 
  - Caching: Didn't add any type of caching, but if we understood what type of load to expect, we might want to add that.  This could come later, after an MVP launch, once we better understand the load.
- Rate Limiting: The House Canary API has rate limits, I didn't add any logic to handle that for this exercise, but that's something we would want to think about and make a decision on
  how we handle that.  The simplest case is to just handle the 429 errors from the third party, a more complex solution is to track API calls in the app.  The later would allow us to
  trigger alerts potentially if we are getting close to the limits.
- Swagger Docs:  Didn't add this, but it's nice to have for documenting your API and providing an interface for consumers to reference and test with.
