import platform
import psutil
import pywhatkit
import datetime
import time
import socket
import getpass
import os

# 1️⃣ Collect complete system info
def get_system_info():
    info = {
        "Username": getpass.getuser(),
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
        "Disk Total": f"{round(psutil.disk_usage('/').total / (1024**3), 2)} GB",
        "Disk Free": f"{round(psutil.disk_usage('/').free / (1024**3), 2)} GB",
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Current Directory": os.getcwd()
    }
    return info

sys_info = get_system_info()
message = "💻 System Info:\n" + "\n".join([f"{k}: {v}" for k, v in sys_info.items()])

# 2️⃣ Send via WhatsApp (robust)
phone_number = "+917041082582"  # Replace with recipient number
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute + 1  # send 1 minute later

print("⌛ Sending system info via WhatsApp...")

# Schedule message 1 minute later to ensure WhatsApp Web loads properly
pywhatkit.sendwhatmsg(phone_number, message, hour, minute, wait_time=20, tab_close=True)

print("✅ System info scheduled to be sent via WhatsApp!")
