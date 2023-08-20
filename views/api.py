from tools.faceID import FaceID
from flask import Blueprint, jsonify,request
import base64
import uuid
import os
import io

faceID = FaceID()
api = Blueprint("api", __name__)


@api.route("/predict/face/", methods=["POST"])
def predictFace():
    print("request")
    image_name = createName()
    result = None
    try:
        image_data = request.form["image"]
        image_data = image_data.replace('data:image/jpeg;base64,', '')  # Remove the data URL prefix
        with open(image_name, 'wb') as f:
            f.write(base64.b64decode(image_data))
        result = faceID.findMatch(image_name)
    except Exception as e:
        print("exception:", e)

    return jsonify({"result": result})

def createName():
    random_id = uuid.uuid4()
    return f"./media/images/face_{random_id}.jpeg"