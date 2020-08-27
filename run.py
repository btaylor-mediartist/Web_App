from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

LISTDB = 'list.db'

def fetchMenu(con):
    films = []
    cur = con.execute('SELECT film FROM films')
    for row in cur:
        films.append(list(row))

    games = []
    cur = con.execute('SELECT game FROM games')
    for row in cur:
        games.append(list(row))

    textbles = []
    cur = con.execute('SELECT textble FROM textbles')
    for row in cur:
        textbles.append(list(row))

    miscs = []
    cur = con.execute('SELECT misc FROM miscs')
    for row in cur:
        miscs.append(list(row))

    return {'films':films, 'games':games, 'textbles':textbles, 'miscs':miscs}

@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/addlist')
def addlist():
    con = sqlite3.connect(LISTDB)
    menu = fetchMenu(con)
    con.close()

    #for input in request.form:
    #    if input == 'film':
    #        details[input] = request.form[input]
            #Me trying to have user input add into the database
            #conn = sqlite3 . connect ('list')
            #cursor = conn.cursor()
            #s_film = input('film:')
            #cursor.execute("""INSERT INTO films (film)) VALUES (?)""", (s_film))
            #conn.commit()
            #print('Data entered successfully.')
            #conn . close()
            #if (conn):
            #    conn.close()
            #    print("\nThe SQLite connection is closed.")

    #    elif request.form[input] and request.form[input] != '0':
    #        items[input] = request.form[input]



    return render_template('addlist.html',
    films=menu['films'],
    games=menu['games'],
    textbles=menu['textbles'],
    miscs=menu['miscs'])

@app.route('/filmlink')
def filmlink():
    con = sqlite3.connect(LISTDB)
    menu = fetchMenu(con)
    con.close()
    return render_template('film.html', films=menu['films'])

@app.route('/gamelink')
def gamelink():
    con = sqlite3.connect(LISTDB)
    menu = fetchMenu(con)
    con.close()
    return render_template('game.html', games=menu['games'])

@app.route('/textlink')
def textlink():
    con = sqlite3.connect(LISTDB)
    menu = fetchMenu(con)
    con.close()
    return render_template('text.html', textbles=menu['textbles'])

@app.route('/misclink')
def misclink():
    con = sqlite3.connect(LISTDB)
    menu = fetchMenu(con)
    con.close()
    return render_template('misc.html', miscs=menu['miscs'])

@app.route('/listed')
def listed():

    print(request.form)
    con = sqlite3.connect(LISTDB)
    menu = fetchMenu(con)
    con.close()

    return render_template(
    'listed.html',
    films=menu['films'],
    games=menu['games'],
    textbles=menu['textbles'],
    miscs=menu['miscs'], items='items')
