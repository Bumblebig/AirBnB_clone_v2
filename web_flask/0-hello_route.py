#!/usr/bin/python3
<<<<<<< HEAD
"""Write a Script that starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
        /: Displays 'Hello HBNB!'
        """
        from flask import Flask

        app = Flask(__name__)


        @app.route("/", strict_slashes=False)
        def hello_hbnb():
                """Displays 'Hello HBNB!'"""
                return "Hello HBNB!"


                if __name__ == "__main__":
                app.run(host="0.0.0.0")
=======
"""
starts Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> a68b7bdc727b7b683fa6b02e552bf0361b53f87c
