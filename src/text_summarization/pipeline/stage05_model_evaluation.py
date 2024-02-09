from src.text_summarization.logger import logging
from src.text_summarization.entity import *
from src.text_summarization.config.configuration import *
from src.text_summarization.components.model_evaluation import *

class ModelEvaluationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.evaluate()


