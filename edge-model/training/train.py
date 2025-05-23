# edge-model/training/train.py

import os
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from dataset import EmailDataset

MODEL_NAME = "distilbert-base-uncased"

def main():
    data_path = os.path.join("../../data", "emails.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError("emails.csv not found in data directory")

    df = pd.read_csv(data_path)
    if 'text' not in df.columns or 'label' not in df.columns:
        raise ValueError("Dataset must contain 'text' and 'label' columns")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

    train_dataset = EmailDataset(df, tokenizer)

    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=16,
        logging_dir="./logs",
        logging_steps=10,
        save_strategy="epoch"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )

    trainer.train()

    model.save_pretrained("../onnx/model")
    tokenizer.save_pretrained("../onnx/model")

if __name__ == "__main__":
    main()
