from src.text_summarization.pipeline.stage01_data_ingestion import *
from src.text_summarization.logger import logging

STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>>stage {STAGE_NAME} started<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>>stage {STAGE_NAME} completed<<<")
except Exception as e:
    raise e