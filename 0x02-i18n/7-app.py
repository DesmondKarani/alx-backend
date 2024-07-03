#!/usr/bin/env python3
"""Flask App with Babel Translations, User Locale Preference, and Timezone"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

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

    This function assigns the user retrieved by `get_user`
    to the global `g.user`
    object before each request.
    """
    g.user = get_user()


def get_locale():
    """
    Selects the best match for supported languages.

    This function is called by Flask-Babel to determine which language to use
    for the current request. It checks in the following order:
    1. Locale from URL parameters.
    2. Locale from user settings.
    3. Locale from request header.
    4. Default locale.

    Returns:
        str: The best match for the supported languages.
    """
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    header_locale = (
            request.accept_languages.best_match(app.config['LANGUAGES'])
            )
    if header_locale:
        return header_locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_timezone():
    """
    Retrieves the timezone based on URL parameter, user settings, or default.

    This function checks in the following order:
    1. Timezone from URL parameters.
    2. Timezone from user settings.
    3. Default to UTC timezone.

    Returns:
        tzinfo: A pytz timezone object.
    """
    try:
        # 1. Find timezone parameter in URL parameters
        timezone = request.args.get('timezone')
        if timezone:
            return pytz.timezone(timezone)

        # 2. Find time zone from user settings
        if g.user and g.user['timezone']:
            return pytz.timezone(g.user['timezone'])

        # 3. Default to UTC
        return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])
    except pytz.exceptions.UnknownTimeZoneError:
        return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index():
    """
    The index view function.

    This function handles requests to the root URL ('/') of the Flask app and
    renders the '7-index.html' template.

    Returns:
        str: The rendered HTML template for the root URL.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
