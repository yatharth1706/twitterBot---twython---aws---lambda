#!/usr/bin/env python
import random
from twython import Twython
from ssm_secrets import get_secret

# Create the Twython Twitter client using the credentials stored in SSM
twitter = Twython(
    get_secret("CONSUMER_KEY"),
    get_secret("CONSUMER_SECRET"),
    get_secret("ACCESS_TOKEN_KEY"),
    get_secret("ACCESS_TOKEN_SECRET")
)

# Sample random tweets
potential_tweets = [
    'This is my first tweet with Sparrow by @yatharth170699 - http://yatharth1706.github.io/',
    'Wow! Isn\'t Sparrow by @fmc_sea just the coolest! http://yatharth1706.github.io/',
    'Jeez! Everyone should learn about AWS Lambda and Twitter Bots from @yatharth170699'
]


def send_tweet(tweet_text):
    """Sends a tweet to Twitter"""
    twitter.update_status(status=tweet_text)


def handler(event, context):
    """Sends random tweet from list of potential tweets"""
    send_tweet(random.choice(potential_tweets))


def follow_someone(screen_name):
    twitter.create_friendship(screen_name=screen_name)


def follow_fernando():
    follow_someone("fmc_sea")


def like_tweet(tweet_id):
    twitter.create_favorite(id=tweet_id)



