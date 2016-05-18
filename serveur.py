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
    activite = []
    installation = []
    for row in cursor.execute("select nom from activite group by nom"):
        if row not in activite:
            activite.append(row)
    for row in cursor.execute("select ville from installation group by nom"):
        if row not in installation:
            installation.append(row)
    activite.sort()
    installation.sort()
    return template('tpl/index', activite=activite, installation=installation)

def check_requete(activite, installation):
    if(activte == "" &)

@post('/index')
def do_index():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    resultat = []
    activite = request.forms.get('activite')
    installation = request.forms.get('installation')
    for row in cursor.execute("select i.adresse, i.ville, e.nom, a.nom from installation i join equipement e on i.numero_instal = e.numero_installation join activite a on a.numero_equipement = e.numero_equipement where LOWER(i.ville) = LOWER(\""+installation+"\") and a.nom LIKE \"%"+activite+"%\""):
        resultat.append(row)
    return template('tpl/result', resultat=resultat)

run(host='localhost', port=8080)