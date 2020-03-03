from flask import Blueprint

authn = Blueprint('authn',__name__, template_folder= 'templates')
from app.auth import routes