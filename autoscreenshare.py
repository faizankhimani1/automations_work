# File naam: 2_second_share_prank.py
# Double-click karo → 2 second share → auto stop!

import pyautogui
import time

print("2 SECOND SHARE PRANK shuru... 5 sec mein cursor hata lena")
time.sleep(5)

# Step 1: Share start karo (Ctrl + Shift + E)
pyautogui.hotkey('ctrl', 'shift', 'e')
time.sleep(1.8)

# Step 2: Entire screen select + Share
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('enter')
print("Share ON ho gaya!")

# Step 3: Sirf 2 second wait → phir stop!
time.sleep(2)

# Step 4: Share STOP kar do (Ctrl + Shift + E again = toggle off)
pyautogui.hotkey('ctrl', 'shift', 'e')
print("Share STOP ho gaya! Prank successful 😂")

input("\nPrank complete! Enter daba ke band kar do...")