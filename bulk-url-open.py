from selenium import webdriver
import time

urls = [
    "https://www.streebo.com/lp-chatbot-for-telecom?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-field-service-manufacturing-chatbot?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-travel-chatbot?%20utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-retail?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-airlines?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-hospitality?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/ai-orchestration?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-banking?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-financial-services-chatbot?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-government?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-insurance-chatbot?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-healthcare?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-logistics-chatbot?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-education?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-utility-sector?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-food-beverage-chatbot?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-ai-pharmacy-chatbot?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-non-profit-organization?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-telecom?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-field-service-manufacturing-chatbot?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-chatbot-for-hr?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget",
    "https://www.streebo.com/lp-oil-and-gas-chatbot?utm_source=linkedin&utm_medium=cpc&utm_campaign=retarget"
]

driver = webdriver.Chrome()

def wait_for_full_load_safe(driver, timeout=90):
    start = time.time()
    while time.time() - start < timeout:
        try:
            ready = driver.execute_script("return document.readyState")
            if ready == "complete":
                return
        except:
            pass
        time.sleep(1)
    print("Load timeout, continuing...")

def auto_scroll(driver):
    height = driver.execute_script("return document.body.scrollHeight")
    for y in range(0, height, 500):
        driver.execute_script(f"window.scrollTo(0, {y});")
        time.sleep(0.4)
    driver.execute_script("window.scrollTo(0, 0);")

for url in urls:
    print("Opening:", url)
    driver.get(url)

    wait_for_full_load_safe(driver)
    auto_scroll(driver)

    time.sleep(3)

driver.quit()
