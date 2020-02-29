from flask import Blueprint

pdash = Blueprint('pdash',__name__, template_folder= 'templates')
from app.plogin import routes