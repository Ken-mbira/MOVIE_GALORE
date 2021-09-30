from flask import Blueprint
from flask_restful import Api,Resource

auth = Blueprint('auth',__name__,url_prefix='/auth')
api = Api(auth,catch_all_404s=True)

from app.auth.v1.view.views import UserView,UserLogin

api.add_resource(UserView,'/controls')
api.add_resource(UserLogin,'/login')