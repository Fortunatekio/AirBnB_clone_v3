#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
from api.v1.views.index import *
from models.state import State
from models.place import *
from models.review import *
from models.city import *
from models.amenity import *
from models.user import *

""" Create a blueprint for the API """
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
