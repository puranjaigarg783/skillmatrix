from flask import Blueprint

filtr = Blueprint('filtr',__name__, template_folder= 'templates')
from app.filter import routes