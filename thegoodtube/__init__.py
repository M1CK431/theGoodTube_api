from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
CORS(app)
app.config.from_object('config')
socketio = SocketIO(app, cors_allowed_origins="*", logger=True)


@app.route("/", methods=["GET"])
def root():
    return jsonify({
        "name": "theGoodTube",
        "description": "REST API over youtube-dl",
        "version": app.config["VERSION"],
        "environment": app.config["ENV"]
    })


from . import downloads # noqa
