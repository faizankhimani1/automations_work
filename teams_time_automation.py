import time
import pyautogui
import subprocess
from datetime import datetime
from win10toast import ToastNotifier

toaster = ToastNotifier()

def notify(title, msg):
    toaster.show_toast(
        title,
        msg,
        duration=5,
        threaded=True
    )

def open_teams():
    subprocess.Popen("ms-teams:")

def keep_active():
    pyautogui.moveRel(5, 0, duration=0.1)
    pyautogui.moveRel(-5, 0, duration=0.1)

teams_opened = False
active_mode = False
lunch_notified = False
back_notified = False

print("Teams Time Automation Started")

while True:
    now = datetime.now().strftime("%H:%M")

    # 1:30 PM → Lunch → Away
    if now == "13:04" and not lunch_notified:
        notify(
            "Lunch Break 🍽️",
            "Lunch ka time ho gaya hai.\nIsliye aapko Away kar diya gaya hai."
        )
        active_mode = False
        lunch_notified = True
        back_notified = False
        time.sleep(60)

    # 2:30 PM → Back → Available
    if now == "14:07" and not back_notified:
        if not teams_opened:
            open_teams()
            teams_opened = True

        notify(
            "Back to Work ✅",
            "Lunch break end ho gaya hai.\nAapko Available kar diya gaya hai."
        )
        active_mode = True
        back_notified = True
        time.sleep(60)

    # Active = Available
    if active_mode:
        keep_active()

    time.sleep(40)
