import os
from google.cloud import vision
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './gcp_key.json'


def detect_text(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
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
    request_json = request.files.to_dict()
    print(request_json)
    if request_json:
        print(request_json['image'])

        """Detects text in the file."""
        client = vision.ImageAnnotatorClient()
        print(client)

        image = vision.types.Image(content=request_json["image"].read())

        response = client.document_text_detection(image=image)
        texts = response.text_annotations

        for text in texts:
            text_from_image = ''.join(text.description)
            return(text_from_image, 200, headers)

    else:
        return(200, headers)


