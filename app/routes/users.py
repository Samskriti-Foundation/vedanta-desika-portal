from flask import Blueprint, jsonify
from app.extensions import db
from app.models import User

user_bp = Blueprint("nodes", __name__, url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def get_users():
    users = db.session.execute(db.select(User).order_by(User.first_name)).scalars()
    return users

@user_bp.route("/", methods=["POST"])
def add_user():
    return ""