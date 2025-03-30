# reddit_terminal_joke
Display a well-upvoted [reddit joke](https://www.reddit.com/r/Jokes/) on your command line.

**Step 0: Clone this repo and make sure you have `uv`**

[uv](https://docs.astral.sh/uv/getting-started/installation/) is a Python package
installer and resolver that isn't...well, a [dumpster fire](https://nielscautaerts.xyz/python-dependency-management-is-a-dumpster-fire.html).


**Step 1: Be able to make reddit API calls**

You have to do a little actual work for this. Tragic, I know.

Nowadays, it's a lot easier to just use [praw](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html) to deal with reddit + Python, but for laziness' sake (after all, it took me
five years to remove the requirements.txt 🙃), we'll stick with `HTTPBasicAuth` since it
still appears to work just fine (on my machine™️).

First, you'll need to obtain a reddit account if you don't have one already, and
create an app from the [reddit apps page](https://www.reddit.com/prefs/apps) to access
your own client ID and client secret. I chose 'script' as the type and a placeholder
`http://localhost:8080` for the redirect URI, since it's required but not needed for our
purposes here.

Next, add a **reddit_credentials.py** file in your reddit_terminal_joke repo.
Obviously, it should be `.gitignore`d - or, better yet, use environment variables or
something and don't even risk it. I recommend following the formatting examples
in [praw.ini](https://praw.readthedocs.io/en/stable/getting_started/configuration/prawini.html#using-interpolation)'s documentation for constructing the user agent string:

```
REDDIT_USER_AGENT = 'script:reddit_terminal_joke:v0.2.0 (by u/YourRedditUsername)'
REDDIT_CLIENT_ID = <your_own_reddit_client_id>
REDDIT_CLIENT_SECRET = <your_own_reddit_client_secret>
REDDIT_UNAME = <throwaway_reddit_account_username>
REDDIT_PW = <throwaway_reddit_account_password>
```


**Step 2: Try it!**
`uv run reddit_terminal_joke.py` from the repo.

Note how this creates a `reddit_joke_cache.json` (or whatever
`RedditJokeFetcher.CACHE_FILENAME` is for you), which is just what it sounds
like. Up to `RedditAPIHelper.POST_LIMIT` decent jokes are initially fetched and
stored there so that we don't need a new HTTP request with every call.
Instead, we pick a random one from the cache if present, refilling it in the
meantime if not (or just empty).



**Step 3: Make it happen when you open the terminal**

Try adding something convoluted like this to your `.bashrc` file if you also want
a `redditjoke` command to use whenever. I am sure there is a better way, but wsl
and I have not been getting along:

```
alias redditjoke='cd ~/reddit_terminal_joke && uv run reddit_terminal_joke.py && cd -'

redditjoke
```

**Step 4: Keep your jokes fresh**

Run `force_refill_joke_cache.py` to obtain more jokes. Better yet, make a cron job for it:

```
@daily uv run /path/to/your/reddit_terminal_joke/force_refill_joke_cache.py
```
