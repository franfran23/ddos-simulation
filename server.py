#!/bin/python3

import time, math, random, threading
from flask import Flask, jsonify


app = Flask(__name__)

MAX_CONCURRENT_REQUEST = 1
sema = threading.Semaphore(MAX_CONCURRENT_REQUEST)


@app.before_request
def simulate_slow_hardware():
	sema.acquire() # aquire slot
	t_end = time.time() + random.uniform(0.05, 0.3) # ~50-300ms window
	while time.time() < t_end:
		# resource intensive task
		math.sqrt(random.random())

@app.after_request
def release_slot(response):
	sema.release()
	return response



@app.route('/')
def index():
	return 'Bienvenue sur mon site !\n<a href="/page2">Aller sur la page n°2</a>'

@app.route('/page2')
def page2():
	return 'Voici la page 2!! <a href="/">retour</a>'

if __name__ == '__main__':
	app.run(debug=True, host="127.0.0.1", port=5000)
