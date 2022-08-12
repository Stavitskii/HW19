"""
`POST /auth` — получает логин и пароль из Body запроса в виде JSON, далее проверяет соотвествие с данными в БД (есть ли
 такой пользователь, такой ли у него пароль)
и если всё оk — генерит пару access_token и refresh_token и отдает их в виде JSON.

`PUT /auth` — получает refresh_token из Body запроса в виде JSON, далее проверяет refresh_token и если он не истек и
 валиден — генерит пару access_token и refresh_token и отдает их в виде JSON.
"""
from flask import request
from flask_restx import Namespace, Resource

auth_ns = Namespace('auth')

@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get("username")
        password = req_json.get("password")
        if not (username or password):
            return "username and password needed", 400
        # todo generate tokens
        return #tokens

    def put(self):
        req_json = request.json
        ref_token = req_json.get("refresh_token")
        if not ref_token:
            return "refresh_token needed", 400
        # tokens = todo generate tokens
        return  # tokens



