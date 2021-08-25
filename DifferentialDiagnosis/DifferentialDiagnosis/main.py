import utils
import config
import os
import sys
from google.cloud import storage
import json

CREDENTIALS = config.google_cloud_credentials
BUCKET = config.bucket
MODEL_NAME = config.model_name
INPUT_SHAPE = config.input_shape
CLASS_MAPPING = config.class_mapping
TOP_K = config.top_k

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS
MODEL = None


def handler(request):
    global MODEL, input_image

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
        if MODEL is None:
            output_filename = '/tmp/model.h5'
            MODEL = utils.load_model(BUCKET, MODEL_NAME, output_filename)

        images = request.files.getlist("s3-input-ke-2[]")
        for i in range(0, len(images)):
            input_image = images[i].read()

        try:
            image = utils.load_image(input_image, INPUT_SHAPE)
            input_arr = utils.preprocess(image)
        except Exception as e:
            print(e)
            print('Unable to load image')
            sys.exit(-1)

        # make predictions
        try:
            output = utils.make_prediction(input_arr, MODEL, TOP_K)
        except Exception as e:
            print(e)
            sys.exit(-1)

        # final output
        output_mapped = [(CLASS_MAPPING[x], p) for x, p in output]
        print(output_mapped)
        output_mapped = json.dumps(output_mapped)
        print(output_mapped)
        return (output_mapped, 200, headers)
