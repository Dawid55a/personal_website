from flask import (Flask, render_template, request, redirect, url_for, session, flash)
from datetime import timedelta, datetime

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

email = ""
password = ""


class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.String(120), unique=False, nullable=True)
    username = db.Column("username", db.String(80), unique=False, nullable=True)
    password = db.Column("password", db.String(120))
    login_date = db.Column("login_date", db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()
if User.query.filter_by(username='admin') == False:
    admin = User(email="admin@root.com",username="YourMaster", password="admin")
    db.session.add(admin)
    db.session.commit()


@app.route("/")
def main():
    return render_template('template.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login_name: str = request.form["email"]
        # password = request.form["password"]
        session['email'] = login_name
        if User.query.filter_by(email=login_name):
            return redirect(url_for("username", username=login_name))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    if 'email' in session:
        session.pop('email', None)
    return redirect(url_for("login"))


@app.route("/user/<username>")
def username(username):
    return f"<h1>{username}</h1>"


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user = User(username=request.form['username'], email=request.form['email'], password=request.form['password'])
        db.session.add(user)
        return redirect(url_for("login"))
    else:
        return render_template("register.html")


@app.route("/calendar")
def calendar():
    pass


if __name__ == '__main__':
    app.run(debug=True)
