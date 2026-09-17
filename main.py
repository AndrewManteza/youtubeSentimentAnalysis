import pandas as pd
from googleapiclient.discovery import build
from apiCredential import API_KEY

# Initialize the YouTube API client
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)


# Get comments for a specific video 
# Note this is for the initial testing and I need to make a function to iterate through each video in the list of videos that I have
# May need to export the list of videos to a CSV file and then read it in to iterate through each video ID
# Also need to create a separate Jupyter Notebook for the data preprocessing and analysis of the comments data that I will be collecting from the YouTube API


video_id = "ABC123XYZ"

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=100,
    textFormat="plainText"
)

response = request.execute()


# Turn the response into a pandas DataFrame
comments = []

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]

    comments.append({
        "author": comment["authorDisplayName"],
        "text": comment["textDisplay"],
        "likes": comment["likeCount"],
        "published_at": comment["publishedAt"]
    })

df = pd.DataFrame(comments)

df.head()