#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests


def sort_histogram(histogram={}):
    '''Sorts and prints the given histogram.
    '''
    histogram = list(filter(lambda kv: kv[1], histogram))
    histogram_dict = {}

    histogram.sort(
        key=lambda kv: kv[1],
        reverse=True
    )
    res_str = '\n'.join(list(map(
        lambda kv: '{}: {}'.format(kv[0], kv[1]),
        histogram
    )))
def count_words(subreddit, word_list, histogram=[], n=0, after=None):
    '''Counts the number of times each word in a given wordlist
    occurs in a given subreddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    sort = 'hot'
    limit = 30
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            'https://www.reddit.com',
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )}  
