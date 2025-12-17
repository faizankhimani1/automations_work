from selenium import webdriver
import time

# Chrome को visibly open करने के लिए ये enough है
driver = webdriver.Chrome()

print("🚀 Automation Starting... Browser opening...")

# URL open
driver.get("https://faizankhimani.netlify.app/")
print("🌐 URL Opened Successfully!")

# 10 seconds तक खुला छोड़े ताकि आप देख सकें
time.sleep(10)

print("✅ Automation Finished. Closing browser...")
driver.quit()
