from libs.bottle import route, template, get, post, request, run

def check_login(username, password):
    return username == password


@get('/')
def login():
    return '''
        <body style="text-align : center;  font-family : Noto Sans; background-color : #D3FEE4">
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
        <body style="text-align : center; font-family : Noto Sans; background-color : #D3FEE4">
            <h1> Effectuez votre recherche </h1>
            <form action="/index" method="post">
                <table style="width : 40%; margin-left : 30%">
                    <tr>
                        <td>Activité</td>
                        <td>Equipement</td>
                        <td>Installation</td>
                    </tr>
                    <tr>
                        <td><input name="activite" type="text"></td>
                        <td><input name="equipement" type="text"></td>
                        <td><input name="installation" type="text"></td>
                        <td><input value="Valider" type="submit"></td>
                    </tr>
                </table>
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
        return "<body style=\'text-align : center; font-family : Noto Sans; background-color : #D3FEE4\'><p>Vous voulez faire du "+activite+" au "+equipement+" situé vers "+installation+".</p></body>"
    else:
        return "<p>Il manque des informations.</p>"

run(host='localhost', port=8080)
