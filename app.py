import media
import fresh_tomatoes
import entertainment_center
import random, threading, webbrowser

from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

# create html content for the home page based on list of movie objects provided
fresh_tomatoes.open_movies_page(entertainment_center.movies)

# default route: Movies Trailer Website home page 
@app.route('/')
def home():
	return render_template('./home.html')

if __name__ == '__main__':
	# create random port above 5000
	port = 5000 + random.randint(0, 999)
	# create url
	url = "http://127.0.0.1:{0}".format(port)
	# open the default web browser
	threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
	# run the server on the randomly generated port
	app.run(port=port, debug=False)
