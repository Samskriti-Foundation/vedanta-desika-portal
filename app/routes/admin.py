from flask import Blueprint, render_template

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/")
def login():
    return render_template("pages/admin/index.html", authenticated=False)

def home():
    return render_template("pages/admin/index.html", authenticated=True)