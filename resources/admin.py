from flask_restplus import Resource, Namespace, reqparse, fields
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
    def delete(self, user_id):
        response = user.delete_a_user(user_id=user_id)


user_api.add_resource(Users1, "/users1")
user_api.add_resource(Users2, "/users2/<int:user_id>")
