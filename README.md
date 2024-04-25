# A simple guide to run django applications with gunicorn
This is a simple how-to guide on running our django application using gunicorn.

>CAUTION: The explanation in it is based on my understanding of the subject, which could very highly likely be flawed as I speculate a lot and don't validate my hypothesis until it is proven wrong in practise.

## Why
Why even run my application using gunicorn as opposed to via the command `python manage.py runserver` ?
It is because running the above command, in the background, runs serves our APIs via the development server that is pacakged with django. This development server is not intended for concurrent (more than one request at the same time) and high volume requests - a situation that our application will deal with in actual production environment. Hence the packages development server is not fit for production deployment. Gunicorn does that (deploy my django app in prod), more details below:

## What is Gunicorn
Gunicorn is a production grade server that is designed to handle concurrent reqests in high volumns.
It is especially designed to do just that - run my django application on as many worker CPUs as I define in its config and distributes the large volumns of incoming requests across the worker CPUs to be processed.

## How
Step by step guide:
1. install gunicorn in your django project, `pip install gunicorn`
2. create a config file for gunicorn called `gunicorn.config.py` 
    1. populate some init configs in the file:
```
bind = "0.0.0.0:8001" # Adjust host and port as needed
workers = 2 # Adjust workers (dedicated CPUs) as needed   
```
     2. It is noteworthy that the gunicorn config file is a python file which isn't usually the case in other application configs.
3. run the application using gunicorn with the command `gunicorn main_app.wsgi:application`
        1. It is noteworthy that we are using python's dot notation to specify the django application path here, `main_app` refers to the main dajngo application that is found in any django project and contains the `wsgi.py` file along with the root `urls.py` and `views.py` files, `settings.py` file plus a few others.
4. Gunicorn should now be running the django project/application at the specified host and on the specified number of workers. 

## How to run this project:
1. Install the depedencies: `pip install -r requirements.txt`
2. create the `.env` file with the following config data:
```
bind = "0.0.0.0:8000"  # Adjust host and port as needed
workers = 3 # Adjust workers (dedicated CPUs) as needed
```
3. Run the application: `gunicorn gunicorn_poc.wsgi:application`

## Issues and contributions
If you encounter any issue then please raise and issue on Github. Please create PRs for Contributions.
