from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

LISTDB = 'list.db'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/output')
def output():
    db = sqlite3.connect(LISTDB)
    print(db)

    films = []
    cur = db.execute('SELECT film FROM films')
    for row in cur:
        films.append(list(row))

    games = []
    cur = db.execute('SELECT game FROM games')
    for row in cur:
        games.append(list(row))

    textbles = []
    cur = db.execute('SELECT textble FROM textbles')
    for row in cur:
        texts.append(list(row))

    miscs = []
    cur = db.execute('SELECT misc FROM miscs')
    for row in cur:
        miscs.append(list(row)) 

    db.close()

    return render_template('output.html', films=film, games=game, textbles=textble, miscs=misc)
