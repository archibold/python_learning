from flask import Blueprint, jsonify, request

from flaskr.extensions import db
from flaskr.models import Item


items_bp = Blueprint("items", __name__, url_prefix="/api/items")


@items_bp.get("")
def list_items():
    return jsonify([item.to_dict() for item in Item.query.order_by(Item.id).all()])


@items_bp.post("")
def create_item():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    if not name:
        return jsonify({"error": "Pole 'name' jest wymagane."}), 400

    item = Item(name=name, description=data.get("description"))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@items_bp.put("/<int:item_id>")
def update_item(item_id):
    item = db.session.get(Item, item_id)
    if item is None:
        return jsonify({"error": "Nie znaleziono elementu."}), 404

    data = request.get_json(silent=True) or {}
    if "name" in data:
        name = str(data["name"]).strip()
        if not name:
            return jsonify({"error": "Pole 'name' nie może być puste."}), 400
        item.name = name
    if "description" in data:
        item.description = data["description"]

    db.session.commit()
    return jsonify(item.to_dict())


@items_bp.delete("/<int:item_id>")
def delete_item(item_id):
    item = db.session.get(Item, item_id)
    if item is None:
        return jsonify({"error": "Nie znaleziono elementu."}), 404

    db.session.delete(item)
    db.session.commit()
    return "", 204
