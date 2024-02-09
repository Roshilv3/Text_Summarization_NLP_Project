import os
from src.text_summarization.logger import logging
from src.text_summarization.constants import *
from src.text_summarization.utils.common import read_yaml, create_directories
from datasets import load_dataset, load_from_disk

from transformers import (TrainingArguments,Trainer, 
                          DataCollatorForSeq2Seq, 
                          AutoModelForSeq2SeqLM, AutoTokenizer)
import torch

from src.text_summarization.entity import *
from src.text_summarization.config.configuration import *



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collector = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        #loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir='pegasus-samsum', 
            num_train_epochs= self.config.num_train_epochs, 
            warmup_steps= self.config.warmup_steps,
            per_device_train_batch_size= self.config.per_device_train_batch_size,
            per_device_eval_batch_size= self.config.per_device_eval_batch_size,
            weight_decay= self.config.weight_decay, 
            logging_steps= self.config.logging_steps,
            evaluation_strategy= self.config.evaluation_strategy,
            eval_steps= self.config.eval_steps, 
            save_steps= self.config.save_steps,
            gradient_accumulation_steps= self.config.gradient_accumulation_steps
        )

        # Train model
        trainer = Trainer(model= model_pegasus, args= trainer_args,
                          data_collator=seq2seq_data_collector,
                          tokenizer=tokenizer,
                          train_dataset=dataset_samsum_pt["test"],
                          eval_dataset=dataset_samsum_pt["validation"])
        
        trainer.train()

        # Save Model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))

        # Save Tokenizer
        tokenizer.save_pretrianed(os.path.join(self.config.root_dir, "tokenizer"))  