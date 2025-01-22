from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME="Data Ingestion stage"

try:
    obj=DataIngestionPipeline()
    obj.main()
except Exception as e:
    raise e

    
