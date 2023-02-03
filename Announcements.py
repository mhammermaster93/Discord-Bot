import os
import discord
# import googleapiclient.discovery


# my_secret = os.environ['youtube_api']

# service = googleapiclient.discovery.build("youtube", "v3", developerKey=my_secret)

# #API key added
# # api = os.environ.get(my_secret)
# api = os.environ.get('youtube_api')

# print(api)
# channel_id = "UCEPeyXOw5LA_DyTu2U4-4Gg"

# response = service.channels().list(
#     part="contentDetails",
#     id=channel_id
# ).execute()

# uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

# response = service.playlistItems().list(
#     part="snippet",
#     maxResults=200,
#     playlistId=uploads_playlist_id
# ).execute()

# videos = []
# for item in response["items"]:
#     video_id = item["snippet"]["resourceId"]["videoId"]
#     title = item["snippet"]["title"]
#     published_at = item["snippet"]["publishedAt"]
#     videos.append({"video_id": video_id, "title": title, "published_at": published_at})

# print("this is a video " + item['title'])
import os
import discord
from googleapiclient.discovery import build


#API key added
api = 'AIzaSyD-oubfkByi32q3KXwkxUwN5xgeb8Ae25Q'


youtube = build("youtube", "v3", developerKey=api)

channel_id = "UCEPeyXOw5LA_DyTu2U4-4Gg"

response = youtube.channels().list(
    part="contentDetails",
    id=channel_id
).execute()

uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

response = youtube.playlistItems().list(
    part="snippet",
    maxResults=200,
    playlistId=uploads_playlist_id
).execute()

videos = []
for item in response["items"]:
    video_id = item["snippet"]["resourceId"]["videoId"]
    title = item["snippet"]["title"]
    published_at = item["snippet"]["publishedAt"]
    videos.append({"video_id": video_id, "title": title, "published_at": published_at})

    print("this is a video " + item['snippet']['title'])