from flask import Flask
import os as __os

# __env_attrs = __os.environ

# PORT = int(__env_attrs.get('PORT'))
app = Flask(__name__)

from api.url_register import bp as url_register_bp
app.register_blueprint(url_register_bp)