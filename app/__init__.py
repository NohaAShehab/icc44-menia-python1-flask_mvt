from flask import Flask, render_template


def create_app():
    app = Flask(__name__)


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('notfound.html')

    return app