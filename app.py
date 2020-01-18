from flask import Flask, request, render_template, redirect, url_for
from goodreads import client
import os

gc = client.GoodreadsClient(os.environ.get('GCLIENT_TOKEN'),os.environ.get('GCLIENT_KEY'))

app = Flask(__name__)

@app.route('/')
def form():
	return render_template('form.html' )

@app.route('/search/ID/<idnum>')
def display_booksById(idnum):
	return render_template('index.html', len = 7, links=links)

@app.route('/search/ISBN/<isbn>')
def display_booksByIsbn(isbn):
	return render_template('index.html', len = 7, links=links)



@app.route('/', methods=['POST'])
def form_post():
	try:
		links,book_obj,query_num = get_search_tag()
		links.insert(0,book_obj)
		if search_by_id() == True:
			return redirect(url_for('display_booksById', idnum=query_num, len=7, links=links))
		else:
			return redirect(url_for('display_booksByIsbn', isbn=query_num, len=7, links=links))
	except KeyError:
		return render_template('notFound.html')
	except IndexError:
		return render_template('indexError.html')
	except:
		return render_template('404.html')

def get_search_tag():
	user_input = request.form['text']
	query_num = user_input.strip()
	if search_by_id() == True:
		book_obj = gc.book(query_num)
	else:
		book_obj = gc.book(isbn=query_num)
	links = book_obj.similar_books[:7]
	return links,book_obj,query_num

def search_by_id():
	if request.form['userChoice'] == 'isbn_no':
    		return False
	else:
    		return True

def main():
	app.run()

if __name__=="__main__":
	main()
