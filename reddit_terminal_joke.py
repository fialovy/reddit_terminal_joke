from reddit_api_helper import RedditAPIHelper


class RedditJokeFetcher(object):

    REQUIRED_UPVOTES = 500

    def __init__(self):
        self.api = RedditAPIHelper()
        self.req_headers = self.api.get_request_headers()

    def get_post_item(self, post, item_id):
        item = post.get('data', {}).get(item_id)
        return item

    def get_post_text(self, post):
        return self.get_post_item(post, 'selftext')

def main():
    fetcher = RedditJokeFetcher()
    jokes_data = fetcher.api.get_reddit_response(
        'http://www.reddit.com/r/Jokes.json',
        params={'sort': 'hot', 'limit': fetcher.api.POST_LIMIT},
        headers=fetcher.api.get_request_headers())
    jokes_posts = (jokes_data.get('data') or {}).get('children')

    for post in jokes_posts:
        data = post.get('data', {})
        title = data.get('title')
        text = data.get('selftext')
        upvotes = data.get('ups')  # At least I think, anyway
        if title and text and upvotes >= fetcher.REQUIRED_UPVOTES:
            print('\n{}\n\n{}'.format(title, text))
            return

if __name__ == '__main__':
    main()
