

from flask.blueprints import Blueprint
track_blueprint = Blueprint('tracks', __name__, url_prefix='/tracks')
from app.tracks import views

