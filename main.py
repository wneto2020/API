from flask import Flask, request

import functionsbd

app = Flask('API')


@app.route('/insert', methods=['POST'])
def insert():

    body = request.get_json()

    if 'nome' not in body:
        return {"ERROR": "NAME NOT INSERT"}

    if 'email' not in body:
        return {"ERROR": "EMAIL NOT INSERT"}

    if 'senha' not in body:
        return {"ERROR": "PASSWORD NOT INSERT"}

    else:
        functionsbd.insert(body['nome'], body['email'], body['senha'])
        return {'STATUS':200, 'INSERT': 'HAS BEEN SUCCESFULLY'}


@app.route('/delete', methods=['POST'])
def delete():
    body = request.get_json()
    if 'nome' not in body:
        return {"ERROR": "NAME NOT INSERT"}

    if 'email' not in body:
        return {"ERROR": "EMAIL NOT INSERT"}

    if 'senha' not in body:
        return {"ERROR": "PASSWORD NOT INSERT"}

    else:
        functionsbd.delete(body['nome'], body['email'], body['senha'])

        return {'STATUS': 200, 'DELETE': 'HAS BEEN SUCCESFULLY'}


@app.route('/update', methods=['POST'])
def update():
    body = request.get_json()

    if 'nome' not in body:
        return {"ERROR": "NAME NOT INSERT"}

    if 'senha' not in body:
        return {"ERROR": "PASSWORD NOT INSERT"}

    if 'nova_senha' not in body:
        return {"ERROR": "NEW PASSWORD NOT INSERT"}

    else:
        functionsbd.update(body['nome'], body['senha'], body['email'],body['nova_senha'])

        return {'STATUS': 200, 'UPADATE': 'HAS BEEN SUCCESFULLY'}

app.run()