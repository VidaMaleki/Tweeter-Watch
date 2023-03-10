from flask import Blueprint, jsonify
import snscrape.modules.twitter as sntwitter
from app import db
from datetime import datetime
from textblob import TextBlob
import json
# import pandas as pd

tweet_bp = Blueprint("tweete_watch", __name__)

tracked_accounts = ["@alikarimi_ak8", "@taylorlorenz", "@BarackObama"]

@tweet_bp.route("/accounts", methods=["GET"])
def get_accounts():
    db.session.add(tracked_accounts)
    db.session.commit()
    return jsonify(tracked_accounts), 200

# I created this endponit to check tweets structures
@tweet_bp.route("/<twitter_handle>/tweets", methods=["GET"])
def get_tweets(twitter_handle):
    limit = 10
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(f"from:{twitter_handle}").get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append({
                "tweet": tweet
            })
    return jsonify(tweets)

def get_conversation_threads(username, since_date):
    threads = []
    
    # Search for tweets directed to the user since the specified date
    search_query = f"to:{username} since:{since_date}"
    for tweet in sntwitter.TwitterSearchScraper(search_query).get_items():
        # Check if the tweet is a reply to another tweet
        if tweet.inReplyToTweetId is not None:
            # Look for the parent tweet in the existing threads
            parent_id = tweet.inReplyToTweetId
            parent_thread = next((t for t in threads if t['id'] == parent_id), None)
            if parent_thread is None:
                # Create a new thread if the parent tweet is not already in a thread
                parent_tweet = sntwitter.TwitterSearchScraper(f"from:{tweet.user.username} id:{parent_id}").get_items().__next__()
                parent_thread = {
                    'id': parent_tweet.id,
                    'content': parent_tweet.rawContent,
                    'date': parent_tweet.date,
                    'username': parent_tweet.user.username,
                    'url': parent_tweet.url,
                    'replyCount': parent_tweet.replyCount,
                    'retweetCount': parent_tweet.retweetCount,
                    'likeCount': parent_tweet.likeCount,
                    'replies': []
                }
                threads.append(parent_thread)
            
            # Add the current tweet as a reply to the parent tweet
            parent_thread['replies'].append({
                'id': tweet.id,
                'content': tweet.rawContent,
                'date': tweet.date,
                'username': tweet.user.username,
                'url': tweet.url,
                'replyCount': tweet.replyCount,
                'retweetCount': tweet.retweetCount,
                'likeCount': tweet.likeCount
            })
    
    return threads

@tweet_bp.route('/tweets/<twitter_handle>', methods=['GET'])
def get_user_tweets(twitter_handle):
    since_date = datetime(datetime.now().year, 3, 1).strftime('%Y-%m-%d')
    conversation_threads = get_conversation_threads(twitter_handle, since_date)
    db.session.add(conversation_threads)
    db.session.commit()
    return json.dumps({'threads': conversation_threads}, default=str)
    
    
@tweet_bp.route('/audience/<twitter_handle>', methods=['GET'])
def get_audience(twitter_handle):
    # Get tweets for the user
    since_date = datetime(datetime.now().year, 3, 1).strftime('%Y-%m-%d')
    tweets = get_user_tweets(twitter_handle, since_date)

    # Calculate audience information
    total_tweets = len(tweets)
    total_likes = sum(tweet['likeCount'] for tweet in tweets)
    total_retweets = sum(tweet['retweetCount'] for tweet in tweets)
    total_replies = sum(tweet['replyCount'] for tweet in tweets)
    unique_users = set(tweet['username'] for tweet in tweets)
    total_users = len(unique_users)

    # Create a dictionary with the audience information
    audience_info = {
        'twitter_handle': twitter_handle,
        'total_tweets': total_tweets,
        'total_likes': total_likes,
        'total_retweets': total_retweets,
        'total_replies': total_replies,
        'total_users': total_users
    }
    db.session.add(audience_info)
    db.session.commit()
    # Return the audience information as JSON
    return jsonify(audience_info), 200


def get_tweet_sentiment(tweet):
    # Create a TextBlob object of the tweet text
    blob = TextBlob(tweet['content'])

    # Determine the sentiment polarity (-1 to 1)
    sentiment = blob.sentiment.polarity

    # Classify the sentiment as positive, negative, or neutral
    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'


@tweet_bp.route('/sentiment/<twitter_handle>', methods=['GET'])
def get_sentiment(twitter_handle):
    # Get tweets for the user
    since_date = datetime(datetime.now().year, 2, 1).strftime('%Y-%m-%d')
    tweets = get_conversation_threads(twitter_handle, since_date)

    # Analyze the sentiment of each tweet and store the results
    tweet_sentiments = [get_tweet_sentiment(tweet) for tweet in tweets]

    # Calculate the overall sentiment of the tweets
    num_tweets = len(tweets)
    num_positive = tweet_sentiments.count('positive')
    num_negative = tweet_sentiments.count('negative')
    num_neutral = tweet_sentiments.count('neutral')
    overall_sentiment = 'neutral'
    if num_positive > num_negative and num_positive > num_neutral:
        overall_sentiment = 'positive'
    elif num_negative > num_positive and num_negative > num_neutral:
        overall_sentiment = 'negative'

    # Create a dictionary with the sentiment information
    sentiment_info = {
        'twitter_handle': twitter_handle,
        'num_tweets': num_tweets,
        'num_positive': num_positive,
        'num_negative': num_negative,
        'num_neutral': num_neutral,
        'overall_sentiment': overall_sentiment
    }
    
    db.session.add(sentiment_info)
    db.session.commit()

    return jsonify(sentiment_info), 200