from flask import Blueprint, jsonify, request
from flask_pymongo import PyMongo

overlay_bp = Blueprint('overlay', __name__)
mongo=PyMongo()
@overlay_bp.route('/api/overlay', methods=['GET', 'POST'])
def overlay():
    if request.method == 'GET':
        overlay_settings = mongo.db.overlay_settings.find_one() or {}
        return jsonify(overlay_settings)
    elif request.method == 'POST':
        data = request.json
        mongo.db.overlay_settings.replace_one({}, data, upsert=True)
        return jsonify(message='Overlay settings updated successfully')
