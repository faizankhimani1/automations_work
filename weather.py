from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# -----------------------------
# CONFIG
# -----------------------------
CITY = "Jasdan"   # Change city as needed
WAIT_TIME = 50
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

def check_weather(city):
    driver = open_chrome()
    wait = WebDriverWait(driver, WAIT_TIME)

    driver.get("https://www.google.com/")
    time.sleep(2)

    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys(f"Weather in {city}")
    search_box.send_keys(Keys.ENTER)

    # Wait for weather widget
    temp_elem = wait.until(EC.presence_of_element_located((By.ID, "wob_tm")))
    cond_elem = driver.find_element(By.ID, "wob_dc")
    hum_elem = driver.find_element(By.ID, "wob_hm")

    temperature = temp_elem.text
    condition = cond_elem.text
    humidity = hum_elem.text

    print(f"🌤 Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")

    driver.quit()

if __name__ == "__main__":
    check_weather(CITY)
