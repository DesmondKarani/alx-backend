#!/usr/bin/env python3
""" Flask App with Babel Setup"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration class for Flask app.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    The index view function.

    This function handles requests to the root URL ('/') of the Flask app and
    renders the '1-index.html' template.

    Returns:
        str: The rendered HTML template for the root URL.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
