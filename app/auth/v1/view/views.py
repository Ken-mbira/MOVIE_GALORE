
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app import db

from app.auth.v1.model.models import Genre, User,UserSchema

parser = RequestParser()
parser.add_argument('username',type=str,required=True,help="Please add your name")
parser.add_argument('email',type=str,required=True,help="Please add your email")
parser.add_argument('password',type=str,required=True,help="Please add your password")

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
        # args = parser.parse_args()
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

    def delete(self):
        args = parser.parse_args()
        args = request.get_json()

        username = args['username']
        email = args['email']
        password = args['password']

        User.query.filter_by(email = email).delete()
        db.session.commit()
        
        return {
            'message' : f'User {username} was deleted '
        }

class UserLogin(Resource):
    """This defines the behaviours when a user is login in

    Args:
        Resource ([type]): [description]
    """

    def post(self):
        args = parser.parse_args()
        args = request.get_json()

        username = args['username']
        email = args['email']
        password = args['password']

        user = User.query.filter_by(email = email).first()
        if user is not None and password == user.password:
            return {
                "message" : f"Welcome back {username}"
            }

        return {
            'message' : 'Wrong credentials, please check your email and password and try again'
        }

class UserPreference(Resource):
    """This is where a user can set his/her best genres

    Args:
        Resource ([type]): [description]
    """
    def put(self):
        args = request.get_json()

        username = args['username']
        genre = args['genre']

        user = User.query.filter_by(username = username).first()
        preference = Genre.query.filter_by( name = genre ).first()

        preference.preference.append(user)
        db.session.commit()

        return {
            preference.id : user.id
        }
