from eca import *
from eca.generators import start_offline_tweets

import datetime
import textwrap
import pprint
import re


# This function will be called to set up the HTTP server
def add_request_handlers(httpd):
    # use the library content from the template_static dir instead of our own
    # this is a bit finicky, since execution now depends on a proper working directory.
    httpd.add_content('/lib/', 'application/template/lib')
    httpd.add_content('/style/', 'application/template/style')


@event('init')
def setup(ctx, e):
    # start the offline tweet stream
    start_offline_tweets('data/bata_2014.txt', 'chirp', time_factor=100000)
    ctx.words = {}

# simple word splitter
pattern = re.compile('\W+')

# sample stopword list, needs to be much more sophisticated
stopwords = ['het', 'een', 'aan', 'zijn', 'http', 'www', 'com', 'ben', 'jij']


def words(message):
    result = pattern.split(message)
    result = map(lambda w: w.lower(), result)
    result = filter(lambda w: w not in stopwords, result)
    result = filter(lambda w: len(w) > 2, result)
    return result


@event('chirp')
def tweet(ctx, e):
    # we receive a tweet
    tweet = e.data

    emit('tweets', tweet)

    for w in words(tweet['text']):
        emit('word', {
            'action': 'add',
            'value': (w, 1)
        })