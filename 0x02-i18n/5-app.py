#!/usr/bin/env python3
"""Flask App with Babel Translations and Mock Login"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    """
    Retrieves the user based on the 'login_as' URL parameter.

    This function checks if there is a 'login_as' parameter in the URL.
    If present,
    it returns the corresponding user from the 'users' dictionary.

    Returns:
        dict: The user dictionary if found, otherwise None.
    """
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """
    Sets the global user before each request.

    This function assigns the user retrieved by `get_user` to
    the global `g.user`
    object before each request.
    """
    g.user = get_user()


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
    renders the '5-index.html' template.

    Returns:
        str: The rendered HTML template for the root URL.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
