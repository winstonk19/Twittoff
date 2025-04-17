from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy

class user(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    username = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Cplumn(DB.BigInteger)

Class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primaty_key=True, nullable=False)
    text =DB.Column(DB.Unicode(300), nullable=False)
    vect = DB.Column(DB.PicleType, nullable=False)

    user_id = DB.Column(DB.BigIntenger, DB.ForeignKey=True, nullable=False)

    user = DB.relationship('User', backref=DB.backref('tweets'), lazy=True)
