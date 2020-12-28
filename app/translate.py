import json
import requests
from flask_babel import _
from app import app


def translate(text, dest_language):
    if 'IAM_TOKEN' not in app.config or not app.config['IAM_TOKEN']:
        return _('Error: the translation service is not configured.')

    url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    headers = {
        'Content-type': 'application/json',
        'Authorization': f"Bearer {app.config['IAM_TOKEN']}"
    }
    data = {
        "folder_id": "b1gdqll8rul9h2n8bq6l",
        "texts": text,
        "targetLanguageCode": dest_language
    }

    answer = requests.post(url, data=json.dumps(data), headers=headers)
    if answer.status_code != 200:
        return _('Error: the translation service failed.')

    return answer.json()['translations'][0]['text']

