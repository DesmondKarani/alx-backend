#!/usr/bin/env python3
"""Flask App with Babel Translations and URL parameter for locale"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    # Check if there's a locale parameter in the URL
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # If not, resort to the previous default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
