from datetime import datetime
import os
from networksecurity.constant import training_pipeline


print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")):
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR

        self.artifact_dir = os.path.join(self.artifact_name, timestamp)

        self.timestamp: str = timestamp


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        # Data ingestion directory
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

        # Feature store path
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline.FILE_NAME
        )

        # Train dataset path
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TRAIN_FILE_NAME
        )

        # Test dataset path
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TEST_FILE_NAME
        )

        # Train-test split ratio
        self.train_test_split_ratio: float = (
            training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        )

        # MongoDB collection
        self.collection_name: str = (
            training_pipeline.DATA_INGESTION_COLLECTION_NAME
        )

        # MongoDB database
        self.database_name: str = (
            training_pipeline.DATA_INGESTION_DATABASE_NAME
        )