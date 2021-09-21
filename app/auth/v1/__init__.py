from flask import Blueprint
from flask_restful import Api,Resource

auth = Blueprint('auth',__name__,url_prefix='/auth')
api = Api(auth,catch_all_404s=True)