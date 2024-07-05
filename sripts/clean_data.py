import os
import re

def clean_lyrics(lyrics):
    # Remove unwanted characters and multiple consecutive whitespaces
    lyrics = re.sub(r'[,.;:\-\']', '', lyrics)  # Remove punctuation
    lyrics = re.sub(r'\s+', ' ', lyrics).strip()  # Replace multiple whitespaces with a single space
    lyrics = re.sub(r'\[.*?\]', '', lyrics)  # Remove content within brackets
    lyrics = re.sub(r'\(.*?\)', '', lyrics)  # Remove content within parentheses
    return lyrics

def main():
    input_file_path = os.path.abspath('data/raw/lyrics.txt')
    output_file_path = os.path.abspath('data/processed/cleaned_lyrics.txt')

    if not os.path.exists(input_file_path):
        print(f"Input file {input_file_path} does not exist.")
        return

    with open(input_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned_lyrics = clean_lyrics(line)
            if cleaned_lyrics:  # Write only non-empty lines
                outfile.write(cleaned_lyrics + '\n')

if __name__ == "__main__":
    main()
