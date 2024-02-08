from src.text_summarization.pipeline.stage01_data_ingestion import *
from src.text_summarization.pipeline.stage02_data_validation import *
from src.text_summarization.pipeline.stage03_data_transformation import *
from src.text_summarization.logger import logging

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_01 = "DATA INGESTION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_01} started<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>> {STAGE_NAME_01} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_02 = "DATA VALIDATION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_02} started<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f">>> {STAGE_NAME_02} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_03 = "DATA TRANSFORMATION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_03} started<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logging.info(f">>> {STAGE_NAME_03} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

