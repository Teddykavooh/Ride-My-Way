from flask_restplus import Resource, Namespace
from app.models import Users

user = Users()
user_api = Namespace("admin")


class Users1 (Resource):
    """Contains GET and POST"""
    def get(self):
        response = user.get_all_users()
        return response


class Users2(Resource):
    """Contains DELETE"""
    def delete(self, username):
        response = user.delete_a_user(username=username)
        return response


user_api.add_resource(Users1, "/all_users")
user_api.add_resource(Users2, "/users/<username>")
