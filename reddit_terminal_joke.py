from reddit_api_helper import RedditAPIHelper


class RedditJokeFetcher(object):
   """Utils to fetch a nice Reddit joke."""

    def __init__(self):
        self.api = RedditAPIHelper()
        self.req_headers = self.api.get_request_headers()

    def get_post_item(self, post, item_id):
        item = post.get('data', {}).get(item_id)
        return item

    def get_post_text(self, post):
        return self.get_post_item(post, 'selftext')
