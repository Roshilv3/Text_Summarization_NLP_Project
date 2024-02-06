from urllib import request
import zipfile

from src.text_summarization.logger import logging 
from src.text_summarization.constants import *
from src.text_summarization.utils.common import read_yaml, create_directories
from src.text_summarization.entity import *


class ConfigurationManager:
    def __init__(
        self,
        config_path = Config_File_Path,
        params_path = Params_File_Path
        ):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.config.artifacts_root])





    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config