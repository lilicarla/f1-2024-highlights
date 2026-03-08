import pandas as pd

def process_video_data(videos):

    data = []

    for video in videos:

        snippet = video["snippet"]
        stats = video["statistics"]
        id = video["id"]

        data.append({

            "title": snippet["title"],
            "description": snippet["description"],
            "published_at": snippet["publishedAt"],
            "thumbnail": snippet["thumbnails"]["high"]["url"],
            "video_url": f"https://www.youtube.com/watch?v={id}",

            "views": int(stats.get("viewCount", 0)),
            "likes": int(stats.get("likeCount", 0)),
            "comments": int(stats.get("commentCount", 0))
        })

    df = pd.DataFrame(data)

    df["engagement_rate"] = (
        (df["likes"] + df["comments"]) / df["views"]
    )

    return df