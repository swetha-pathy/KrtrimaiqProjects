import os
import utils

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './gcp_key.json'


def handler(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type, Content-Disposition'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    if request.method == 'POST':
        data = request.get_json()
        text = data['Text']
        translated_text = utils.translate_text(text)
        return (translated_text, 200, headers)
    else:
        return ("Text not translatable", headers)
