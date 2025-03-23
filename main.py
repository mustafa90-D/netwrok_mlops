from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig
 

import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info("Initiating data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        print(dataingestionartifact)
        print("✅ Ingestion completed successfully!")
        print(f"📁 Train file: {dataingestionartifact.trained_file_path}")
        print(f"📁 Test file: {dataingestionartifact.test_file_path}")

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)

        logging.info("Initiating data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)

        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Starting data transformation")

        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)

        logging.info("Data transformation completed")

        logging.info("Starting model training")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(
            model_trainer_config=model_trainer_config, 
            data_transformation_artifact=data_transformation_artifact
        )
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info("Model training completed")
        
    except Exception as e:
        raise NetworkSecurityException(str(e), sys)
