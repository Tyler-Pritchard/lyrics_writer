from transformers import GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset
import os

def main():
    # Load dataset and tokenizer
    dataset = load_dataset("text", data_files={"train": "data/cleaned_lyrics.txt"})
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Add padding token to tokenizer
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True, num_proc=1, remove_columns=["text"])

    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.resize_token_embeddings(len(tokenizer))

    # Data collator
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir="./models/results",
        overwrite_output_dir=True,
        num_train_epochs=5,
        per_device_train_batch_size=2,  # Adjust based on your hardware capabilities
        gradient_accumulation_steps=4,  # Gradient accumulation
        logging_dir="./logs",
        logging_steps=10,
        save_steps=500,
        fp16=False,  # Set to True if using mixed precision training and compatible hardware
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        data_collator=data_collator,
    )

    trainer.train()

if __name__ == "__main__":
    main()
