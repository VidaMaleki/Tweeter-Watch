# Tweeter-Watch

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

