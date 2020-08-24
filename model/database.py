from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, datetime
from flask import g
import sqlite3

import sqlite3
import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext

# db = SQLAlchemy(g)
#
# g.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# g.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db



def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)



# class User(db.Model):
#     __tablename__ = 'user'
#     _id = db.Column("id", db.Integer, primary_key=True)
#     email = db.Column("email", db.String(120), unique=False, nullable=True)
#     username = db.Column("username", db.String(80), unique=False, nullable=True)
#     password = db.Column("password", db.String(120))
#     login_date = db.Column("login_date", db.DateTime, nullable=False, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#
# db.create_all()
# if not User.query.filter_by(username='admin'):
#     admin = User(email="admin@root.com", username="YourMaster", password="admin")
#     db.session.add(admin)
#     db.session.commit()


