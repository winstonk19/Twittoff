from .models import user
import numpy as np
from sklearn.linear_model import LogisticRegression
from .twitter import vectorize_tweet

def predict_user(user0_name, user1_name, hypo_tweet_text):

    user0 = User.query.filter(User.username == user0_name)
    user1 = User.query.filter(User.username == user1_name)
    
    vects = no.vstack([user0_vects, user1_vects])

    zeroes = np.zeros(len(user0.tweets))
    ones = np.ones(len(user1.tweets))

    labels = np.concatenate([zeroes, ones])


    log_reg = LogisticRegression()

    log_reg.fit(vects, labels)

    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text)

    prediction = log_reg.predict(hypo_tweet_vect.reshape(1, -1))

    print(pridiction)

