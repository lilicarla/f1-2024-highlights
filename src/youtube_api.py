from googleapiclient.discovery import build
from src.config import YOUTUBE_API_KEY


def get_youtube_client():
    return build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def get_playlist_video_ids(playlist_id):

    youtube = get_youtube_client()

    video_ids = []

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50
    )

    while request:

        response = request.execute()

        for item in response["items"]:
            video_ids.append(
                item["snippet"]["resourceId"]["videoId"]
            )

        request = youtube.playlistItems().list_next(request, response)

    return video_ids


def get_video_details(video_ids):

    youtube = get_youtube_client()

    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=",".join(video_ids)
    )

    return request.execute()["items"]