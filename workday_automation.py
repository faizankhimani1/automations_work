import time
import subprocess
import ctypes
import webbrowser
from datetime import datetime
from win10toast import ToastNotifier

toaster = ToastNotifier()

# ====== CONFIG (change easily) ======
WORK_START = "10:00"
LUNCH_START = "13:30"
LUNCH_END   = "14:30"
WORK_END    = "19:00"
# ==================================

done = {
    "start": False,
    "lunch_start": False,
    "lunch_end": False,
    "end": False
}

def notify(title, msg):
    toaster.show_toast(title, msg, duration=6, threaded=True)

def lock_screen():
    ctypes.windll.user32.LockWorkStation()

def open_apps():
    webbrowser.open("https://teams.microsoft.com/")
    webbrowser.open("https://mail.google.com/")
    webbrowser.open("https://jira.streebo.com/secure/Dashboard.jspa?selectPageId=10000")
    webbrowser.open("https://leetcode.com/")
    webbrowser.open("https://www.linkedin.com/")
    webbrowser.open("https://web.whatsapp.com/")
    webbrowser.open("https://www.youtube.com/")
    webbrowser.open("https://www.instagram.com/")

    subprocess.Popen("code")  # VS Code

print("✅ Workday Automation Started")

while True:
    now = datetime.now().strftime("%H:%M")

    # Work Start
    if now == WORK_START and not done["start"]:
        notify("Work Start 💼", "Office start ho gaya hai. Focus time!")
        open_apps()
        done["start"] = True

    # Lunch Start
    if now == LUNCH_START and not done["lunch_start"]:
        notify("Lunch Break 🍽️", "Lunch ka time ho gaya hai. Screen lock ho rahi hai.")
        lock_screen()
        done["lunch_start"] = True

    # Lunch End
    if now == LUNCH_END and not done["lunch_end"]:
        notify("Back to Work 🔔", "Lunch break end ho gaya hai. Kaam resume karein.")
        done["lunch_end"] = True

    # Work End
    if now == WORK_END and not done["end"]:
        notify("Work Complete ✅", "Work hours complete ho gaye hain. Good job!")
        lock_screen()
        done["end"] = True

    time.sleep(20)
