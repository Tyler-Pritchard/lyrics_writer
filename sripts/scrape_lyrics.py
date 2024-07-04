import requests
from bs4 import BeautifulSoup

def scrape_lyrics(url):
    print(f"Scraping URL: {url}")
    response = requests.get(url)
    print(f"HTTP Status Code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    lyrics_div = soup.find('div', class_='lyrics')
    if not lyrics_div:
        lyrics_div = soup.find('div', class_='Lyrics__Root-sc-1ynbvzw-0')
    
    if lyrics_div:
        lyrics = lyrics_div.get_text(separator="\n")
        print(f"Lyrics found: {lyrics[:100]}...")  # Print the first 100 characters of the lyrics
        return lyrics
    else:
        print("Lyrics div not found.")
        return ""

url = 'https://genius.com/stairway-to-heaven'  # Replace with the actual URL
lyrics = scrape_lyrics(url)

if lyrics:
    with open('data/raw/lyrics.txt', 'a', encoding='utf-8') as file:  # Open file in append mode
        file.write(lyrics + "\n")  # Add a newline to separate entries
    print("Lyrics scraping complete and file updated.")
else:
    print("Failed to scrape lyrics.")
