import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset

def main():
    # Load dataset
    dataset = load_dataset('text', data_files={'train': 'data/processed/cleaned_lyrics.txt'})

    # Load pre-trained model and tokenizer
    model_name = 'gpt2'
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Set the padding token to be the eos token
    tokenizer.pad_token = tokenizer.eos_token

    device = torch.device("cpu")
    model.to(device)

    # Preprocess data
    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True, num_proc=1, remove_columns=["text"])

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # Training arguments
    training_args = TrainingArguments(
        output_dir="./models/results",
        overwrite_output_dir=True,
        num_train_epochs=5,
        per_device_train_batch_size=2,  # Adjust batch size as needed
        save_steps=500,
        save_total_limit=2,
        logging_dir="./logs",
        logging_steps=10,
        evaluation_strategy="no",
        gradient_accumulation_steps=4,  # Accumulate gradients over multiple steps
        fp16=False,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_datasets["train"],
    )

    # Train model
    trainer.train()

if __name__ == "__main__":
    main()
