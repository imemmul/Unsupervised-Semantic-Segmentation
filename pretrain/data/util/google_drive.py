#
# Authors: Wouter Van Gansbeke & Simon Vandenhende
# Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)

import requests
import gdown
CHUNK_SIZE = 32768

def download_file_from_google_drive(id, destination):
    URL = f"https://drive.google.com/uc?id={id}"
    print(f"requesting URL: {URL}")
    pass
