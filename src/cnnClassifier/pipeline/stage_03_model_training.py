from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_training import ModelTrainingConfig
from src.cnnClassifier.components.model_training import ModelTraining


STAGE_NAME="Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_model_training_config()
            training = ModelTraining(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
    
        except Exception as e:
            raise e
        
if __name__=="__main__":
    try:
        obj=ModelTrainingPipeline
        obj.main()
    except Exception as e:
        raise e