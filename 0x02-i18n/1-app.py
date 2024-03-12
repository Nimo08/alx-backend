#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    "Flask app config"
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
babel.init_app(app)


@app.route("/")
def index():
    """Return 1-index.html"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
