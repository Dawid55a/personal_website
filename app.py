from flask import (Flask, render_template)

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/login")
def login():
    pass


@app.route("/logut")
def logout():
    pass


@app.route("/user/<username>")
def username():
    pass


@app.route("/calendar")
def calendar():
    pass


if __name__ == '__main__':
    app.run(debug=True)
