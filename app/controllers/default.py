from app import app

@app.route('/index')
@app.route('/')
def index():
    return 'Hello World!'


@app.route('/test', defaults={'user_id':None})
@app.route('/test/<int:user_id>', methods=['GET'])
def test(user_id):
    if user_id:
        return 'Olá, %s!' % user_id
    else:
        return 'Olá, usuário!'