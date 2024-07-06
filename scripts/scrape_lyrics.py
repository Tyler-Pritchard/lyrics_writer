from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os

def scrape_lyrics(url, driver, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            print(f"Scraping URL: {url}, Attempt: {attempt + 1}")
            driver.get(url)
            time.sleep(5)  # Wait for the page to load

            # Try to find the lyrics divs using multiple methods
            lyrics_div = None
            possible_selectors = [
                'div.lyrics',  # Older Genius layout
                'div.Lyrics__Root-sc-1ynbvzw-0',  # Newer Genius layout
                'div.Lyrics__Container-sc-1ynbvzw-6',  # Another possible layout
                '.lyrics'  # Just in case
            ]

            for selector in possible_selectors:
                try:
                    lyrics_div = driver.find_element(By.CSS_SELECTOR, selector)
                    if lyrics_div:
                        break
                except:
                    continue

            if lyrics_div:
                lyrics = lyrics_div.text
                return lyrics.strip()
            else:
                print(f"Lyrics div not found for {url}")
                return ""
        except Exception as e:
            print(f"Failed to scrape lyrics from {url}: {e}")
            attempt += 1
            if attempt < retries:
                print(f"Retrying {url}...")
            else:
                return ""

def main():
    # Set up Selenium WebDriver with uBlock Origin
    options = Options()
    options.add_argument("--headless=new")  # Run in headless mode
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-remote-fonts")

    # Path to the uBlock Origin extension
    ublock_origin_path = os.path.abspath('extensions/uBlock0_1.39.2.crx')
    if not os.path.exists(ublock_origin_path):
        raise OSError(f"Path to the extension doesn't exist: {ublock_origin_path}")

    options.add_extension(ublock_origin_path)

    service = Service('/usr/local/bin/chromedriver')  # Path to your WebDriver

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(60)  # Increase page load timeout

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
