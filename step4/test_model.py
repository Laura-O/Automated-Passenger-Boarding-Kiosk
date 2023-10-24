from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient,
)
from msrest.authentication import ApiKeyCredentials

from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("ENDPOINT")
prediction_key = os.getenv("PREDICTION_KEY")

project_id = os.getenv("PROJECT_ID")
publish_iteration_name = os.getenv("PUBLISH_ITERATION_NAME")

prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key}
)
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)

for file in os.listdir("../material_preparation_step/lighter_test_images/"):
    with open(
        f"../material_preparation_step/lighter_test_images/{file}", "rb"
    ) as image_contents:
        results = predictor.detect_image(
            project_id, publish_iteration_name, image_contents.read()
        )

    for prediction in results.predictions:
        print(
            f"{prediction.tag_name} in {file}, probability: {round(prediction.probability * 100, 2)}%"
        )
