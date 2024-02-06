from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/overlay_settings'
mongo = PyMongo(app)

from app.routes.overlay import overlay_bp
app.register_blueprint(overlay_bp)

if __name__ == '__main__':
    app.run(debug=True)
