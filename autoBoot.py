# Generalized imports
import subprocess
import os
import time

def checkRunning():
    try:
        output = str(subprocess.check_output("ps aux | grep [a]mazonScraper", shell=True))
        return 1
    except:
        return 0

def startFile():
    os.system("screen -S amazonScraper sudo python3 /home/pi/Documents/amazonScraper/amazonScraper.py")

while True:
    running = checkRunning()
    if running == 1:
        time.sleep(3600)
    else:
        startFile()