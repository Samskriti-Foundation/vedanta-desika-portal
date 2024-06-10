from flask import Blueprint, render_template

from app.forms import LoginForm

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/")
def login():
    form = LoginForm()
    return render_template("pages/admin/index.html", authenticated=False, form=form)

def home():
    return render_template("pages/admin/index.html", authenticated=True)