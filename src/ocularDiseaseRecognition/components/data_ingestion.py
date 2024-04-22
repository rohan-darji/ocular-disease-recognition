import os
import urllib.request as request
import zipfile
from ocularDiseaseRecognition import logger
from ocularDiseaseRecognition.utils.common import get_size
import time
from requests.exceptions import Timeout
import subprocess
from ocularDiseaseRecognition.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)

        # Use Git LFS to pull the file
        try:
            subprocess.run(['kaggle', 'datasets', 'download', '-p', os.path.dirname(self.config.local_data_file), '-d', self.config.source_URL], check=True)
            print("Dataset downloaded successfully from Kaggle.")
        except subprocess.CalledProcessError as e:
            print(f"Error downloading dataset from Kaggle: {e}")

    def extract_zip_file(self):
        # Ensure the directory exists
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        
        # Extract the zip file
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            print("Zip file extracted successfully.")
