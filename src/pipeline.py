from src.youtube_api import (
    get_playlist_video_ids,
    get_video_details
)

from src.data_processing import process_video_data
from src.google_sheets_client import upload_dataframe

from src.config import PLAYLIST_ID


def run_pipeline():

    print("Recuperando vídeos da playlist...")

    video_ids = get_playlist_video_ids(PLAYLIST_ID)

    print("Recuperando estatísticas dos vídeos...")

    videos = get_video_details(video_ids)

    print("Processando dados...")

    df = process_video_data(videos)

    print("Enviando para o Google Sheets...")

    upload_dataframe(df)

    print("Pipeline concluída")