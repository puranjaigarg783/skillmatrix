from flask import Blueprint

filtr = Blueprint('filtr',__name__, template_folder= 'templates', static_folder = 'static')
from app.filter import routes