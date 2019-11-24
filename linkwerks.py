#Drew Guyer 2017
#GPL License v3.0

import dataset
import praw
import requests

####################   NOTES #############################
#Maximum of 60 requests per minute as per reddit's terms
"""
Response headers:
    X-Ratelimit-Used: Approximate number of requests used in this period
    X-Ratelimit-Remaining: Approximate number of requests left to use
    X-Ratelimit-Reset: Approximate number of seconds to end of period
"""
# Requests for multiple resources at a time are always better than requests for single-resources in a loop.
###################     #######################  ##################

db = dataset.connect('sqlite:////home/drg/cs/pycode/reddit/linkwerks/linkwerks.db')

def praw_reddit_authorized():
    authorized_instance = praw.Reddit(client_id = 'yXTwupFSkGggig',
                                      client_secret = '4QsXNLGCQ1TLo2cbgJ3akyvKYBw',
                                      password = 'LindaPisLameBoo',
                                      user_agent = 'pythonscript:linkwho.py:v1.0 (by /u/drg_analytics)',
                                      username = 'xxXxxXxxX' )
    return authorized_instance


def praw_reddit_read_only():
    read_only_instance = praw.Reddit(client_id = 'yXTwupFSkGggig',
                                     client_secret = '4QsXNLGCQ1TLo2cbgJ3akyvKYBw',
                                     user_agent = 'pythonscript:linkwho.py:v1.0 (by /u/drg_analytics)' )
    return read_only_instance


def get_hot_ten(connection, subreddit_name):
    """prints the top 10 hotest threads for a given subreddit.

    Args:
        connection = praw Reddit instance (authorized or read only) to reddit
        subreddit_name = the desired subreddit

    """

    for submission in connection.subreddit(subreddit_name).hot(limit=10):
        print(submission.title)

def get_most_linked_url(connection, subreddit_name, time):
    """prints the 'linked-to url' for the top 100 threads for a given subreddit all time.

    Args:
        connection = praw Reddit instance (authorized or read only) to reddit
        subreddit_name = the desired subreddit
        time = for the given time period. Options: 'day', 'month', 'year','all'

    """

    for submission in connection.subreddit(subreddit_name).top(time):
        print(submission.url)

def stalk_a_fool(connection, user):
    """query a user's post history in whatever way you wish

    Args:
        connection = praw Reddit instance (authorized or read only) to reddit
        user = the user you want to 'stalk'

    """

    for submission in connection.redditor(user).top(time):
        print(submission.title)


reddit_connect = praw_reddit_authorized()
get_most_linked_url(reddit_connect, subreddit_name= 'the_donald', time= 'day')
