# Hometap Interview

## Running Locally

Create a new virtualenv, for example if using virtualenv

    virtualenv ~/.virtualenvs/hometap

Now activate the virtualenv and install the project requirements
    
    . ~/.virtualenvs/hometap/bin/activate
    pip install -r requirements.txt

You can now run the Flask app locally, to do so you can do the following:

    ./run.sh

You should see the app running and can access it on localhost at port 500.  There is a basic healh endpoint you can hit to verify, in your browser go to http://127.0.0.1:5000/api/health
and you should see the following:

```json
{
    "status": "UP",
    "version": "1.0.0"
}
```

## Running tests

This project uses pytest and you can simply run the the tests script like so, which will also show the coverage report:

    ./tests.sh