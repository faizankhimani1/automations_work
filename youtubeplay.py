# save as youtube_incognito_play.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------------------------
# CONFIG — यहाँ बदलें
# ---------------------------
VIDEO_QUERY = ""   # <-- यहाँ अपना सर्च टेक्स्ट डालें
VIDEO_URL = "https://youtu.be/-WnTkcq_By0?si=ZjG-MCbzgAt05h29"  # अगर पास हो तो ये डाल दें, तब search skip होगा (उदाहरण: "https://www.youtube.com/watch?v=xxxx")
WAIT_TIMEOUT = 15  # सेकंड (WebDriver waits)
# ---------------------------

def open_chrome_incognito():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")            # incognito mode
    options.add_argument("--start-maximized")      # maximize window
    # options.add_argument("--disable-extensions")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)

    # Create driver using webdriver-manager (auto-download driver)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def play_video_by_search(driver, query):
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    driver.get("https://www.youtube.com/")

    # wait for search box
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    # some YouTube pages use name="search_query", sometimes xpath for safety:
    try:
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)
    except Exception:
        # alternate way if 'search_query' not found/works
        search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

    # wait for results (video thumbnails)
    video_xpath = "//ytd-video-renderer//a[@id='thumbnail' and @href]"
    first_video = wait.until(EC.element_to_be_clickable((By.XPATH, video_xpath)))
    # click first video
    first_video.click()

    # wait for video player to load and play button presence
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "video")))
    time.sleep(1)  # small pause to allow playback to start
    # If playback didn't start automatically, click play button (center)
    try:
        play_button = driver.find_element(By.CSS_SELECTOR, "button.ytp-play-button")
        aria_label = play_button.get_attribute("aria-label") or ""
        if "Play" in aria_label:
            play_button.click()
    except Exception:
        pass

def play_video_by_url(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "video")))
    time.sleep(1)
    try:
        play_button = driver.find_element(By.CSS_SELECTOR, "button.ytp-play-button")
        aria_label = play_button.get_attribute("aria-label") or ""
        if "Play" in aria_label:
            play_button.click()
    except Exception:
        pass

def main():
    driver = open_chrome_incognito()
    try:
        if VIDEO_URL.strip():
            print("Opening specific video URL...")
            play_video_by_url(driver, VIDEO_URL)
        else:
            print(f"Searching YouTube for: {VIDEO_QUERY!r}")
            play_video_by_search(driver, VIDEO_QUERY)

        print("✅ Video should be playing now. Keeping browser open for 20 seconds...")
        time.sleep(20)  # adjust as needed; browser stays open
    except Exception as e:
        print("❌ Error:", e)
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    main()
