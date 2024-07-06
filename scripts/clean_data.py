import re

def clean_lyrics(text):
    """
    Function to clean the lyrics text by removing unwanted characters and normalizing the text.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def clean_file(input_file, output_file):
    """
    Function to read the input file, clean each line, and write to the output file.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned_line = clean_lyrics(line)
            if cleaned_line:  # Only write non-empty lines
                outfile.write(cleaned_line + '\n')

if __name__ == "__main__":
    input_path = 'data/raw/lyrics.txt'
    output_path = 'data/cleaned_lyrics.txt'
    clean_file(input_path, output_path)
