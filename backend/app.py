from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import ObjectId
import logging
import cv2
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:5173')  # Replace with your React app's actual origin
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/overlay_settings'
mongo = PyMongo(app)

class Camera:
    def __init__(self, rtsp_url):
        try:
            self.cap = cv2.VideoCapture(rtsp_url)
        except Exception as e:
            logging.error(f"Error initializing camera: {e}")

    def get_frame(self):
        # Assuming you want to capture a frame from the camera
        _, frame = self.cap.read()
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

def generate(camera):
    while True:
        frame = camera.get_frame()
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    # Assuming you want to use the Camera class here
    camera = Camera('your_rtsp_url_here')
    return Response(generate(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/overlay', methods=['GET', 'POST', 'DELETE'])
def overlay():
    if request.method == 'GET':
        overlay_settings = mongo.db.overlay_settings.find_one() or {}
        overlay_settings['_id'] = str(overlay_settings.get('_id'))
        return jsonify(overlay_settings)
    elif request.method == 'POST':
        data = request.json
        mongo.db.overlay_settings.replace_one({}, data, upsert=True)
        return jsonify(message='Overlay settings updated successfully')
    elif request.method == 'DELETE':
        mongo.db.overlay_settings.delete_one({})
        return jsonify(message='Overlay settings deleted successfully')

@app.route('/api/overlay/<string:overlay_id>', methods=['GET', 'PUT', 'DELETE'])
def overlay_by_id(overlay_id):
    if request.method == 'GET':
        overlay_settings = mongo.db.overlay_settings.find_one({'_id': ObjectId(overlay_id)})
        if overlay_settings:
            overlay_settings['_id'] = str(overlay_settings['_id'])
            return jsonify(overlay_settings)
        else:
            return jsonify(message='Overlay not found'), 404
    elif request.method == 'PUT':
        data = request.json
        if '_id' in data and isinstance(data['_id'], str):
            data['_id'] = ObjectId(data['_id'])
        result = mongo.db.overlay_settings.replace_one({'_id': ObjectId(overlay_id)}, data)
        if result.modified_count > 0:
            return jsonify(message='Overlay settings updated successfully')
        else:
            return jsonify(message='Overlay not found'), 404
    elif request.method == 'DELETE':
        result = mongo.db.overlay_settings.delete_one({'_id': ObjectId(overlay_id)})
        if result.deleted_count > 0:
            return jsonify(message='Overlay deleted successfully')
        else:
            return jsonify(message='Overlay not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
