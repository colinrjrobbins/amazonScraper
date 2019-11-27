# Generalized imports
import subprocess
import os
import time
import datetime

def killPrevious():
	output = "1"

	while output != "":
		try:
			output = str(subprocess.check_output("ps aux | grep [a]mazonScraper", shell=True))
			
			hold = output.split()
			print("Preparing to kill process ID: "+hold[1])
			subprocess.Popen('sudo kill {0}'.format(hold[1]),shell=True)
			time.sleep(5)
		except:
			break

	print("\n<xxxxx   AmazonScraper successfully killed.   xxxxx>")
	time.sleep(1)

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
    killPrevious()
    running = checkRunning()
    if running == 1:
        print(str(dt) + ": Waiting for 1 hour...")
        time.sleep(3600)
    else:
        startFile()