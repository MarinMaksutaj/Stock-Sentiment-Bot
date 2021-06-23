import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List
from dotenv import load_dotenv
import os


load_dotenv()
a = os.getenv('a')
b = os.getenv('b')
c = os.getenv('c')
d = os.getenv('d')

auth = tweepy.OAuthHandler(a, b)
auth.set_access_token(c, d)
api = tweepy.API(auth)


def get_tweets(keyword: str, items: int) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode="extended",
                               lang="en", since="2021-06-20").items(items):
        all_tweets.append(tweet.full_text)
    return all_tweets


def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean






