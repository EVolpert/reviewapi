# Review API
A simple review api done as a exercise for a hiring process

## Requirements
  - Python 3.5.2
  - Postgres 10.3
  - Django 2.0.5
  - Virtualenv 16.0.0
  - djangorestframework 3.8.2
  - psycopg2 2.7.4
  - factory-boy 2.11.1

## Set up
 - Install VirtualEnv with: ```pip install virtualenv```
 - Create a new env with: ```virtualenv -p PYTHON3 <name-of-enviroment>```
 - Activate the script with: ```source path-to-enviroment/bin/activate```
 - Install other requirements with: ```pip install -r requirements.txt```
 - Run to apply the migrations to your database : ```python3 manage.py migrate```
 - Run to create a admin superuser ```python3 manage.py createsuperuser```
 - Run to start the server: ```python3 manage.py runserver```
 - The app will run on http://127.0.0.1:8000/

## Endpoints
### Review APP
- list:
    - url: /reviews/
    - HTTP Verb: GET
    - Function : Get all reviews of the authenticate user
    - Return example:
    ```
    [
      {
          "id": 5,
          "created": "2018-06-26T17:36:04.841775-03:00",
          "rating": "1",
          "title": "\"This is my first review\"",
          "summary": "\"This is the review, a great review, the best of the reviews\"",
          "ip_address": "2804:14d:7889:82dd:f0f6:e362:cad4:fc68",
          "company": 1,
          "reviewer": 4
      }
  ]
  ````

- create:
 url: /reviews/
 HTTP Verb: POST
  Function : Create a new review for a specific company
  Request parameters:
    ```
    {
        "created" = <date time>
        "rating" = <char> choices are 1,2,3,4,5
        "title" = <char> max length 64
        "summary" = <char> max length 10000
        "ip_address" = <char> IPV4 or IPV6
        "company" = <pk for the company>
        "reviewer" = <pk for the user>
    }
    ```
    - Return example:
    ```
    [
      {
          "id": 7,
          "created": "2018-06-27T17:45:39.579779-03:00",
          "rating": "1",
          "title": "a title for the review",
          "summary": "a summary of the experience",
          "ip_address": "127.0.0.1",
          "company": 1,
          "reviewer": 4
      }
    ]
    ````
### Review APP
- create:
  url: /signup/
  HTTP Verb: POST
  Function : Create a new user with a token able to use the api
  Request parameters:
  ```
  {
    "username" = <char>
    "email" = <char email format>
    "first_name" = <char>
    "last_name" = <char>
    "password" = <char>
  }
  ```

### Review APP
- admin:
  url: /admin/
  Function : Access the admin for the project
