import unittest
import vcr

from reddit_terminal_joke import RedditTerminalJoke


class RedditAPIHelperTest(unittest.TestCase):

    def test_get_request_headers(self):
        raise NotImplementedError

    def test_get_auth_request_headers(self):
        raise NotImplementedError

    def test_get_reddit_response(self):
        """VCR lets us record and reuse HTTP interactions."""
        with vcr.use_cassette('vcr_cassettes/get_reddit_response.yaml'):
            raise NotImplementedError

class RedditTerminalJokeTest(unittest.TestCase):

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
