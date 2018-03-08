import json
import reddit_credentials as creds
import requests

from requests.auth import HTTPBasicAuth


class RedditAPIHelper(object):

    def get_request_headers(self):
        """Just get a simple header for reddit requests
        """
        return {"User-Agent": creds.REDDIT_USER_AGENT}

    def get_auth_request_headers(self):
        """Do specialness to get a reddit access token for *authorized*
        request headers.
        """
        client_auth = HTTPBasicAuth(creds.REDDIT_CLIENT_ID,
                                    creds.REDDIT_CLIENT_SECRET)
        token_post_data = {
            "grant_type": "password",
            "username": creds.REDDIT_UNAME,
            "password": creds.REDDIT_PW
        }
        token_headers = {"User-Agent": creds.REDDIT_USER_AGENT}

        token_resp = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=client_auth, data=token_post_data,
            headers=token_headers
        )
        reddit_access_token = json.loads(
            token_resp.content).get('access_token', '')

        return {"Authorization": "bearer %s" % reddit_access_token,
                "User-Agent": creds.REDDIT_USER_AGENT}

    def get_reddit_response(self, url, headers={}, params={}):
        resp = requests.get(url, params=params, headers=headers)
        if resp.status_code != 200:
            return
        return json.loads(resp.content)

    # PROBABLY IN TEH NEXT CLASS
    #def __init__(self):
    #    self.api = RedditAPIHelper()
    #    self.req_headers = self.api.get_request_headers()

    #def get_post_item(self, post, item_id):
    #    item = post.get('data', {}).get(item_id)
    #    return item

    #def get_post_text(self, post):
    #    return self.get_post_item(post, 'selftext')
