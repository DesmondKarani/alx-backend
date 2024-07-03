#!/usr/bin/env python3
"""Flask App with Babel Translations and URL parameter for locale"""

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


def get_locale():
    """
    Selects the best match for supported languages.

    This function is called by Flask-Babel to determine which language to use
    for the current request. It first checks for a 'locale' parameter in the
    URL. If the parameter is present and valid, it returns that locale. If the
    parameter is not present or not valid, it falls back to using the
    Accept-Language header.

    Returns:
        str: The best match for the supported languages.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    The index view function.

    This function handles requests to the root URL ('/') of the Flask app and
    renders the '4-index.html' template.

    Returns:
    str: The rendered HTML template for the root URL.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
