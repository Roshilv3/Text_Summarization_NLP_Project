from src.text_summarization.config.configuration import ConfigurationManager
from src.text_summarization.components.model_trainer import ModelTrainer
from src.text_summarization.logger import logging


class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config= model_trainer_config)
        model_trainer.train()