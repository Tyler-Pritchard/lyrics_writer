from transformers import Trainer, TrainingArguments

def main():
    # Load dataset and tokenizer as before
    dataset = load_dataset("text", data_files={"train": "data/cleaned_lyrics.txt"}) # type: ignore
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2") # type: ignore

    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True, num_proc=1, remove_columns=["text"])

    model = GPT2LMHeadModel.from_pretrained("gpt2") # type: ignore

    training_args = TrainingArguments(
        output_dir="./models/results",
        overwrite_output_dir=True,
        num_train_epochs=5,
        per_device_train_batch_size=1,  # Reduced batch size
        gradient_accumulation_steps=4,  # Gradient accumulation
        logging_dir="./logs",
        logging_steps=10,
        save_steps=500,
        fp16=True,  # Mixed precision training
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
    )

    trainer.train()

if __name__ == "__main__":
    main()
