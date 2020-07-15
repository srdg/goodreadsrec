# goodreadsrec

## Project Description
* A book recommender system using the Goodreads API 

## Contributing Guidelines 
Please read the contribution guidelines carefully at [CONTRIBUTING.md](CONTRIBUTING.md).

## About This Project 
* This is a basic web application for a book recommendation system. It uses the [python wrapper](https://github.com/paulshannon/python-goodreads) of the [Goodreads API](https://goodreads.com/api) to show a list of recommended books to the user, given the book ID in goodreads.

## Installation 
```
git clone https://github.com/srdg/goodreadsrec.git
cd goodreadsrec
pip3 install -r requirements.txt
python3 app.py
```
### Start Local Server 
* Go over to the [Goodreads API](https://goodreads.com/api) and register a dummy application to get your own developer token and key. (You need to create an account first, though.)

* Use the token and the key in [`app.py:L5`](https://github.com/srdg/goodreadsrec/blob/master/app.py#L5) to connect your goodreads client to the API. Alternatively, to set the token/key via command line - 
#### Linux
```
export GCLIENT_TOKEN="your-goodreads-token-here"  
export GCLIENT_KEY="your-goodreads-key-here"
```
#### Windows
```
setx GCLIENT_TOKEN "your-goodreads-token-here"   
setx GCLIENT_KEY="your-goodreads-key-here"
```

Open [localhost on port 5000](http://localhost:5000) and you should be able to see the app deployed in your local system.

## Live Demo

* The app is currently deployed on [heroku](http:goodreadsrec.herokuapp.com). Continuous integration is enabled.

