from flask_restful import Resource

from app.auth.v1.model.models import User,UserSchema

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

