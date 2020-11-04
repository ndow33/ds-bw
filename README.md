# Index

- [Tech stack](#tech-stack)
- [Getting started](#getting-started)
- [File structure](#file-structure)
- [More instructions](#more-instructions)
- [Deploying to Heroku](#deploying-to-heroku)

## Tech stack
- [FastAPI](https://fastapi.tiangolo.com/): Web framework. Like Flask, but faster, with automatic interactive docs.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [Heroku](https://devcenter.heroku.com/): Platform as a service, hosts your API.
- [Pipenv](https://pipenv.pypa.io/en/latest/): Reproducible virtual environment, manages dependencies.
- [Pytest](https://docs.pytest.org/en/stable/): Testing framework, runs your unit tests.

## Getting started

[Create a new repository from this template.](https://github.com/Lambda-School-Labs/ds-bw/generate)

Clone the repo
```
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPO-NAME.git

cd YOUR-REPO-NAME
```

Install dependencies
```
pipenv install --dev
```

Activate the virtual environment
```
pipenv shell
```

Launch the app
```
uvicorn app.main:app --reload
```

Go to `localhost:8000` in your browser.

![image](https://user-images.githubusercontent.com/7278219/87965040-c18ba300-ca80-11ea-894f-d51a69d52f8a.png)

You'll see your API documentation:

- Your app's title, "DS API"
- Your description, "Lorem ipsum"
- An endpoint for POST requests, `/predict`
- An endpoint for GET requests, `/vis/{statecode}`

Click the `/predict` endpoint's green button.

![image](https://user-images.githubusercontent.com/7278219/87965845-0532dc80-ca82-11ea-9690-b4c195a648d6.png)

You'll see the endpoint's documentation, including:

- Your function's docstring, """Make random baseline predictions for classification problem."""
- Request body example, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) (like a Python dictionary)
- A button, "Try it out"

Click the "Try it out" button.

![image](https://user-images.githubusercontent.com/7278219/87966677-39f36380-ca83-11ea-97f4-313bc11d3f19.png)

The request body becomes editable. 

Click the "Execute" button. Then scroll down.

![image](https://user-images.githubusercontent.com/7278219/87966896-948cbf80-ca83-11ea-9740-d0801148b1f3.png)

You'll see the server response, including:

- [Code 200](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200), which means the request was successful.
- The response body, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), with random baseline predictions for a classification problem.

## File structure

```
.
└── app
    ├── __init__.py
    ├── main.py
    ├── api
    │   ├── __init__.py
    │   ├── predict.py
    │      
    └── tests
        ├── __init__.py
        ├── test_main.py
        ├── test_predict.py
        
```

## More instructions

Activate the virtual environment
```
pipenv shell
```

Install additional packages
```
pipenv install PYPI-PACKAGE-NAME
```

Launch a Jupyter notebook
```
jupyter notebook
```

Run tests
```
pytest
```

Run linter
```
flake8
```

[calmcode.io videos - flake8](https://calmcode.io/flake8/introduction.html)

## Deploying to Heroku

Prepare Heroku
```
heroku login

heroku create YOUR-APP-NAME-GOES-HERE

heroku git:remote -a YOUR-APP-NAME-GOES-HERE
```

Deploy to Heroku
```
git add --all

git add --force Pipfile.lock

git commit -m "Deploy to Heroku"

git push heroku main:master

heroku open
```

<small>(If you get a `Locking failed!` error when deploying to Heroku or running `pipenv install` then delete `Pipfile.lock` and try again, without `git add --force Pipfile.lock`)</small>

Deactivate the virtual environment
```
exit
```
