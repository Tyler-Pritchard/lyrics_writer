from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the trained model and tokenizer
model_path = 'models/results'
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

# Function to generate text
def generate_lyrics(prompt, max_length=100, num_return_sequences=1, num_beams=5, temperature=1.0, repetition_penalty=2.0):
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(
        inputs.input_ids, 
        max_length=max_length, 
        num_return_sequences=num_return_sequences,
        num_beams=num_beams,  # Use beam search
        temperature=temperature,
        repetition_penalty=repetition_penalty,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id  # Set pad token to eos token
    )
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

# Example prompt
prompt = "I woke up one evening and stepped out of the grave.  I wandered without purpose. It got so cold that my house burned down.  I fled to the forest to hide in the trees."
generated_lyrics = generate_lyrics(prompt, max_length=100, num_return_sequences=3)

# Print the generated lyrics
for i, lyrics in enumerate(generated_lyrics):
    print(f"Generated Lyrics {i+1}:\n{lyrics}\n")
