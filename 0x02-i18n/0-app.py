#!/usr/bin/env python3
"""A flask app set up"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    The index view function.

    This function handles requests to the root URL ('/') of the Flask app and
    renders the '0-index.html' template.

    Returns:
        str: The rendered HTML template for the root URL.
        """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
