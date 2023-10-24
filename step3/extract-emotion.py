from video_indexer import VideoIndexer
import io, os
from PIL import Image
from dotenv import load_dotenv

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
sentiments = info["summarizedInsights"]["sentiments"]
for sentiment in sentiments:
    print(sentiment["sentimentKey"])

emotions = info["summarizedInsights"]["emotions"]
for emotion in emotions:
    print(emotion["type"])
