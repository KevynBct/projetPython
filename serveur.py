from libs.bottle import route, template, get, post, request, run
import sqlite3



def check_login(username, password):
    return username == password

@get('/')
def login():
    return template('tpl/login')


@post('/')
def do_login():
    if check_login(request.forms.get('username'), request.forms.get('password')):
        #return "<p>Your login information was correct.</p>"
        return index()
    else:
        return "<p>Login failed.</p>"


@get('/index')
def index():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    equipement = []
    for row in cursor.execute("""select nom from equipement group by nom"""):
        equipement.append(row)
    return template('tpl/index', equipement=equipement)

def check_search(activite, equipement, installation):
    return activite != "" and equipement != "" and installation != ""

@post('/index')
def do_index():
    equipement = request.forms.get('equipement')
    activite = request.forms.get('activite')
    installation = request.forms.get('installation')
    if check_search(activite, equipement, installation):
        return template('tpl/result', activite=activite, equipement=equipement, installation=installation)
    else:
        return "<p>Il manque des informations.</p>"

run(host='localhost', port=8080)