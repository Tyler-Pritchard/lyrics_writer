from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Add a padding token to the tokenizer
tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model.resize_token_embeddings(len(tokenizer))

# Prepare dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path='data/processed/combined_data.txt',  # Path to your combined data file
    block_size=128
)

# Create data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# Define training arguments
training_args = TrainingArguments(
    output_dir='../models/results',
    overwrite_output_dir=True,
    num_train_epochs=5,  # Increase number of epochs
    per_device_train_batch_size=4,
    save_steps=500,
    save_total_limit=2,
    logging_dir='../logs',
    logging_steps=100,
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained('../models/results')
tokenizer.save_pretrained('../models/results')

print("Training complete and model saved.")
