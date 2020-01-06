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
		user_input = request.form['text']
		query_num = int(user_input.strip())
		if request.form.get('userChoice') == 'isbn_no':
    			book_obj = gc.book(isbn=query_num)
		else:
    			book_obj = gc.book(query_num)
		book_obj = book_obj.similar_books[:7]
		book_obj.insert(0,gc.book(query_num))
		print(book_obj)
		return render_template('index.html', len = 7, links=links)
	except:
		return render_template('404.html')

def main():
	app.run(debug=True)

if __name__=="__main__":
	main()
