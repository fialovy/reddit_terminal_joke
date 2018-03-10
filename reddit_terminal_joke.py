from random import randint

from reddit_api_helper import RedditAPIHelper


class RedditJokeFetcher(object):

    REQUIRED_UPVOTES = 100  # Be pickier if you want.

    def __init__(self):
        """Instantiate our little friend to make all the HTTP requests."""
        self.api = RedditAPIHelper()

    def _get_post_item(self, post, item_id):
        """dict diggity diggin'"""
        return post.get('data', {}).get(item_id)

    def get_jokes_posts(self):
        jokes_data = self.api.get_reddit_response(
            'http://www.reddit.com/r/Jokes.json',
            params={'sort': 'hot', 'limit': self.api.POST_LIMIT},
            headers=self.api.get_request_headers()
        )
        jokes_posts = (jokes_data.get('data') or {}).get('children')

        return jokes_posts

    def get_decent_joke(self, candidates):
        """Get a hopefully decent joke from a list of candidate posts.

        We want something hot that is NOT stickied (that announcement stuff
        that stays on the front page), that actually has a title, actually
        has text, and has a reasonable number of upvotes.
        """
        candidates = [
            post for post in candidates
                if not self._get_post_item(post, 'stickied')
                and self._get_post_item(post, 'title')
                and self._get_post_item(post, 'selftext')
                and self._get_post_item(post, 'ups') >= self.REQUIRED_UPVOTES
        ]
        # Let's try to change things up..
        decent = candidates[randint(0, len(candidates) - 1)]

        return (decent['data']['title'], decent['data']['selftext'])


def main():
    fetcher = RedditJokeFetcher()
    candidates = fetcher.get_jokes_posts()
    title, joketext = fetcher.get_decent_joke(candidates)
    print('{}\n\n{}\n'.format(title.encode('utf-8'), joketext.encode('utf-8')))


if __name__ == '__main__':
    main()
