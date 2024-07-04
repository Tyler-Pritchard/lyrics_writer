import os
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\. \.', '.', text)
    text = re.sub(r'\s+([.,!?])', r'\1', text)
    text = re.sub(r'[\r\n]', ' ', text)
    text = text.strip()
    return text

def preprocess_and_combine(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_folder):
            if filename.endswith('.txt'):
                with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as infile:
                    text = infile.read()
                    cleaned_text = clean_text(text)
                    outfile.write(cleaned_text + "\n")

if __name__ == "__main__":
    input_folder = 'data/raw/'  # Path to your raw text files
    output_file = 'data/processed/combined_data.txt'
    preprocess_and_combine(input_folder, output_file)
    print("Data preprocessing and combining complete.")
