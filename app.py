from flask import (Flask, render_template, request, redirect, url_for)

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('template.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login_name: str = request.form["email"]
        # password = request.form["password"]
        return redirect(url_for("username", username=login_name))
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    pass


@app.route("/<username>")
def username(username):
    return f"<h1>{username}</h1>"


@app.route("/calendar")
def calendar():
    pass


if __name__ == '__main__':
    app.run(debug=True)
