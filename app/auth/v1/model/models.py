from app import db,ma

preferences = db.Table('preferences',
    db.Column('user.id', db.Integer,db.ForeignKey('users.id')),
    db.Column('genre_id', db.Integer,db.ForeignKey('genres.id'))
)

class Genre(db.Model):
    """This will define all the preferences available for a user to choose from

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'genres'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),unique = True,index = True)

    def __repr__(self):
        return self.name

class User(db.Model):
    """This will define the behaviours of the user class

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200))
    email= db.Column(db.String(200),unique = True,index = True)
    password = db.Column(db.String)
    preference = db.relationship('Genre', secondary=preferences, backref=db.backref('preference', lazy = 'dynamic'))

    def __repr__(self):
        return self.username 

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User 