#!/usr/bin/python3
""" This module initializes a Flask application"""

from flask import Flask
from os import getenv
from models import storage
from models.state import State
from api.v1.views import app_views
from api.v1.views import cities
from api.v1.views import states
from api.v1.views import amenities

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.teardown_appcontext
def teardown_app_context(exception):
    """Closes the storage"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
