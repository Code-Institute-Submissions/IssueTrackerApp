# ISSUE TRACKER
[![Build Status](https://travis-ci.org/tjasajan/IssueTrackerApp.svg?branch=master)](https://travis-ci.org/tjasajan/IssueTrackerApp)

A web application that allows users to post and upvote bugs and new feature proposals.

This is a milestone project for Full Stack Frameworks with Django, part of the Full-Stack Web Developer program @ Code Institute.

## Introduction

A web application that allows users to post and upvote bugs and new feature proposals.

The primary entity in the Issue Tracker is a ticket describing a user’s issue, with ticket status.

Users can create tickets, comment on tickets, upvote bugs and upvote feature requests. 

Upvoting bugs is free. To upvote a feature request, users need to pay some money. 

Payments are processed with Stripe.

This Project is deployed [here](https://django-issue-tracker-app.herokuapp.com/)

Source code is availible on [GitHub](https://github.com/tjasajan/IssueTrackerApp)

## Build with

+ [Python](https://www.python.org/)
+ [Django Framework](https://www.djangoproject.com/)

## Other technologies used

+ Visual Studio Code editor
+ Virtual environment
+ Pylint
+ pip
+ django-forms-bootstrap
+ django-vote
+ AWS
+ Stripe
+ HTML5, CSS3
+ Chrome DevTools

## Installation

1. Download files
2. Install [Python](https://www.python.org/downloads/)
3. Install Django and other requirements
~~~~
pip install -r requirements.txt
~~~~
5. Run application
~~~~
python manage.py runserver
~~~~


## Testing

Testing was done manually throughout development process and with help of a print() function for each new functionality. 

Testing for responsive layout was done in Chrome and also on different devices.  

## Deployment

Output installed packages for dependency management:
~~~~
pip freeze --local > requirements.txt
~~~~

Create Procfile needed for Heroku deployment:
~~~~
echo web: gunicorn IssueTracker.wsgi:application
~~~~

Add to Heroku app repository:
~~~~
heroku git:remote -a django-issue-tracker-app
~~~~

Create AWS account, create bucket with public access, add user and policy.

On Heroku platform add Heroku Postgress Add-on.

Add config vars.




