"""Project manager"""

from flask import Flask
from flask import render_template
from flask import g
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Config file example in GitHub
app.config.from_pyfile('manager.conf')
db = SQLAlchemy(app)

# Import files including pages after app is created
import login
import user

@app.route('/')
def home():
    if g.user:
        return redirect(url_for('user', usr=g.user))
    return render_template('home.html')

@app.route('/help')
def help():
    return render_template('help.html')


if __name__ == '__main__':
    app.run()