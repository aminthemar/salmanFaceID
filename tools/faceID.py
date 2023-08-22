from base.singleton import Singleton
import face_recognition
from io import BytesIO
import requests
import numpy as np
from PIL import Image

class FaceID(Singleton):
    encodings = []
    labels = []

    def __init__(self, modelPath="./static/model/"):
        if self.initialized:
            return
        self.initialized = True

        self.meetPersonnel("http://192.168.1.151:8000/")

    def meetPersonnel(self, baseURL):
        try:
            personnel_data = requests.get(baseURL+"human_resources/personnel/image").json()
            for personnel in personnel_data:
                if personnel["avatar"] is not None:
                    url = baseURL+personnel["avatar"]
                    known_image = requests.get(url).content
                    known_image = np.array(Image.open(BytesIO(known_image)))
                    known_image = face_recognition.face_encodings(known_image)[0]
                    self.encodings.append(known_image)
                    self.labels.append(personnel["id"])
            print(self.labels)
        except Exception as e:
            print("exception 2:", e)
    
    def findMatch(self, image_path):
        input_image = face_recognition.load_image_file(image_path)
        unknown_encoding = face_recognition.face_encodings(input_image)
        if(len(unknown_encoding) < 1):
            return None
        else:
            unknown_encoding = unknown_encoding[0]
        matches = face_recognition.compare_faces(self.encodings, unknown_encoding)
        face_distances = face_recognition.face_distance(self.encodings, unknown_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            return self.labels[best_match_index]
        else:
            return None