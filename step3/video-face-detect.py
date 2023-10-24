from video_indexer import VideoIndexer
from dotenv import load_dotenv
import os
import io
from PIL import Image

load_dotenv()

subscription_key = os.getenv("SUBSCRIPTION_KEY")
location = os.getenv("LOCATION")
account_id = os.getenv("ACCOUNT_ID")


video_analysis = VideoIndexer(
    vi_subscription_key=subscription_key,
    vi_location=location,
    vi_account_id=account_id,
)

info = video_analysis.get_video_info("7d38f35bee", video_language="English")

print(info)

images = []
for thumbnail in info["videos"][0]["insights"]["faces"][0]["thumbnails"]:
    file_name = thumbnail["fileName"]
    thumbnail_id = thumbnail["id"]
    img_code = video_analysis.get_thumbnail_from_video_indexer(
        "7d38f35bee", thumbnail_id
    )
    img_stream = io.BytesIO(img_code)
    img = Image.open(img_stream)
    images.append(img)

# create directory
if not os.path.exists("thumbnails"):
    os.makedirs("thumbnails")

# save directory
for i, img in enumerate(images):
    img.save("thumbnails/extract-face" + str(i + 1) + ".jpg")
