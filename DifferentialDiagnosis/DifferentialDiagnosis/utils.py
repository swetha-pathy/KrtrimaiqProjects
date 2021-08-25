import numpy as np
import cv2
from google.cloud import storage
import tensorflow.keras.models as KM


def download_file(bucket_name, file_name, output_fname):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = storage.Blob(file_name, bucket)
    blob.download_to_filename(output_fname)


def load_model(bucket_name, file_name, output_fname):
    download_file(bucket_name, file_name, output_fname)
    return KM.load_model(output_fname, compile=False)


def load_image(img_bytes, shape=None, color_format='rgb'):
    """ Reads image as numpy array """
    image = np.frombuffer(img_bytes, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    if color_format == 'rgb':
        image = image[:, :, ::-1]
    if image.shape != shape:
        image = cv2.resize(image, (shape[0], shape[1]))
    return image


def preprocess(img):
    mean = np.mean(img)
    std = np.std(img)
    img = (img - mean) / (std + 1e-5)
    return np.expand_dims(img, axis=0)


def make_prediction(inp, model, top_k=3):
    predictions = list(np.squeeze(np.array(model.predict(inp))))
    output = []
    for _ in range(top_k):
        arg_max = np.argmax(predictions)
        output.append((arg_max, predictions[arg_max]))
        predictions[arg_max] = 0
    return output


