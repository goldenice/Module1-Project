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
    start_offline_tweets('data/data.txt', 'chirp', time_factor=1000000)
    ctx.words = {}
    temp_file = open("data/words.txt", "r")
    ctx.filter_words = temp_file.readlines()
    temp_file.close()

# simple word splitter
pattern = re.compile('\W+')

# sample stopword list, needs to be much more sophisticated
stopwords = []


def words(message):
    result = pattern.split(message)
    result = map(lambda w: w.lower(), result)
    result = filter(lambda w: w not in stopwords, result)
    result = filter(lambda w: len(w) > 2, result)
    return result

def combine(l):
    s = ""
    for e in l:
        s+=e['text']
    return s

def check_relevance(ctx, tweet, min_score):
        score = 0
        for word in ctx.filter_words:
            if word.replace("\n", "") in tweet["text"].lower():
                if " %s "%(word.replace("\n", "")) in tweet["text"].lower():
                    score += 3
                else:
                    score += 1
        if score >= min_score:
            relevant = True
        else:
            relevant = False
        return relevant

@event('chirp')
def tweet(ctx, e):
    # we receive a tweet
    tweet = e.data
    relevant = check_relevance(ctx, tweet, 3)
    if relevant:
        coordinates = tweet['coordinates']['coordinates']
        tweet['coordinates'] = {}
        tweet['coordinates']['lat'] = coordinates[1]
        tweet['coordinates']['lng'] = coordinates[0]
        emit('tweets', tweet)
