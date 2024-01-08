#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

""" Create a blueprint for the API """
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *

from api.v1.views.index import *
