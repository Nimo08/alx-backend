#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    "Flask app config"
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Return 3-index.html"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> str:
    """Determing preferred locale"""
    return 'en'


if __name__ == "__main__":
    app.run(debug=True)
