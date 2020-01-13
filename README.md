# goodreadsrec

## Project Description :1st_place_medal: 
* A book recommender system using the Goodreads API 

## Contributing Guidelines :tada: 
Read carefully contribution guidelines [CONTRIBUTING.md](CONTRIBUTING.md).

## About This Project :gear:  
* This is a basic web application for a book recommendation system. It uses the [python wrapper](https://github.com/paulshannon/python-goodreads) of the [Goodreads API](https://goodreads.com/api) to show a list of recommended books to the user, given the book ID in goodreads.

### Technologies Used :package: 
* Python
* HTML
* CSS
* Heroku (For Deployment)

## Installation :octocat: 
1. Clone it :busts_in_silhouette:

		`git clone https://github.com/srdg/goodreadsrec.git`

2. cd into goodreadsrec

		`cd goodreadsrec`

3. Requirement

		`pip3 install -r requirements.txt`

4.	Run the code

		`python3 app.py`

### Start Local Server :dancer: 
* Go over to the [Goodreads API](https://goodreads.com/api) and register a dummy application to get your own developer token and key. (You need to create an account first, though.)

* Use the token and the key in `app.py:L5` to connect your goodreads client to the API.Open [Local Server](http://localhost:5000) and you should be able to see the app deployed in your local system.

## Deployment :+1: 
### How to Deploy
* Copy the project seperately
* Go to [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)
* Create an [Heroku account](https://signup.heroku.com/dc)
* Install pipenv

		`pip install --user pipenv`

* Install git ( check git --version)

		`git --version`

* Install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
* Login heroku  

		`heroku login`

* Create a virtual enviroment 

		`python3 -m venv directory_name`

* Create a Procfile
* Create app on Heroku 

		`heroku create`

* Deploy your code  

		`git push heroku master`

### Important note to update the site :v: 
1. change made in the code.
2. git status of project.
3. git add --all.
4. git commit -u "your commit".
5. git remote -v.
6. git push heroku master

### Import Link :100: 
1. https://devcenter.heroku.com/articles/getting-started-with-python#prepare-the-app
2. https://devcenter.heroku.com/articles/django-app-configuration (configure the app).

### Create your requirements.txt file :key: 
		(recipes_dev) $ `pip freeze > requirements.txt`

		(recipes_dev) $ `cat requirements.txt`

* The app is currently deployed on [heroku](http:goodreadsrec.herokuapp.com). Continuous integration is enabled.

## Features :1234: 
TBD

## Help Contributing Guides :crown:

We love to have `articles` and `codes` in different languages and `betterment` of existing ones.

Please discuss it with us first by creating new issue.

:tada: :confetti_ball: :smiley: _**Happy Contributing**_ :smiley: :confetti_ball: :tada:

		 READ instructions before making any pull request 💥 .