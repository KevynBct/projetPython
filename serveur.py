from libs.bottle import route, template, get, post, request, run, static_file
import sqlite3


<<<<<<< HEAD



def check_login(username, password):
    return username == password

=======
>>>>>>> 79807ac50d61cc49655f20bccceb0c3d862e7bda
@get('/')
def login():
    return template('tpl/login')


@post('/')
def do_login():
    return index()


@get('/index')
def index():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    activite = []
    installation = []
<<<<<<< HEAD
    for row in cursor.execute("""select nom from equipement group by nom"""):
        equipement.append(row)
    for row in cursor.execute("""select nom from activite group by nom"""):
        activite.append(row)
    return template('tpl/index', equipement=equipement, activite=activite, installation=installation)

def check_search(activite, equipement, installation):
    return activite != "" and equipement != "" and installation != ""
=======
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
<<<<<<< HEAD
    if(activte == "" &)
>>>>>>> 1e0edc1fdefee3c02966265610c0156157724397
=======
    requete = ""
    if(activite == "" and installation != ""):
        requete = "select i.adresse, i.ville, e.nom, a.nom from installation i join equipement e on i.numero_instal = e.numero_installation join activite a on a.numero_equipement = e.numero_equipement where LOWER(i.ville) = LOWER(\""+installation+"\")"
    elif(activite != "" and installation == ""):
        requete = "select i.adresse, i.ville, e.nom, a.nom from installation i join equipement e on i.numero_instal = e.numero_installation join activite a on a.numero_equipement = e.numero_equipement where a.nom LIKE \"%"+activite+"%\""
    elif(activite != "" and installation != ""):
        requete = "select i.adresse, i.ville, e.nom, a.nom from installation i join equipement e on i.numero_instal = e.numero_installation join activite a on a.numero_equipement = e.numero_equipement where LOWER(i.ville) = LOWER(\""+installation+"\") and a.nom LIKE \"%"+activite+"%\""
    return requete

>>>>>>> 79807ac50d61cc49655f20bccceb0c3d862e7bda

@post('/index')
def do_index():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    resultat = []
    requete = check_requete(request.forms.get('activite'), request.forms.get('installation'))
    for row in cursor.execute(requete):
        resultat.append(row)
    return template('tpl/result', resultat=resultat)

@route('/static/<filename>', name='static')
def serve_static(filename):
    return static_file(filename, root="static")


run(host='localhost', port=8080)