from flask import Blueprint, request

from api.controllers import calculate_price

from api.controllers import index_controller
from api.controllers import index

bp = Blueprint('url_register', __name__, template_folder='templates', static_folder='static')

bp.add_url_rule("/", view_func=index, methods=['GET', 'POST'])
bp.add_url_rule("/public/health/", view_func=index_controller, methods=['GET'])
bp.add_url_rule("/estimate_price", view_func=calculate_price, methods=['GET', 'POST'])
