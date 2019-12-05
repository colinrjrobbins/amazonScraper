# code name: amazonScraperClass.py
# creator: Colin Robbins
# date started: 2019-12-04
# date previously edited: 2019-12-04
# purpose: To scan amazon for the given product and send me an email if it notices the
#          price drop.

# generalized imports
import datetime as dt
import time
import os

# imports for web parsing
from bs4 import BeautifulSoup
import requests

class amazonScraper():
    def __init__(self):
        self.URL = 'https://www.amazon.ca/gp/product/B07RS512XL?pf_rd_p=46535598-d2e0-4bc4-8392-182d8c1e93fc&pf_rd_r=YDTVGVF57RWYKZKQDVNA'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
        self.comparePrice = 453.19
        self.logFile = open("logFile.txt","w")
        self.errorLog = open("errorLog.txt","w")
        
    def timeCheck(self):
        print("Waiting...")
        time.sleep(10)
        
    def pageGather(self):
        self.page = requests.get(self.URL,
                                 headers=self.header)
        self.status = self.page.status_code
        
    def currentTime(self):
        self.current = dt.datetime.now()
        
    def informationGrab(self):
        if self.status == 200:
            try:
                self.page_decode = self.page.content.decode('utf-8')
                self.soup = BeautifulSoup(self.page_decode,
                                          'lxml')
            except Exception as e:
                print("\nError occured at {0}: {1}\n".format(str(self.current),str(e)))
                self.errorLog.write("\n"+ str(self.current)+": "+str(e)+"\n")
                
            try:
                self.title = self.soup.find(id="productTitle").get_text().strip().split()
                self.titleFinal = " ".join(self.title[0:3])
                self.price = self.soup.find(id="priceblock_ourprice").get_text()
                self.floatPrice = float(self.price[5:11])
                self.percentDown = (((self.comparePrice / self.floatPrice) - 1) * 100)
                self.formattedPercent = float("%2f" % round(self.percentDown,2))
            except Exception as e:
                print("\nError occured at {0}: {1}\n".format(str(self.current),str(e)))
                self.errorLog.write("\n" + str(self.current) + ": " + str(e)+ "\n")
        else:
            print("Error Connecting to Amazon.")
            self.errorLog.write("\nInternet Error Code " + self.status + ": Amazon Connection unavailable.\n")
    
    def checkData(self):
        if self.formattedPercent >= 10.00:
            try:
                r = requests.post('https://maker.ifttt.com/trigger/price_change/with/key/mFJcPs0GfZCjSl6uFLKED3PYPvbt3zrJ6zRgrDR9ZvS',
                                    params={"value1":self.titleFinal,
                                            "value2":self.price,
                                            "value3":str(self.formattedPercent)})
                self.comparePrice = self.floatPrice
                self.success = 1
            except Exception as e:
                self.success = 0
                print("\nError occured at {0}: {1}\n".format(str(self.current),str(e)))
                self.errorLog.write("\n" + str(self.current) + ": " + str(e)+ "\n")
                
    def saveToFile(self):
        if self.success == 1:
            print("Gather Successful. Saved to log file.")
            self.logFile.write("\nGather success {0}:\nProduct Name: {1}\nCurrent Price: {2}\nPercent Off: {3}\n".format(str(currentTime),titleFinal,str(price),str(formattedPercent)))
            self.logFile.close()
            os.system("sudo cp -rf /home/pi/Documents/amazonScraper/logFile.txt /home/pi/")
        else:
            print("Gather Unsuccessful. Trying again.")
    