from flask import (Flask, render_template, request, redirect, url_for, session, flash)
from datetime import timedelta, datetime

from flask_sqlalchemy import SQLAlchemy


def main():
    app = Flask(__name__)
    app.secret_key = "key"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class User(db.Model):
        _id = db.Column("id", db.Integer, primary_key=True)
        email = db.Column("email", db.String(120), unique=False, nullable=True)
        username = db.Column("username", db.String(80), unique=False, nullable=True)
        password = db.Column("password", db.String(120))
        login_date = db.Column("login_date", db.DateTime, nullable=False, default=datetime.utcnow)

        def __repr__(self):
            return '<User %r>' % self.username

    db.create_all()
    if not User.query.filter_by(username='admin'):
        admin = User(email="admin@root.com", username="YourMaster", password="admin")
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
        data = User.query.filter_by(email=username).first_or_404("Upppss, something went wrong")

        return f"<h1>{data.username}</h1>" \
               f"<h1>{data.email}</h1>" \
               f"<h1>{data.password}</h1>" \
               f"<p>{data}</p>"

    @app.route("/register", methods=["POST", "GET"])
    def register():
        if request.method == "POST":
            user = User(username=request.form['username'], email=request.form['email'],
                        password=request.form['password'])
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login"))
        else:
            return render_template("register.html")

    @app.route("/calendar")
    def calendar():
        pass

    app.run(debug=True)


if __name__ == '__main__':
    main()
