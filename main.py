from flask import (Flask, render_template, request, redirect, url_for, session, flash, Blueprint)
from model.database import db, User


bp = Blueprint("main", __name__)


@bp.route("/")
def main():
    return render_template('template.html')





