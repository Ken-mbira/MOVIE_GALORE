from app import db,ma

class Issue(db.Model):
    """This defines all the behaviours of an issue

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'issues'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))


    def read(self):
        return self.title

class IssueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Issue

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
    issue = db.relationship('Issue', backref='user',lazy="dynamic")

    def __repr__(self):
        return self.username 

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User 

class Category(db.Model):
    """This defines all the categories that an issue may fall into

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    issue = db.relationship("Issue",backref="category", lazy="dynamic")

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category