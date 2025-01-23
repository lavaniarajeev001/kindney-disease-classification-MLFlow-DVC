from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import Dataingestion
from src.cnnClassifier.components.prepare_base_mode import PrepareBaseModel

STAGE_NAME="Data Ingestion stage"
try: 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
except Exception as e:
        raise e



STAGE_NAME = "Prepare base model stage"
try: 
   prepare_base_model = PrepareBaseModelPipeline()
   prepare_base_model.main()
except Exception as e:
        raise e


STAGE_NAME="Model Training Stage"
try:
   Model_training=ModelTrainingPipeline()
   Model_training.main()
except Exception as e:
   raise e

    
