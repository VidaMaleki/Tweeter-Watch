# Tweeter-Watch
Build a system that tracks tweets and replies of the three of the following
accounts (pick whichever three you like) from **February 1st, 2023** onwards and
extracts some information, explained in the **Basics** section, based on the
tracked data.

The list of accounts:

- @alikarimi_ak8
- @elonmusk
- @BarackObama
- @taylorlorenz
- @cathiedwood
- @ylecun

## Requirements

### Basics

- For each account extract all the conversation threads. Data for each tweet
should at least include name of the author, time of the tweet and
text of the tweet. Feel free to include anything else you think is useful.
- For each account figure out a set of active audiences. A good heuristic for an active
audience is the set of accounts which reply to tweets of a given account.
- Sentiment:
Use any method you think best to assign sentiment scores to each of the following:
    - figure out how positive or negative each thread is.
    - figure out how positive or negative audience of (e.g. replies to) each thread is.

**Important:** The system should keep running and the information should remain up to date even after you have submitted your entry.

## Delivery

The delivery has two parts:

**API Endpoints:**

- Make a REST API with the following endpoints:
    - /accounts: return a json list of all tracked accounts.
    - /tweets/<twitter-handle> : return a json of the user's conversation threads since start.
    - /audience/<twitter-handle> : return a json of information about the audience for a user's account.
    - /sentiment/<twitter-handle> : return a json about the sentiment information of an account (e.g. thread level, audience level)

**Source Code:**

The source code behind the endpoints should be posted on Github or another code hosting website so we could review it.

To submit send an email to **competition@310.ai** before **March 11th**. The email should contain:

- a link to your API endpoint.
- a link to you source code.
- a link to the website if have made it for the extra score

### Extra Score

- Figure out a sentiment metric that measures how positive or negative each account is.
- Use AI to come up with a two paragraph summary description of the account.
- Make a website that presents the data extracted in a simple and clean way.
The list of accounts:

- @alikarimi_ak8
- @BarackObama
- @taylorlorenz

## Setup
### Managing Dependencies
Create a virtual environment:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ # You're in activated virtual environment!
```

Install dependencies (we've already gathered them all into a `requirements.txt` file):

```bash
(venv) $ pip install -r requirements.txt
```

## Setting Up Databases

Create one databases:
1. A development database named `tweeter-watch-db`

Note: If you want to test your project create two data base.

## Creating a `.env` File

Create a file named `.env`.

Create two environment variables that will hold your database URLs.

- `SQLALCHEMY_DATABASE_URI` to hold the path to your development database

Your `.env` may look like this:

```
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/tweeter-watch-db
```

## Run `$ flask db init`

Run `$ flask db init`.

**_After you make your first model in Wave 1_**, run the other commands `migrate` and `upgrade`.

## Run `$ flask run` or `$ FLASK_ENV=development flask run`

Check that your Flask server can run with `$ flask run`.

We can run the Flask server specifying that we're working in the development environment. This enables hot-reloading, which is a feature that refreshes the Flask server every time there is a detected change.

```bash
$ FLASK_ENV=development flask run
```
## Tweet Models


### Tips

SQLAlchemy's column type for text is db.String. The column type for datetime is db.DateTime.
SQLAlchemy supports nullable columns with specific syntax.
Don't forget to run:
flask db init once during setup
flask db migrate every time there's a change in models, in order to generate migrations
flask db upgrade to run all generated migrations

