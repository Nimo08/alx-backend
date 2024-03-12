#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def index():
    """Return 3-index.html"""
    return render_template("3-index.html")


@babel.locale_selector
def get_locale():
    """Determing preferred locale"""
    return 'en'


babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(debug=True)
