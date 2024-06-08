from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models import Node
from app.schemas import node_input_schema

nodes_bp = Blueprint("nodes", __name__, url_prefix="/api/nodes")


@nodes_bp.route("/", methods=["POST"])
def add_node():
    data = request.get_json()
    
    errors = node_input_schema.validate(data)
    
    if errors:
        return jsonify(errors), 400
    
    if data["parent_id"] == 0:
        if db.session.query(Node).count() == 0:
            # Create the root node
            db.session.add(Node(
                left=1,
                right=2,
                name=data.get("name")
            ))
            
            return jsonify({"message": "Root node created successfully"}), 201
            
        # Root node exists, throw error
        return jsonify({
            "error": "Root node already exists",
        }), 400
    
    if data["parent_id"] not in [node.id for node in db.session.query(Node).all()]:
        # Parent node does not exist, throw error
        return jsonify({
            "error": "Parent node does not exist",
        }), 400
    
    parent_node = db.session.query(Node).filter_by(id=data["parent_id"]).first()


@nodes_bp.route("/tree", methods=["GET"])
def build_tree():
    return jsonify({
        "tree_data": {},
    })