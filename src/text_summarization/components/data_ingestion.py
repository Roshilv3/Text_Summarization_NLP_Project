
import os
from urllib import request
import zipfile

from src.text_summarization.logger import logging 
from src.text_summarization.constants import *
from src.text_summarization.utils.common import get_size
from src.text_summarization.entity import *


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logging.info(f"{filename} download! with following information: \n{headers}")
        else:
            logging.info(f"File already exist of size {get_size(Path(self.config.local_data_file))}")


    def extract_zip(self):
        """
        zip_file_path: str
        Extract the zip file into data directory.
        Function returns none
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


