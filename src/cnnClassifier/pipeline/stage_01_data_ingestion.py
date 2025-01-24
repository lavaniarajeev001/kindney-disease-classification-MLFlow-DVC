import os
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import Dataingestion


STAGE_NAME="Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=Dataingestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__=="__main__":
    try:
        obj=DataIngestionPipeline()
        obj.main()
    except Exception as e:
        raise e


