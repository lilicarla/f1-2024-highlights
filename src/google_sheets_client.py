import gspread
from google.oauth2.service_account import Credentials
from src.config import SPREADSHEET_ID, CREDENTIALS_FILE

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def get_client():

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )

    return gspread.authorize(creds)


def upload_dataframe(df):

    client = get_client()

    sheet = client.open_by_key(SPREADSHEET_ID).sheet1

    sheet.clear()

    sheet.update(
        [df.columns.values.tolist()] +
        df.values.tolist()
    )