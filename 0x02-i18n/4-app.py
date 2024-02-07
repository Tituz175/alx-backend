#!/usr/bin/env python3
"""Flask file"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Configuration object for the babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """Index function documentation"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """if a user is logged in, use the locale from the user settings"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)