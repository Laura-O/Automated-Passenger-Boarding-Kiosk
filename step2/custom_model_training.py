from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from dotenv import load_dotenv
import os

load_dotenv()

fr_endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
fr_key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
storage_url = os.getenv("AZURE_STORAGE_BLOB_URL")

# Training

form_training_client = FormTrainingClient(
    endpoint=fr_endpoint, credential=AzureKeyCredential(fr_key)
)

training_process = form_training_client.begin_training(
    storage_url, use_training_labels=False, include_subfolders=True
)
custom_model = training_process.result()

print(custom_model)

print(f"Custom Model ID's: {custom_model.model_id}")
print(f"Custom Model status: {custom_model.status}")

# Testing
form_recognizer_client = FormRecognizerClient(
    endpoint=fr_endpoint, credential=AzureKeyCredential(fr_key)
)

with open("../material_preparation_step/boarding-pass/boarding-avkash.pdf", "rb") as f:
    poller = form_recognizer_client.begin_recognize_custom_forms(
        model_id=custom_model.model_id,
        form=f,
        include_field_elements=True,
    )
forms = poller.result()

for idx, form in enumerate(forms):
    for name, field in form.fields.items():
        if field.label_data:
            print(
                "Label: '{}', Value: '{}'".format(
                    field.label_data.text if field.label_data else name,
                    field.value,
                )
            )
