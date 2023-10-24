from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

from dotenv import load_dotenv
import os

load_dotenv()

face_endpoint = os.getenv("FACE_ENDPOINT")
face_key = os.getenv("FACE_KEY")

face_client = FaceClient(face_endpoint, CognitiveServicesCredentials(face_key))

for id in os.listdir("../material_preparation_step/digital-ids"):
    if id.endswith(".png"):
        with open(f"../material_preparation_step/digital-ids/{id}", "rb") as id_file:
            faces = face_client.face.detect_with_stream(id_file)
            for face in faces:
                print(f"Found Face ID {face.face_id} in {id}")
