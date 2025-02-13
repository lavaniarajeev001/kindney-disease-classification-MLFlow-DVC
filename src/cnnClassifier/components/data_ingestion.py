import gdown
import zipfile
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
import os

class Dataingestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self)->str:
        try:
            dataset_url=self.config.source_URL
            zip_download_dir=self.config.local_data_file
            os.makedirs(self.config.root_dir,exist_ok=True)

            file_id=dataset_url.split("/")[-2]
            prefix='https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

        except Exception as e:
            raise e

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as f:
            f.extractall(unzip_path)