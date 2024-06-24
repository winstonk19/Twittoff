from os import getenv
import tweepy
from .models import DB, user, Tweet

key = getenv('TWITTER_API_KEY')
secret = getenv('TWITER_API_KEY_SECRET')

TWITTER_AUTH = tweepy.0AuthHandler(key, secret)
TWITTER = tweepy.API(TWITTER_AUTH)

def add_or_update_user(username):

    try:
    
    twitter_user = TWITTER.get_user(screen_name=username)

    db_user = (user.query.get(twitter_user.id) or User(id=twitter_user.id, username=username))

    DB.session.add(db_user)

    tweets = twitter_user.timeline(count=200, 
                                   exclude_replies=True, 
                                   include_rts=False, 
                                   tweet_mode='extended'),
                                   since_id=db_user.newest_tweet_id
    

    if tweets:
        db_user.newest_id = tweets[0].id

    for tweet in tweets:
        tweet_vector = vectorize_tweet(tweet.full_text)
        db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300])
        DB.session.add(db.tweet)

    DB.session.commit()

except Exception as e:
    print(f"Error Processing {username}: {e}")
    raise e

else:
    DB.session.commit()

nlp = spacy.load('my_model/')

def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector
     

  