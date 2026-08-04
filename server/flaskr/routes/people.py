from flask import Blueprint

peope_bp = Blueprint("people", __name__, url_prefix="/api/people")

@peope_bp.get("")
def all_people():
    pass