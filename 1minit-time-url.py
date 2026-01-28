from selenium import webdriver
import time
from datetime import datetime
import csv
from openpyxl import Workbook

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
            if driver.execute_script("return document.readyState") == "complete":
                return
        except:
            pass
        time.sleep(1)

def auto_scroll(driver):
    height = driver.execute_script("return document.body.scrollHeight")
    for y in range(0, height, 500):
        driver.execute_script(f"window.scrollTo(0, {y});")
        time.sleep(0.4)
    driver.execute_script("window.scrollTo(0, 0);")

# 🔥 Script start
script_start = datetime.now()
analytics = []

for index, url in enumerate(urls, start=1):
    page_start = datetime.now()

    driver.get(url)
    wait_for_full_load_safe(driver)
    auto_scroll(driver)

    time.sleep(60)  # 1 minute wait

    page_end = datetime.now()
    duration = round((page_end - page_start).total_seconds(), 2)

    analytics.append([
        index,
        url,
        page_start.strftime("%Y-%m-%d %H:%M:%S"),
        page_end.strftime("%Y-%m-%d %H:%M:%S"),
        duration
    ])

driver.quit()

script_end = datetime.now()
total_time = round((script_end - script_start).total_seconds(), 2)

# ======================
# 📄 CSV FILE EXPORT
# ======================
csv_file = "page_analytics.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Page No", "URL", "Start Time", "End Time", "Time Spent (sec)"])
    writer.writerows(analytics)
    writer.writerow([])
    writer.writerow(["Script Start", script_start.strftime("%Y-%m-%d %H:%M:%S")])
    writer.writerow(["Script End", script_end.strftime("%Y-%m-%d %H:%M:%S")])
    writer.writerow(["Total Time (sec)", total_time])

# ======================
# 📊 EXCEL FILE EXPORT
# ======================
wb = Workbook()
ws = wb.active
ws.title = "Automation Analytics"

ws.append(["Page No", "URL", "Start Time", "End Time", "Time Spent (sec)"])
for row in analytics:
    ws.append(row)

ws.append([])
ws.append(["Script Start", script_start.strftime("%Y-%m-%d %H:%M:%S")])
ws.append(["Script End", script_end.strftime("%Y-%m-%d %H:%M:%S")])
ws.append(["Total Time (sec)", total_time])

excel_file = "page_analytics.xlsx"
wb.save(excel_file)

print("✅ Analytics Generated Successfully")
print(f"📄 CSV File   : {csv_file}")
print(f"📊 Excel File : {excel_file}")
