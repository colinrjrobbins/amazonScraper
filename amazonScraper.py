# code name: amazonScraper.py
# creator: Colin Robbins
# date started: 2019-10-30
# date previously edited: 2019-12-07
# purpose: To scan amazon for the given product and send me an email if it notices the
#          price drop.

import amazonScraperClass
from amazonScraperClass import amazonScraper as AmS

testCheck = AmS()

while True:
    print("Grabbing current time...")
    testCheck.currentTime()
    print("Opening log files...")
    testCheck.fileOpener()
    print("Gathering product information...")
    testCheck.pageGather()
    print("Sparsing through data...")
    testCheck.informationGrab()
    print("Checking Data...")
    testCheck.checkData()
    print("Saving to file...")
    testCheck.saveToFile()
    testCheck.timeCheck()
