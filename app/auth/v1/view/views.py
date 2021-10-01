
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app import db

from app.auth.v1.model.models import User,UserSchema,Category,CategorySchema,Issue,IssueSchema

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

    def get(self):
        args = request.get_json()

        username = args['username']
        email = args['email']
        password = args['password']

        user = User.query.filter_by(email = email).first()
        if user is not None and password == user.password:
            return {
                "message" : f"Welcome back {user.username}"
            }

        return {
            'message' : 'Wrong credentials, please check your email and password and try again'
        }

class IssueView(Resource):
    """This defines the behaviour when an issue is being created

    Args:
        Resource ([type]): [description]
    """

    def get(self):
        "This retrieves all the issues and displays them for a user to see"
        issue = Issue.query.all()
        issue_schema = IssueSchema(many = True)
        output = issue_schema.dump(issue)
        
        return {'Issues':output}

    def post(self):
        """This adds an issue to the database
        """
        args = request.get_json()

        title = args['title']
        body = args['body']
        category_choice = args['category_choice']

        category = Category.query.filter_by(name = category_choice).first()

        issue = Issue(title = title, body = body, category_id = category.id)
        db.session.add(issue)
        db.session.commit()

        issue = Issue.query.all()
        issue_schema = IssueSchema(many = True)
        output = issue_schema.dump(issue)

        return{'Issues':output}

    def delete(self):
        """This will delete the issue"""
        args = request.get_json()

        title = args['title']

        issue = Issue.query.filter_by(title = title).first()
        db.session.delete(issue)
        db.session.commit()
        
        issue = Issue.query.all()
        issue_schema = IssueSchema(many = True)
        output = issue_schema.dump(issue)

        return{'Issues':output}




