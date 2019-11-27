# Generalized imports
import subprocess
import os
import time
import datetime

def checkRunning():
    try:
        output = str(subprocess.check_output("ps aux | grep [a]mazonScraper", shell=True))
        return 1
    except:
        return 0

def startFile():
    print("Starting Scraper...")
    os.system("sudo python3 /home/pi/Documents/amazonScraper/amazonScraper.py")

while True:
    dt = datetime.datetime.now()
    running = checkRunning()
    if running == 1:
        print(str(dt) + ": Waiting for 1 hour...")
        time.sleep(3600)
    else:
        startFile()