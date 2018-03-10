from reddit_api_helper import RedditAPIHelper


class RedditJokeFetcher(object):

    REQUIRED_UPVOTES = 500

    def __init__(self):
        self.api = RedditAPIHelper()

    def _get_post_item(self, post, item_id):
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
        # Attempt to trim off announcements or whatnot that are automatically
        # at the top. Hopefully no more than 3 of those buggers.
        import pdb; pdb.set_trace()     
        candidates = candidates[3:]

        for post in candidates:
            # It's more clear than a list comprehension, okay? Sue me.
            title = self._get_post_item('title')
            text = self._get_post_item('selftext')
            upvotes = self._get_post_item('ups')  # At least I think, anyway

            if title and text and upvotes >= self.REQUIRED_UPVOTES:
                return (title, text)


def main():
    fetcher = RedditJokeFetcher()
    candidates = fetcher.get_jokes_posts()
    joke = fetcher.get_decent_joke(candidates)
    print joke


if __name__ == '__main__':
    main()
