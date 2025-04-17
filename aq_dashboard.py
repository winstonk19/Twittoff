'''OpenAQ Air Quality Dashboard with Flask.'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from openaq import OpenAQ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)
api = OpenAQ()


class Record(DB.Model):
    # id column
    id = DB.Column(DB.Integer, primary_key=True)
    # datetime column
    datetime = DB.Column(DB.String(30))
    # value column
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return "Record: {}, {}, {}".format(self.id, self.datetime, self.value)


def get_results():

    status, body = api.measurements(parameter='pm25')
    results = [(item['date']['utc'], item['value'])
               for item in body['results']]
    return results


@app.route('/')
def root():
    '''Base view.'''
    # Query the database for Record objects with value >=10
    records = Record.query.filter(Record.value >= 10).all()

    # Convert the results to a string and return them
    return str(records)


@app.route('/refresh')
def refresh():
    ''' Pull fresh data from Open AQ and replace existing data.'''
    DB.drop_all()
    DB.create_all()
    # get data from OpenAQ, make Record objects with it, and add to db
    for data in get_results():
        record = Record(datetime=data[0], value=data[1])
        DB.session.add(record)
    DB.session.commit()
    return root()
