from flask import Blueprint

from hometap_interview.version import VERSION

health_bp = Blueprint('health', __name__, url_prefix='/api/health')

@health_bp.route('/', methods=['GET'])
def health():
    return {
        'status': 'UP',
        'version': VERSION
    }