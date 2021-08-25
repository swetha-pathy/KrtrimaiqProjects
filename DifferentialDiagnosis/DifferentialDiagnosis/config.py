class_mapping = {0: 'Papule, Nodule, Plaque',
                 1: 'Vesicle, Blister, Pustule, Bullae',
                 2: 'Macule, Patch',
                 3: 'Purpura, Petichiae, Erythema',
                 4: 'Erosion, Ulcer',
                 5: 'Warts',
                 6: 'Scale, Crust, Excoriation'}

google_cloud_credentials = 'kr-imagesearch-credentials.json'
bucket = 'kr-misc-models'
model_name = 'dermnet0.h5'
input_shape = (256, 256, 3)
top_k = 3
