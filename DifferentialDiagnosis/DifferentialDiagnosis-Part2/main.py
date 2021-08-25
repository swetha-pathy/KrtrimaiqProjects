import utils
import config
import os
import sys

CREDENTIALS = config.google_cloud_credentials
BUCKET = config.bucket
FILENAME = config.filename
AGE_MAPPING = config.age_mapping

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS

# inputs
type_of_lesion = 'nodule'
no_of_lesions = 'solitary'  # solitary | multiple
body_location = 'hand'
age = 18  # 1 to 200
gender = 'Male'  # Female | Male
itching = 'yes'  # yes | no | sometimes
fever = 'no'  # yes | no
rate_of_dev = 'months'
appearance = 'well'


age = utils.convert_age_to_age_band(age, AGE_MAPPING)
metadata = utils.load_metadata(BUCKET, FILENAME)

predicted_disease = utils.predict_disease(metadata, type_of_lesion, no_of_lesions,
                                          body_location, age, gender, itching,
                                          fever, rate_of_dev, appearance)

print(predicted_disease)
