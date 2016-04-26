from libs.bottle import route, template, get, post, request, run



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
    return template('tpl/index', activite='test')

def check_search(activite, equipement, installation):
    return activite != "" and equipement != "" and installation != ""

@post('/index')
def do_index():
    activite = request.forms.get('activite')
    equipement = request.forms.get('equipement')
    installation = request.forms.get('installation')
    if check_search(activite, equipement, installation):
        return template('tpl/result', activite=activite, equipement=equipement, installation=installation)
    else:
        return "<p>Il manque des informations.</p>"

run(host='localhost', port=8080)