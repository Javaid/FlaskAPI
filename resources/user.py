from gettext import gettext

from flask_restful import Resource

from flask import request


class User(Resource):
    @classmethod
    def get(cls):
        return {"message": gettext("Welcome User")}, 200

    @classmethod
    def post(cls):
        user_json = request.get_json()
        # user_data = user_schema.load(user_json)
        return  user_json['email']
