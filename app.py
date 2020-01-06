from flask import Flask, request, render_template, redirect, url_for
from goodreads import client
import os

gc = client.GoodreadsClient(os.environ.get('GCLIENT_TOKEN'),os.environ.get('GCLIENT_KEY'))

app = Flask(__name__)

@app.route('/')
def form():
	return render_template('form.html' )


@app.route('/', methods=['POST'])
def form_post():
	try:
		links = get_search_tag()
		links.insert(0,gc.book(query_num))
		return render_template('index.html', len = 7, links=links)
	except:
		return render_template('404.html')

def get_search_tag():
	user_input = request.form['text']
	query_num = int(user_input.strip())
	if search_by_id() == true:
		book_obj = gc.book(query_num)
	else:
		book_obj = gc.book(isbn=query_num)
	print(book_obj)
	links = book_obj.similar_books[:7]
	return links

def search_by_id():
	if request.form['userChoice'] == 'isbn_no':
    		return false
	else:
		return true

	def main():
	app.run()

if __name__=="__main__":
	main()
