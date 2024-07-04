# lyrics_writer

Welcome to the Lyrics Writer project! This project aims to use AI to generate song lyrics. It leverages the GPT-2 model from Hugging Face's Transformers library to create original and unique lyrics.

## Project Structure
lyrics_writer/
│
├── data/
│ ├── raw/ # Raw data files
│ ├── processed/ # Processed data files
│ └── cached/ # Cached data files
│
├── models/ # Saved models and tokenizer files
│ └── results/
│ ├── added_tokens.json
│ ├── config.json
│ ├── generation_config.json
│ ├── merges.txt
│ ├── model.safetensors
│ ├── special_tokens_map.json
│ ├── tokenizer_config.json
│ └── vocab.json
│
├── scripts/ # Python scripts for different tasks
│ ├── clean_data.py # Script for cleaning data
│ ├── train_model.py # Script for training the model
│ ├── scrape_lyrics.py # Script for web scraping lyrics
│ └── run_model.py # Script for generating lyrics
│
├── logs/ # Training and other logs
│
├── .gitignore # Git ignore file
│
└── README.md # Project documentation



## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)
- Git

### Installation

1. **Clone the repository:**

   ```
   bash
   git clone https://github.com/Tyler-Pritchard/lyrics_writer.git
   cd lyrics_writer
   ```

2. **Create a virtual environment and activate it:**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install the required packages:**
    ```
    pip install -r requirements.txt
    ```

## Usage
1. **Scrape Lyrics**    
    Use the scrape_lyrics.py script to scrape song lyrics from the web:
    ```
    python scripts/scrape_lyrics.py
    ```
    This script will scrape the lyrics and save them to data/raw/lyrics.txt.

2. **Clean Data**
    Use the clean_data.py script to clean and preprocess the data:
    ```
    python scripts/clean_data.py
    ```
    This script will preprocess the raw text files and save the cleaned data to data/processed/combined_data.txt.

3. **Train Model**
    Use the train_model.py script to train the GPT-2 model on the processed data:
    ```
    python scripts/train_model.py
    ```
    This script will train the model and save the trained model and tokenizer files to models/results/.

4. **Generate Lyrics**
    Use the run_model.py script to generate song lyrics using the trained model:
    ```
    python scripts/run_model.py
    ```
This script will load the trained model and generate lyrics based on a provided prompt.

## Project Overview

### Data Collection
    - Raw Data: Collected from various sources such as song lyrics websites.
    - Processed Data: Cleaned and preprocessed text data.
  
### Model Training
    - Model: GPT-2 from Hugging Face's Transformers library.
    - Training: Fine-tuning the model on the collected and processed lyrics data.
  
### Text Generation
    - Generation: Using the trained model to generate new song lyrics based on a prompt.

## Contributing
    Contributions are welcome! Please feel free to submit a Pull Request.

## License
    This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Hugging Face for providing the Transformers library.
Lyrics sources like Genius.

## Contact
For any inquiries, please reach out to Tyler Pritchard.