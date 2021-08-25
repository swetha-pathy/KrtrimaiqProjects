google_cloud_credentials = 'kr-imagesearch-credentials.json'
bucket = 'kr-misc-models'
filename = 'dermnet_skin_diseases_data2.csv'
age_mapping = {1: '0-10', 2: '11-20', 3: '21-30', 4: '31-40', 5: '41-50',
               6: '51-60', 7: '60-200'}

disease_mapping = {'Acne- closed comedone, open comedone- Mild acne': 0,
                   'Acne- Cystic, Pustular- Moderate acne': 1,
                   'Acne- Excoriated- Severe acne': 2,
                   'Angiokeratoma': 3,
                   'Calcifying epithelioma': 4,
                   'Chondrodermatis nodularis': 5,
                   'Rosacea': 6,
                   'Cowden disease': 7,
                   'Cylindroma': 8,
                   'Fibroma': 9,
                   'Merkel cell cancer': 10,
                   'Neurofibroma': 11,
                   'Actinic cheilitis': 12,
                   'Actinic keratosis': 13,
                   'Basal cell carcinoma': 14,
                   "Bowen's disease": 15,
                   'Psoriasis': 16,
                   'Reiter syndrome': 17,
                   'Rheumatoid nodule': 18,
                   'Seborrhoiec dermatitis': 19,
                   'Bullous pemphigoid': 20,
                   'Dermatitis herpetiformis': 21,
                   'Diabetic bullae': 22,
                   'Eczema': 23,
                   'Folliculitis, furuncles': 24,
                   'Herpes': 25,
                   'Hand, foot and mouth disease': 26,
                   'PLE': 27,
                   'Pompholyx': 28,
                   'Ecthyma': 29,
                   'Ichthyosis': 30,
                   'Impetigo': 31,
                   'Kerion': 32,
                   'Neurotic excoriation': 33,
                   'Pemphigus foliaceous': 34,
                   'Sycosis barbae': 35,
                   'Albinism': 36,
                   'Atypical naevi': 37,
                   'CTCL': 38,
                   'Hypomelanosis': 39,
                   'Lentigo': 40,
                   'Melasma': 41,
                   'Naevus anemicus': 42,
                   'Seborrhoeic keratoses': 43,
                   'Vitiligo': 44,
                   'Contact dermatitis': 45,
                   'Chancroid': 46,
                   'Lichen sclerosis': 47,
                   "Paget's", 48,
                   'Syphilis': 49,
                   'Cellulitis': 50,
                   'Pyoderma gangrenosum': 51,
                   'SCC': 52,
                   'Vasculitis': 53,
                   'Erythema ab igne': 54,
                   'Erythema multiformae': 55,
                   'Erythema infectiosum': 56,
                   'Lyme disease': 57,
                   'HSP': 58,
                   'Meningococcemia': 59,
                   'Schamberg disease': 60,
                   'Genital warts': 61,
                   'Periungual warts': 62,
                   'Warts digitate': 63,
                   'Oral warts': 64,
                   'Plantar warts': 65
                   }