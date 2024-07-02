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
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    g.user = get_user()


def get_locale():
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
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
