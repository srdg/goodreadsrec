from flask import Flask, request, render_template
from goodreads import client

gc = client.GoodreadsClient('ZfHUtSBSMU3ZOTo82zl7wA','OlI30Km37ikK1EIgG7jwWDxeiaAJDX10Fm9zw9XTUA')

app = Flask(__name__)

@app.route('/')
def form():
	return render_template('form.html' )

@app.route('/', methods=['POST'])
def form_post():
	try:
		input = request.form['input']
		isbn_no/book_id= int(text.strip())
		recommendations = gc.book(isbn_no).similar_books[:7]
		recommendations.insert(0,gc.book(book_id))
		print(recommendations)
		return render_template('index.html', len = 7, recommendations=links)
	except:
		return render_template('404.html')
	
if __name__=="__main__":
	app.run()


