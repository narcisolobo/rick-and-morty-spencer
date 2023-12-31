import datetime
from os import environ
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    """ This function creates a Flask app and returns it. """

    app = Flask(__name__)
    app.secret_key = environ.get("SECRET_KEY")

    from app.controllers.characters import bp as characters
    app.register_blueprint(characters)

    @app.template_filter("format_date")
    def format_date(val):
        date = datetime.datetime.fromisoformat(val)
        return date.strftime("%b %-d, %Y")

    return app
