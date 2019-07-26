from google_images_download import google_images_download
import pandas as pd
import os
from utils.create_breeds_file import create_breeds_file


dir_name = '../../data/images'

response = google_images_download.googleimagesdownload()

if os.path.exists("../../data/breeds_list.txt"):
    with open("../../data/breeds_list.txt") as f:
        keywords = f.read()
else:
    keywords = create_breeds_file()

arguments = {"keywords": keywords,
             "limit": 100,
             "print_urls": True,
             "output_directory": dir_name}

absolute_image_paths = response.download(arguments)

ids = []
breeds = []

for address, dirs, files in os.walk(dir_name):
    for file in files:
        breed = os.path.split(address)[1]
        ids.append(os.path.join('images',breed, file))
        breeds.append(breed)

df = pd.DataFrame({'id':ids, 'breed':breeds})

df.to_csv(os.path.join(os.path.split(dir_name)[0], 'labels.csv'), index=False)