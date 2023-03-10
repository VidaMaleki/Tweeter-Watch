
import snscrape.modules.twitter as sntwitter
from datetime import datetime
import json
import pandas as pd


tracked_accounts = ["@alikarimi_ak8", "@elonmusk", "@BarackObama"]
query = "(from:BarackObama)"


# Helper function to use for 

tweets = []
limit = 1
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append({ "tweet": tweet
                    # 'id': tweet.id,
                    # 'content': tweet.rawContent,
                    # 'date': tweet.date,
                    # 'username': tweet.user.username,
                    # 'url': tweet.url,
                    # 'replyCount': tweet.replyCount,
                    # 'retweetCount': tweet.retweetCount,
                    # 'likeCount': tweet.likeCount
                }
        )
# df = pd.DataFrame(tweets, columns=["id","content","date", "username", "url", "replyCount", "retweetCount", "likeCount"])
    
print(tweets)
