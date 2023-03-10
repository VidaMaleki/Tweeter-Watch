from app import db


class TrackedAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f'<TrackedAccount {self.account_name}>'

class TweetThread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(5000), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    reply_count = db.Column(db.Integer, nullable=False)
    retweet_count = db.Column(db.Integer, nullable=False)
    like_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<TweetThread {self.id}>'

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(280), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    reply_count = db.Column(db.Integer, nullable=False)
    retweet_count = db.Column(db.Integer, nullable=False)
    like_count = db.Column(db.Integer, nullable=False)
    parent_thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    replies = db.relationship('Thread', backref=db.backref('parent_thread', remote_side=[id]), lazy=True)

    def __init__(self, tweet_id, content, date, username, url, reply_count, retweet_count, like_count):
        self.tweet_id = tweet_id
        self.content = content
        self.date = date
        self.username = username
        self.url = url
        self.reply_count = reply_count
        self.retweet_count = retweet_count
        self.like_count = like_count

    def __repr__(self):
        return '<Thread %r>' % self.tweet_id

class Audience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    twitter_handle = db.Column(db.String(255), nullable=False)
    total_tweets = db.Column(db.Integer, nullable=False)
    total_likes = db.Column(db.Integer, nullable=False)
    total_retweets = db.Column(db.Integer, nullable=False)
    total_replies = db.Column(db.Integer, nullable=False)
    total_users = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Audience {self.twitter_handle}>'

class Sentiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    twitter_handle = db.Column(db.String(255), nullable=False)
    num_tweets = db.Column(db.Integer, nullable=False)
    num_positive = db.Column(db.Integer, nullable=False)
    num_negative = db.Column(db.Integer, nullable=False)
    num_neutral = db.Column(db.Integer, nullable=False)
    overall_sentiment = db.Column(db.String(10))
    tweets = db.relationship('Tweet', backref='sentiment')

    def __repr__(self):
        return f'<Sentiment {self.twitter_handle}>'