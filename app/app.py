from flask import Flask
from .routes import home, admin, nodes
from dotenv import load_dotenv
import os
from .extensions import db, ma

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db.init_app(app)
ma.init_app(app)

app.register_blueprint(home.home_bp)
app.register_blueprint(admin.admin_bp)
app.register_blueprint(nodes.nodes_bp)

with app.app_context():
    db.create_all()