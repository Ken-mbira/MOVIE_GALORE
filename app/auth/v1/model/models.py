from app import db

class User(db.Model):
    """This will define the behaviours of the user class

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200))
    email= db.Column(db.String(200))
    password = db.Column(db.String)

    def __repr__(self):
        return f'User { self.username }'