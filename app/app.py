from flask import Flask
from .routes import home, admin

app = Flask(__name__)

app.register_blueprint(home.home_bp)
app.register_blueprint(admin.admin_bp)