#!/usr/bin/env python3
"""Flask App with get_locale Function"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """
    Selects the best match for supported languages.

    This function is called by Flask-Babel to determine which language to use
    for the current request based on the 'Accept-Language' header.

    Returns:
        str: The best match for the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The index view function.

    This function handles requests to the root URL ('/') of the Flask app and
    renders the '2-index.html' template.

    Returns:
        str: The rendered HTML template for the root URL.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
