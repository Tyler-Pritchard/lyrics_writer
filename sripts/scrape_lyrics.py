from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

def scrape_lyrics(url, driver):
    try:
        print(f"Scraping URL: {url}")
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        # Try to find the lyrics divs using multiple methods
        lyrics_div = driver.find_element(By.CSS_SELECTOR, 'div.lyrics')
        if not lyrics_div:
            lyrics_div = driver.find_element(By.CSS_SELECTOR, 'div.Lyrics__Root-sc-1ynbvzw-0')
        if not lyrics_div:
            lyrics_div = driver.find_element(By.CSS_SELECTOR, 'div.Lyrics__Container-sc-1ynbvzw-6')

        if lyrics_div:
            lyrics = lyrics_div.text
            return lyrics.strip()
        else:
            print(f"Lyrics div not found for {url}")
            return ""

    except Exception as e:
        print(f"Failed to scrape lyrics from {url}: {e}")
        return ""

def main():
    # Set up Selenium WebDriver
    options = Options()
    options.headless = True  # Run in headless mode
    service = Service('path/to/your/webdriver')  # Path to your WebDriver

    driver = webdriver.Chrome(service=service, options=options)

    # Load the URLs from the Excel file
    df = pd.read_excel('data_sets/song_links.xlsx')
    urls = df['URL'].tolist()

    # Open the file in append mode
    with open('data/raw/lyrics.txt', 'a', encoding='utf-8') as file:
        for url in urls:
            lyrics = scrape_lyrics(url, driver)
            if lyrics:
                file.write(lyrics + "\n\n")
                print(f"Lyrics scraped and appended from: {url}")
            else:
                print(f"Failed to scrape lyrics from: {url}")

    driver.quit()

if __name__ == "__main__":
    main()
