import json
import os

from random import randint

from reddit_api_helper import RedditAPIHelper


class RedditJokeFetcher(object):

    REQUIRED_UPVOTES = 100  # Be pickier if you want.
    CACHE_FILENAME = 'reddit_joke_cache.json'

    def __init__(self):
        """Instantiate our little friend to make all the HTTP requests."""
        self.api = RedditAPIHelper()

    def _get_jokes_url(self):
        return 'http://www.reddit.com/r/Jokes.json',

    def _get_jokes_url_params(self):
        return {'sort': 'hot', 'limit': self.api.POST_LIMIT},

    def _get_cache_path(self):
        """Return le fancy path to joke cache for file open shenanigans"""
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        return os.path.join(__location__, self.CACHE_FILENAME)

    def _get_post_item(self, post, item_id):
        """dict diggity diggin'"""
        return post.get('data', {}).get(item_id)

    def _get_jokes_posts(self):
        jokes_data = self.api.get_reddit_response(
            'http://www.reddit.com/r/Jokes.json',
            params={'sort': 'hot', 'limit': self.api.POST_LIMIT},
            headers=self.api.get_request_headers()
        )
        jokes_posts = (jokes_data.get('data') or {}).get('children')

        return jokes_posts

    def _get_joke_candidates(self):
        """Get a stash of hopefully decent jokes.

        We want hot things that are NOT stickied (that announcement stuff
        that stays on the front page), that actually have titles, actually
        have text, and have a reasonable number of upvotes.
        """
        candidates = self._get_jokes_posts()
        candidates = [
            post for post in candidates
                if not self._get_post_item(post, 'stickied')
                and self._get_post_item(post, 'title')
                and self._get_post_item(post, 'selftext')
                and self._get_post_item(post, 'ups') >= self.REQUIRED_UPVOTES
        ]
        # I am genuinely sorry for how ugly this is...
        candidates = [
            {'title': post['data']['title'], 'text': post['data']['selftext']}
                for post in candidates
        ]
        return candidates

    def _get_cached_jokes(self):
        """Return jokes from cache if they exist there; None otherwise."""
        try:
            with open(self._get_cache_path(), 'r') as cache_file:
                jokes = json.loads(cache_file.read())
        except IOError:  # file no exist?
            return None
        except ValueError:  # mmm...l'empty?
            return None

        return jokes

    def _get_jokes_and_fill_cache(self):
        """Get fresh jokes from Reddit, write to cache while at it, and return them."""
        candidates = self._get_joke_candidates()
        with open(self._get_cache_path(), 'w') as cache_file:
            json.dump(candidates, cache_file)

        return candidates

    def get_decent_joke(self):
        """Get cached joke, or refill cache and use one from that process."""
        jokes = self._get_cached_jokes()
        if not jokes:
            jokes = self._get_jokes_and_fill_cache()

        # Let's try to change things up..
        return jokes[randint(0, len(jokes) - 1)]


def main():
    fetcher = RedditJokeFetcher()
    joke = fetcher.get_decent_joke()
    print('{}\n\n{}\n'.format(
        joke['title'].encode('utf-8'), joke['text'].encode('utf-8')))


if __name__ == '__main__':
    main()
