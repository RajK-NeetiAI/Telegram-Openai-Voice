import os
import tempfile

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

CREDENTIALS = os.getenv('CREDENTIALS')
GCP_CLOUD_STORAGE_BUCKET_NAME = os.getenv('GCP_CLOUD_STORAGE_BUCKET_NAME')

ERROR_MESSAGE = 'We are facing an issue, please try after sometimes.'
AUDIO_FILE_FORMAT = 'mp3'

"""Use the following variable to control the response type
"audio" -> to send audio responses
"text" -> to send text message
"""
REPLY_TYPE = 'audio' # "text"

OUTPUT_DIR = os.path.join(
    tempfile.gettempdir(),
    'telegrambot'
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

CREDENTIALS_FILE_PATH = os.path.join(
    OUTPUT_DIR,
    'credentials.json'
)
