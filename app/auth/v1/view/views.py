
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app import db

from app.auth.v1.model.models import User,UserSchema

parser = RequestParser()
parser.add_argument('username',type=str,required=True,help="Please add your name")
parser.add_argument('email',type=str,required=True,help="Please add your email")
parser.add_argument('email',type=str,required=True,help="Please add your password")

class UserView(Resource):
    """This is the class that defines how the user will be viewed

    Args:
        Resource ([type]): [description]
    """
    def get(self):
        user = User.query.all()
        user_schema = UserSchema(many = True)
        output = user_schema.dump(user)

        return{'user':output}

    def post(self):
        args = parser.parse_args()
        args = request.get_json()

        username = args['username']
        email = args['email']
        password = args['password']

        user = User(username = username,email = email, password = password)
        db.session.add(user)
        db.session.commit()

        user = User.query.all()
        user_schema = UserSchema(many = True)
        output = user_schema.dump(user)

        return{'user':output}