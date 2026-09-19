from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e