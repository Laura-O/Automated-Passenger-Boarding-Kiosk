from video_indexer import VideoIndexer
from dotenv import load_dotenv
import os

load_dotenv()

subscription_key = os.getenv("SUBSCRIPTION_KEY")
location = os.getenv("LOCATION")
account_id = os.getenv("ACCOUNT_ID")


video_analysis = VideoIndexer(
    vi_subscription_key=subscription_key,
    vi_location=location,
    vi_account_id=account_id,
)

video_analysis.check_access_token()

uploaded_video_id = video_analysis.upload_to_video_indexer(
    input_filename="../material_preparation_step/digital-ids/avkash-boarding-pass.mp4",
    video_name="avkash-boarding-pass",
    video_language="English",
)

info = video_analysis.get_video_info(uploaded_video_id, video_language="English")

images = []
for thumbnail in info["videos"][0]["insights"]["faces"][0]["thumbnails"]:
    file_name = thumbnail["fileName"]
    thumbnail_id = thumbnail["id"]
    img_code = video_analysis.get_thumbnail_from_video_indexer(
        uploaded_video_id, thumbnail_id
    )
    img_stream = io.BytesIO(img_code)
    img = Image.open(img_stream)
    images.append(img)

for i, img in enumerate(images):
    img.save("../thumbnail/extract-face" + str(i + 1) + ".jpg")
