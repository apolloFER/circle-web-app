# Circle Validator

[![Build Status](https://travis-ci.org/apolloFER/circle-web-app.svg?branch=master)](https://travis-ci.org/apolloFER/circle-web-app)
[![Demo](https://img.shields.io/badge/demo-online-green.svg)](https://circle-validate.ronic.co)
[![Docker](https://img.shields.io/docker/pulls/darkoronic/circle-validator.svg)](https://hub.docker.com/r/darkoronic/circle-validator/)
> Simple Django project that draws a circle and then validates if the user clicks inside.

Circle Validator is a Django app with HTML5 canvas frontend.

It draws a circle on the HTML5 canvas an then validates each user click. If a click is inside the circle, it is marked green. Otherwise it is marked red.
There is an API that can be used with JSON POST requests. JSON schema can be found in the lower sections of this README file.

It's compatible with Python 2.7, 3.4, 3.5 and 3.6.

![Screenshot](https://user-images.githubusercontent.com/6859904/30520109-b4e6e77e-9ba6-11e7-8740-d2b0aba83bc7.png)

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Tests](#tests)
- [Deployment](#deployment)
- [License](#license)

## Demo

There's a fully working demo at https://circle-validate.ronic.co

## Features

The backend is written using latest version of Django framework - 1.11. The frontend is a HTML5 canvas with vanilla Javascript.

There is an API that can be accessed via ```api/in_circle``` URL. The API accepts raw JSON in the body of a POST request. JSON format is strictly tested and validated on the backend. The correct JSON schema for the request is:

```json
{
  "type": "object",
  "required": [
    "point",
    "circle"
  ],
  "properties": {
    "point": {
      "type": "object",
      "required": [
        "x",
        "y"
      ],
      "properties": {
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "circle": {
      "type": "object",
      "required": [
        "x",
        "y",
        "radius"
      ],
      "properties": {
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        },
        "radius": {
          "type": "number"
        }
      }
    }
  }
}
```

The API will return a JSON response that conforms to the following schema:

```json
{
  "type": "object",
  "required": [
    "point",
    "inside"
  ],
  "properties": {
    "point": {
      "type": "object",
      "required": [
        "x",
        "y"
      ],
      "properties": {
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "inside": {
      "type": "boolean"
    }
  }
}
```

On the ```beanstalk``` branch is a AWS Elastic Beanstalk compatible version (more on Deployment section). Demo is run on AWS Elastic Beanstalk.

Circle Validator is Docker compatible. A public Docker image can be found at https://hub.docker.com/r/darkoronic/circle-validator/ There is also Docker Compose compatibility for launching both the app and the tests. (more on Usage section).

## Setup

Circle Validator is compatible with Python 2.7, 3.4, 3.5, 3.6. It is tested on Linux and is OSX compatible. Windows compatibility is not tested.

It's advisable to use virtualenv.

Requirements for running the app are in the ```requirements.txt``` file. Install them (in a virtualenv) using

```pip install -r requirements.txt```

There is a separate ```requirements-test.txt``` file with requirements for running the tests. Cricle Validator uses pytest and pytest-django for testing. More in the Tests section.

Docker and Docker Compose are probably the easiest ways of using Circle Validator. Make sure you have both of them installed on your machine.

## Usage

There are three ways of running Circle Validator.

### Using virtualenv

Navigate to the folder where Circle Validator is located and activate the virtualenv in which you installed the dependencies. Run it using

```python manage.py runserver```

### Using Docker

You can either pull the public Docker repo using

```docker pull darkoronic/circle-validator```

or navigate to the folder where Circle Validator is located and build it using

```docker build -t circle-validator .```

Depending on which one you are using the image name will differ.

Run it using

```docker run -p 8000:8000 darkoronic/circle-validator```

Replace ```darkoronic/circle-validator``` with ```circle-validator``` in case you built it yourself.

### Using Docker Compose

The easiest way to run Circle Validator is with Docker Compose.

Navigate to the folder where Circle Validator is located and run

```docker-compose up web```

### Accessing the app

After running it (with one of the 3 methods explained above) you can access the app in your browser by pointing your browser to http://127.0.0.1:8000/

## Tests

Tests for Circle Validator are written using the awesome PyTest library. You should first install the test dependencies in your virtualenv using

```pip install -r requirements-test.txt```

Navigate to the folder where Circle Validator is located and run ```pytest```.

### Using Docker Compose

There's an easier way to run tests using Docker Compose. As you did for running the app, navigate to the folder and then run

```docker-compose up test```

This will run the tests in Docker. Just make sure to rebuild it with ```docker-compose build tests``` if you change something.

### Travis

Circle Validator is tested Using Travis-CI - https://travis-ci.org/apolloFER/circle-web-app

## Deployment

Current Docker images are good only for testing and development since they rely on Django's runserver command which is not intended for production environments.

In the ```beanstalk``` branch you can find an AWS Elastic Beanstalk compatible version with all needed configuration for running it. The folder containing Circle Validator is compressed to a Zip archive and uploaded to AWS Console in a Elastic Beanstalk Python environment (AWS only supports Python 2.7 and Python 3.4).

Current demo is run on AWS Elastic Beanstalk.

## License

[GPL © Darko Ronić.](LICENSE)
