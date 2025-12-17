from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# -----------------------------
SEARCH_QUERY = "Hospitals near me"
TOP_N = 5
CSV_FILENAME = "nearby_hospitals_full.csv"
WAIT_TIME = 10
# -----------------------------

def open_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_hospitals():
    driver = open_chrome()
    wait = WebDriverWait(driver, WAIT_TIME)

    driver.get("https://www.google.com/maps")
    time.sleep(3)

    # Search box
    search_box = wait.until(EC.presence_of_element_located((By.ID, "searchboxinput")))
    search_box.send_keys(SEARCH_QUERY)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    # Wait for hospital cards to load
    hospital_cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='article']")))
    
    hospitals = []

    for card in hospital_cards[:TOP_N]:
        try:
            # Click hospital card to open details panel
            driver.execute_script("arguments[0].click();", card)
            time.sleep(3)

            # Name
            try:
                name = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class,'fontHeadlineLarge')]"))).text
            except:
                name = "N/A"

            # Rating
            try:
                rating = driver.find_element(By.XPATH, "//span[contains(@aria-label,'stars')]").text
            except:
                rating = "N/A"

            # Address
            try:
                address = driver.find_element(By.XPATH, "//button[@data-item-id='address']//div[1]").text
            except:
                address = "N/A"

            # Phone number
            try:
                phone = driver.find_element(By.XPATH, "//button[@data-item-id='phone']//div[1]").text
            except:
                phone = "N/A"

            # Open/Close timing
            try:
                timing = driver.find_element(By.XPATH, "//div[contains(@aria-label,'Open')] | //div[contains(@aria-label,'Closes')]").text
            except:
                timing = "N/A"

            # Maps link
            try:
                maps_link = driver.current_url
            except:
                maps_link = "N/A"

            hospitals.append([name, rating, address, phone, timing, maps_link])

        except Exception as e:
            print("Error scraping a hospital:", e)
            continue

    # Save CSV
    with open(CSV_FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Rating", "Address", "Phone", "Open/Close Timing", "Google Maps Link"])
        writer.writerows(hospitals)

    print(f"✅ Top {TOP_N} hospitals saved in '{CSV_FILENAME}'")
    driver.quit()

if __name__ == "__main__":
    scrape_hospitals()
