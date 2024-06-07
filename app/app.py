from flask import Flask
from .routes import home, admin
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'

app.register_blueprint(home.home_bp)
app.register_blueprint(admin.admin_bp)