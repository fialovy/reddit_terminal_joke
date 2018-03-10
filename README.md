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
    
    
**Step 4: Make it happen when you open the terminal**    

You can quite literally add `python /path/to/your/reddit_terminal_joke/reddit_terminal_joke.py` to the bottom of your **.bashrc** file, and it will run! :D    




