from flask import Blueprint

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/<username>")
def username(username):
    data = User.query.filter_by(email=username).first_or_404("Upppss, something went wrong")

    return f"<h1>{data.username}</h1>" \
           f"<h1>{data.email}</h1>" \
           f"<h1>{data.password}</h1>" \
           f"<p>{data}</p>"


@bp.route("/calendar")
def calendar():
    return "Work in progress"
