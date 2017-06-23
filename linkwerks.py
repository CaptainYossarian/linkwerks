#Drew Guyer 2017
#Program to see what are the most commonly linked to websites

import praw
import requests
import requests.auth

#Maximum of 60 requests per minute as per reddit's terms
"""
Response headers:
    X-Ratelimit-Used: Approximate number of requests used in this period
    X-Ratelimit-Remaining: Approximate number of requests left to use
    X-Ratelimit-Reset: Approximate number of seconds to end of period
"""
# Requests for multiple resources at a time are always better than requests for single-resources in a loop.


def praw_reddit_authorized():
    authorized_connection = praw.Reddit(client_id = 'yXTwupFSkGggig',
                                        client_secret = '4QsXNLGCQ1TLo2cbgJ3akyvKYBw',
                                        password = 'OmputerClaw65',
                                        user_agent = 'pythonscript:linkwho.py:v1.0 (by /u/drg_analytics)',
                                        username = 'drg_analytics' )
    return authorized_connection

def praw_reddit_read_only():
    read_only_connection = praw.Reddit(client_id = 'yXTwupFSkGggig',
                                       client_secret = '4QsXNLGCQ1TLo2cbgJ3akyvKYBw',
                                       user_agent = 'pythonscript:linkwho.py:v1.0 (by /u/drg_analytics)' )
    return read_only_connection

def get_hot_ten(connection, subreddit_name):
    """returns the top 10 hotest threads for a given subreddit.

    Args:
        connection = praw connection (authorized or read only) to reddit
        subreddit_name = the desired subreddit

    """

    for submission in connection.subreddit(subreddit_name).top(limit=10):
        print(submission.title)

#
reddit_connect = praw_reddit_authorized()
#print authorized_connection.user.me()

#read_only_connection = praw_reddit_read_only()
get_hot_ten(reddit_connect, 'all')