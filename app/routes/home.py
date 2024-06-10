from flask import Blueprint, render_template, request

home_bp = Blueprint("home", __name__, url_prefix="/")


@home_bp.route("/")
def home():
    return render_template("pages/home/index.html")


@home_bp.route("/tree/<view>", methods=["GET"])
def tree(view):
    print("hello Pranav")
    if view == "horizontal":
        return render_template("pages/home/fragments/horizontal_tree.html")
    if view == "vertical":
        return render_template("pages/home/fragments/vertical_tree.html")    
    return render_template("pages/home/fragments/list.html")