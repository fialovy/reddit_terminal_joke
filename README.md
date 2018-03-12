# reddit_terminal_joke
Display a well-upvoted reddit joke upon opening your terminal. Because you use a terminal, right? Good!    

But **how**, you ask?    
    
    
**Step 0: Be worthy**

Be a cool person who regularly needs a terminal because vim or emacs and not some schmancy IDE.
    
    
**Step 1: Clone this repo**

Put it somewhere nice. Put it in a happy, warm place on your machine.
    
    
**Step 2: Be able to make reddit API calls**

You have to do a little actual work for this. Tragic, I know.

You need to put a **reddit_credentials.py** file in your reddit_terminal_joke repo so that the code can access teh important magical things. It should look like this:

```
REDDIT_USER_AGENT = 'Python script to get a well-upvoted reddit joke - or technically whatever string you want'            
REDDIT_CLIENT_ID = <your_own_reddit_client_id>                                             
REDDIT_CLIENT_SECRET = <your_own_reddit_client_secret>                            
REDDIT_UNAME = <throwaway_reddit_account_username>                                            
REDDIT_PW = <throwaway_reddit_account_password>
```

[This](https://github.com/reddit-archive/reddit/wiki/OAuth2) mentions how to get a reddit client ID and client secret. More effort...sue me.    

**Step 3: Try it!**    
`python reddit_terminal_joke.py` from the repo. Hurrah!   

Note how this creates a `reddit_joke_cache.json` (or whatever
`RedditJokeFetcher.CACHE_FILENAME` is for you), which is just what it sounds
like. Up to `RedditAPIHelper.POST_LIMIT` decent jokes are initially fetched and
stored there so that we don't need a new HTTP request with every damn call.
Instead, we pick a random one from the cache if present, refilling it in the
meantime if not (or just empty).    

    
    
**Step 4: Make it happen when you open the terminal**    

You can quite literally add `python /path/to/your/reddit_terminal_joke/reddit_terminal_joke.py` to the bottom of your **.bashrc** file, and it will run! :D    

**Step 5: Keep your jokes fresh**    

Run `python /path/to/your/reddit_terminal_joke/force_refill_joke_cache.py` to
get moar tasty jokes from reddit. Better yet, make a cron job for it:

```
@daily python /path/to/your/reddit_terminal_joke/force_refill_joke_cache.py
```

cron jobs are absolutely amazing fun and should be abused by all.

**Step 6: bother me until I actually provide tests**

I love testing, so there is no excuse.



