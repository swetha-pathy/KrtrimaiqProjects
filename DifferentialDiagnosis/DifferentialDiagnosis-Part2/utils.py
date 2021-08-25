import numpy as np
import pandas as pd
from google.cloud import storage


def download_file(bucket_name, file_name, output_fname):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = storage.Blob(file_name, bucket)
    blob.download_to_filename(output_fname)


def load_metadata(bucket_name, file_name, output_fname='/tmp/metadata.csv'):
    download_file(bucket_name, file_name, output_fname)
    df = pd.read_csv(output_fname)
    return np.array(df)


def convert_age_to_age_band(age, age_mapping):
    age = int(age)
    for a, band in age_mapping.items():
        start_age = int(band.split('-')[0].strip())
        end_age = int(band.split('-')[1].strip())
        if (age >= start_age) and (age < end_age):
            return a


def predict_disease(metadata, type_of_lesion, no_of_lesions, body_location,
                   age, gender, itching, fever, rate_of_dev, appearance):

    filt_lesion = []

    for n in metadata:
        for x in type_of_lesion.split(','):
            if x.lower() in n[1].lower():
                filt_lesion.append(n)

    scores = [0 for _ in filt_lesion]

    for i, n in enumerate(filt_lesion):
        # todo factor in rate_of_dev and appearance
        lesion_ = n[2]
        loc = n[3]
        age_band = n[4]
        com_gen = n[5]
        itch = n[6]
        fev = n[7]

        try:
            if no_of_lesions.lower() == 'solitary':
                if 'solitary' in lesion_.lower():
                    scores[i] += 2
            else:
                if 'multiple' in lesion_.lower():
                    scores[i] += 2
                elif lesion_.lower() == 'solitary':
                    scores[i] -= 2
        except AttributeError:
            pass

        try:
            if ('anywhere' in loc.lower()) or ('any site' in loc.lower()):
                scores[i] += 2
            elif body_location.lower() in loc.lower():
                scores[i] += 2
        except AttributeError:
            pass

        if str(age) in str(age_band):
            scores[i] += 1

        try:
            if com_gen.lower() == gender.lower():
                scores[i] += 1
        except AttributeError:
            scores[i] += 1

        try:
            if itch.lower() == itching.lower():
                scores[i] += 1
            elif (itch.lower() in ['sometimes', 'yes']) and (itching.lower() in ['sometimes', 'yes']):
                scores[i] += 0.5
        except AttributeError:
            pass

        try:
            if fev.lower() == fever.lower():
                scores[i] += 1
            elif (fever.lower() == 'yes') and (fev.lower() == 'sometimes'):
                scores[i] += 1
        except AttributeError:
            pass

    max_score = 0
    idx = []
    for ix, s in enumerate(scores):
        if s > max_score:
            max_score = s
            idx = [ix]
        elif s == max_score:
            idx.append(ix)

    probable_diseases = [m[0] for m in filt_lesion]
    return probable_diseases
