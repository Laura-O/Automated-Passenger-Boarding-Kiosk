from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
from dotenv import load_dotenv
import os

load_dotenv()

fr_endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
fr_key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
storage_url = os.getenv("AZURE_STORAGE_BLOB_URL")

# Testing
form_recognizer_client = FormRecognizerClient(
    endpoint=fr_endpoint, credential=AzureKeyCredential(fr_key)
)

for file in os.listdir("../material_preparation_step/digital-ids"):
    if file.endswith(".png"):
        with open(f"../material_preparation_step/digital-ids/{file}", "rb") as id_file:
            id = id_file.read()

        id_content = form_recognizer_client.begin_recognize_identity_documents(
            id, content_type="image/png"
        )
        id_content_result = id_content.result()

        id_content_result_dict = id_content_result[0].to_dict()

        print(f"ID file: {file}")
        for field_name, values in id_content_result_dict["fields"].items():
            print(values["name"], values["value"], values["confidence"])
