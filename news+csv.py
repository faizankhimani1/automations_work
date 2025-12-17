from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# -----------------------------
# CONFIG
# -----------------------------
NEWS_SITE = "https://www.ndtv.com/india-news/"
WAIT_TIME = 10
CSV_FILENAME = "latest_news.csv"
# -----------------------------

def open_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver

def scrape_latest_news():
    driver = open_chrome()
    wait = WebDriverWait(driver, WAIT_TIME)

    print("Opening Google News...")
    driver.get(NEWS_SITE)
    time.sleep(3)

    print("Scraping latest news headlines...")

    # News headlines container
    articles = driver.find_elements(By.XPATH, "//article//h3/a")

    news_data = []
    for art in articles[:20]:  # Top 20 news
        try:
            title = art.text
            link = art.get_attribute("href")
            news_data.append([title, link])
        except:
            continue

    # Save CSV
    with open(CSV_FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Headline", "Link"])
        writer.writerows(news_data)

    print(f"✅ Top {len(news_data)} news saved in '{CSV_FILENAME}'")
    driver.quit()

if __name__ == "__main__":
    scrape_latest_news()
