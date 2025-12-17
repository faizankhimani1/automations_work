from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

CSV_FILENAME = "flipkart_mobiles.csv"
WAIT_TIME = 15
SEARCH_QUERY = "Mobiles under ₹20000"
TOP_N = 20

def open_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_flipkart_mobiles():
    driver = open_chrome()
    wait = WebDriverWait(driver, WAIT_TIME)

    print("Opening Flipkart...")
    driver.get("https://www.flipkart.com")
    time.sleep(3)

    # Close login popup if it appears
    try:
        close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]")))
        close_btn.click()
    except:
        pass

    # Search bar
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys(SEARCH_QUERY)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    # Scroll down a bit to load products
    driver.execute_script("window.scrollTo(0, 1500);")
    time.sleep(3)

    # Find product cards (top-level product divs)
    products = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@class='_1AtVbE']//div[contains(@class,'_13oc-S')]")
    ))[:TOP_N]

    mobiles = []

    for product in products:
        try:
            name = product.find_element(By.XPATH, ".//a[@class='_1fQZEK']").text
        except:
            name = "N/A"
        try:
            price = product.find_element(By.XPATH, ".//div[@class='_30jeq3']").text
        except:
            price = "N/A"
        try:
            specs_text = product.find_element(By.XPATH, ".//div[@class='_1xgFaf']").text
            specs_parts = specs_text.split("|")
            ram = specs_parts[0].strip() if len(specs_parts) > 0 else "N/A"
            storage = specs_parts[1].strip() if len(specs_parts) > 1 else "N/A"
        except:
            ram = "N/A"
            storage = "N/A"

        mobiles.append([name, price, ram, storage])

    # Save CSV
    with open(CSV_FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Price", "RAM", "Storage"])
        writer.writerows(mobiles)

    print(f"✅ First {TOP_N} mobiles saved in '{CSV_FILENAME}'")
    driver.quit()

if __name__ == "__main__":
    scrape_flipkart_mobiles()
