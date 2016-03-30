from libs.bottle import route, template, get, post, request, run

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

def check_login(username, password):
    return username == password


@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text">
            Password: <input name="password" type="password">
            <input value="Login" type="submit">
        </form>
    '''


@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@get('/index')
def index():
    return '''
        <form action="/index" method="post">
            Activité: <input name="activite" type="text">
            </br>
            Equipement: <input name="equipement" type="text">
            </br>
            Installation: <input name="installation" type="text">
            <input value="Valider" type="submit">
        </form>
    '''

def check_search(activite, equipement, installation):
    return activite != "" and equipement != "" and installation != ""

@post('/index')
def do_index():
    activite = request.forms.get('activite')
    equipement = request.forms.get('equipement')
    installation = request.forms.get('installation')
    if check_search(activite, equipement, installation):
        return "<p>Vous voulez faire du "+activite+" au "+equipement+" situé vers "+installation+".</p>"
    else:
        return "<p>Il manque des informations.</p>"

run(host='localhost', port=8080)
