from src.text_summarization.pipeline.stage01_data_ingestion import *
from src.text_summarization.pipeline.stage02_data_validation import *
from src.text_summarization.logger import logging

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_01 = "DATA INGESTION STAGE"
try:
    logging.info(f">>>stage {STAGE_NAME_01} started<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>>stage {STAGE_NAME_01} completed<<<")
except Exception as e:
    raise e

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STAGE_NAME_02 = "DATA VALIDATION STAGE"
try:
    logging.info(f">>>stage {STAGE_NAME_02} started<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f">>>stage {STAGE_NAME_02} completed<<<")
except Exception as e:
    raise e

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


