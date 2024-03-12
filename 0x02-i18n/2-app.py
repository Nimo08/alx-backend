#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
