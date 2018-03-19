import unittest
import vcr

from reddit_api_helper import RedditAPIHelper
from reddit_terminal_joke import RedditJokeFetcher


class RedditAPIHelperTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.api = RedditAPIHelper()
        super(RedditAPIHelperTest, self).__init__(*args, **kwargs)

    def test_get_request_headers(self):
        raise NotImplementedError

    def test_get_auth_request_headers(self):
        raise NotImplementedError

    def test_get_reddit_response(self):
        """VCR lets us record and reuse HTTP interactions."""
        with vcr.use_cassette('vcr_cassettes/get_reddit_response.yaml'):
            raise NotImplementedError


class RedditJokeFetcherTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.fetcher = RedditJokeFetcher()
        super(RedditJokeFetcherTest, self).__init__(*args, **kwargs)

    def test_get_jokes_url(self):
        """OMG IS THIS EVEN USEFUL"""
        self.assertEqual(
            self.fetcher._get_jokes_url(), 'http://www.reddit.com/r/Jokes.json')

    def test_get_jokes_url_params(self):
        """mmm does unittest library work? great!"""
        self.assertEqual(
            self.fetcher._get_jokes_url_params(),
            {'sort': 'hot', 'limit': RedditAPIHelper.POST_LIMIT})

    def test_get_post_item(self):
        raise NotImplementedError

    def test_get_jokes_posts(self):
        raise NotImplementedError

    def test_get_joke_candidates(self):
        raise NotImplementedError

    def test_get_cached_jokes(self):
        raise NotImplementedError

    def test_get_jokes_and_fill_cache(self):
        raise NotImplementedError

    def test_get_decent_joke(self):
        raise NotImplementedError


if __name__ == '__main__':
    unittest.main()
