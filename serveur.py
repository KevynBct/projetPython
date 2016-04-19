from libs.bottle import route, template, get, post, request, run

def check_login(username, password):
    return username == password


@get('/')
def login():
    return '''
        <body style="text-align : center; font : Arial">
            <h1> Bienvenue </h1>
            <form action="" method="post">
                Username: <input name="username" type="text">
                Password: <input name="password" type="password">
                <input value="Login" type="submit">
            </form>
        </body>
    '''


@post('/')
def do_login():
    if check_login(request.forms.get('username'), request.forms.get('password')):
        #return "<p>Your login information was correct.</p>"
        return index()
    else:
        return "<p>Login failed.</p>"


@get('/index')
def index():
    return '''
        <body style="text-align : center; font : Arial">
            <h1> Effectuez votre recherche </h1>
            <form action="/index" method="post">
                Activité: <input name="activite" type="text">
                </br>
                Equipement: <input name="equipement" type="text">
                </br>
                Installation: <input name="installation" type="text">
                <input value="Valider" type="submit">
            </form>
        </body>
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
