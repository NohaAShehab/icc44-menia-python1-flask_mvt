from flask import Flask, render_template
from flask_migrate import Migrate

from app.config import  app_config as AppConfig
from app.models import db
from app.students import student_blueprint
from app.tracks import  track_blueprint


def create_app(config_mode='dev'):
    app = Flask(__name__)
    CurrentConfigClass = AppConfig[config_mode]
    print(CurrentConfigClass)
    # debug? # db_uri
    app.config["SQLALCHEMY_DATABASE_URI"] = CurrentConfigClass.SQLALCHEMY_DATABASE_URI
    app.config.from_object(CurrentConfigClass) # csrf

    db.init_app(app)
    migrate = Migrate(app, db)


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('notfound.html')

    app.register_blueprint(student_blueprint)
    app.register_blueprint(track_blueprint)

    return app