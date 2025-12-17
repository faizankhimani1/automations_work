from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

CSV_FILENAME = "imdb_movies_visible.csv"
WAIT_TIME = 10
IMDB_URL = "https://www.imdb.com/chart/top/"

def open_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_visible_movies():
    driver = open_chrome()
    wait = WebDriverWait(driver, WAIT_TIME)

    print("Opening IMDb Top 250 page...")
    driver.get(IMDB_URL)
    time.sleep(3)

    # Wait for movies container
    movies_rows = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "tbody.lister-list tr")
    ))

    # Open CSV file in append mode
    with open(CSV_FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Year", "Rating"])  # Header

        for row in movies_rows:
            try:
                title = row.find_element(By.CSS_SELECTOR, "td.titleColumn a").text
            except:
                title = "N/A"
            try:
                year = row.find_element(By.CSS_SELECTOR, "td.titleColumn span").text.replace("(", "").replace(")", "")
            except:
                year = "N/A"
            try:
                rating = row.find_element(By.CSS_SELECTOR, "td.ratingColumn.imdbRating strong").text
            except:
                rating = "N/A"

            writer.writerow([title, year, rating])

    print(f"✅ Movies saved in '{CSV_FILENAME}'")
    driver.quit()

if __name__ == "__main__":
    scrape_visible_movies()
