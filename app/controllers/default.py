from flask import render_template
from app import app

@app.route('/index/<user>')
@app.route('/', defaults={'user':None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/test', defaults={'user_id':None})
@app.route('/test/<int:user_id>', methods=['GET'])
def test(user_id):
    if user_id:
        return 'Olá, %s!' % user_id
    else:
        return 'Olá, usuário!'