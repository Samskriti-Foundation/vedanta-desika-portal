from flask import Blueprint, render_template, request

home_bp = Blueprint("home", __name__, url_prefix="/")


@home_bp.route("/")
def home():
    view = request.args.get("view", "horizontal")
    return render_template("pages/home/index.html", view=view)

