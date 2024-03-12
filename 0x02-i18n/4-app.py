#!/usr/bin/env python3
"""Force locale with URL parameter"""

from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """Flask app config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Return 4-index.html"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """Determing preferred locale"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
