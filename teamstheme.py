# # File naam: teams_light_mode_100_percent.py
# # Double-click karo → bas 10 second mein Teams kholo → ho gaya!

# import pyautogui
# import time

# print("Teams ko LIGHT MODE kar raha hoon... 10 seconds mein Teams kholo")
# time.sleep(10)

# # 1. Settings kholo
# pyautogui.hotkey('ctrl', ',')
# time.sleep(4)

# # 2. Search box mein "appearance" type karo
# pyautogui.write('appearance', interval=0.1)
# time.sleep(2.5)

# # 3. Theme dropdown pe click karo (exact location tere screenshot ke hisaab se)
# # Dropdown right side mein hota hai → Tab se pahunch jayega
# pyautogui.press('tab', presses=5, interval=0.5)   # Theme dropdown tak jata hai
# time.sleep(1)
# pyautogui.press('enter')        # dropdown kholo
# time.sleep(1)

# # 4. Light mode select karo (2nd option)
# pyautogui.press('down')         # pehla wala (system) skip
# pyautogui.press('down')         # Light pe aa jao
# pyautogui.press('enter')        # Light select + apply
# time.sleep(2)

# # 5. Settings band kar do
# pyautogui.hotkey('esc', presses=3, interval=0.6)

# print("")
# print("==================================================")
# print("   SUCCESS! Teams ab pura LIGHT MODE mein hai    ")
# print("   Ab message wala script 100% chalega           ")
# print("==================================================")
# input("Enter daba ke band kar do...")


# File naam rakho: teams_proof_maker.py
# Double-click karo → bas chalega life-time tak!

import pyautogui
import time
import os
from datetime import datetime

# Folder banao aaj ki date ke naam se
today = datetime.now().strftime("%d_%b_%Y")
folder_name = f"Teams_Proof_{today}"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Naya folder bana diya: {folder_name}")

print("=== TEAMS PROOF MAKER SHURU === ")
print("Har 60 second mein screenshot le raha hoon...")
print("Band karne ke liye Ctrl+C daba dena terminal mein\n")

count = 0
try:
    while True:
        count += 1
        # Time format for file name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{folder_name}/Teams_{timestamp}.png"
        
        # Full screen screenshot (sirf Teams ka bhi kar sakte hain agar window title pata ho)
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        
        print(f"{count} → Screenshot liya: {filename}")
        
        # 60 second wait (1 minute)
        time.sleep(60)

except KeyboardInterrupt:
    print("\n\nBHAI BAND KAR DIYA! Total screenshots:", count)
    print(f"Saare proofs yahan milega → {os.getcwd()}\\{folder_name}")
    input("Enter daba ke band kar do...")