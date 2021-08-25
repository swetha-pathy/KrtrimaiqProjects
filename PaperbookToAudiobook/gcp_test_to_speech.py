import os
from google.cloud import texttospeech
from flask import send_file
from polyglot.detect import Detector


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './gcp_key.json'


def text_to_speech(request):
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
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

    request_json = request.get_json()

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    # Set the text input to be synthesized

    text = request_json['message']
    print(text)

    # Language detection polyglot
    detector = Detector(text)
    print(detector.language.code)
    lang_code = detector.language.code

    if "krtrimaiq" in text:
        ssml = '<speak>{}</speak>'.format(
            text.replace('krtrimaiq', 'krutrima<break time="0.1s"/>IQ'))

        synthesis_input = texttospeech.types.SynthesisInput(ssml=ssml)

    elif "Krtrimaiq" in text:
        ssml = '<speak>{}</speak>'.format(
            text.replace('Krtrimaiq', 'krutrima<break time="0.1s"/>IQ'))

        synthesis_input = texttospeech.types.SynthesisInput(ssml=ssml)

    else:
        synthesis_input = texttospeech.types.SynthesisInput(text=text)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code=lang_code,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    audio_file = client.synthesize_speech(synthesis_input, voice, audio_config)

    if (request_json['click'] == 'download'):
        with open('/tmp/audio_file.mp3', 'wb') as out:
            out.write(audio_file.audio_content)
        path_to_file = '/tmp/audio_file.mp3'

        print(os.listdir("/tmp"))
        print(len(os.listdir("/tmp")))

        return (send_file(
            path_to_file,
            as_attachment=True,
            cache_timeout=0), 200, headers)

    else:
        byte_stream = audio_file.audio_content
        return (byte_stream, 200, headers)
