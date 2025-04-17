from flask import Flask, render_template
from .models import DB, user, Tweet

def create_app():

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

DB.init_app(app)

@app.route('/')
def root():
    return render_template('base.html', title='Home')

@app.route('/reset')
def reset():
    DB.drop_all()
    DB.create_all()


    winston = User(id=1, username='winstonk19')

    tweet = Tweet(id=1, text'this is winston\'s tweet', user=winston)
    return 'reset'