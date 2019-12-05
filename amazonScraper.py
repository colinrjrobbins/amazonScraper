# code name: amazonScraper.py
# creator: Colin Robbins
# date started: 2019-10-30
# date previously edited: 2019-11-16
# purpose: To scan amazon for the given product and send me an email if it notices the
#          price drop.

# generalized imports
# import datetime as dt
# import time
# import os

# # imports for web parsing
# from bs4 import BeautifulSoup
# import requests

import amazonScraperClass
from amazonScraperClass import amazonScraper as AmS

# # FUNCTIONS
# def timeCheck():
#     print("Waiting...")
#     while True:
#         # hold for 15 minutes.
#         time.sleep(900)

# # URL used for the amazon product
# URL = 'https://www.amazon.ca/gp/product/B07RS512XL?pf_rd_p=46535598-d2e0-4bc4-8392-182d8c1e93fc&pf_rd_r=YDTVGVF57RWYKZKQDVNA'
# # used to avoid cookie data and to verify your a human being
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

# # Generalized holding variables
# comparePrice = 453.19

# while True:
#     logFile = open("logFile.txt","w")
#     timeCheck()
#     # gather the amazon page as HTML code with a GET protocol
#     page = requests.get(URL,headers=header)

#     # check to make sure it is successfully connected
#     status = page.status_code
    
#     # gather current Date and time for the log file
#     currentTime = dt.datetime.now()

#     # check to make sure it was a success or display an error.
#     if status == 200:
#         try:
#             # decode the page and prepare it for reading
#             page_decode = page.content.decode('utf-8')
#             # using lxml instead of html parser
#             soup = BeautifulSoup(page_decode, "lxml")
#         except Exception as e:
#             print("\nError occured at {0}: {1}\n".format(str(currentTime), str(e)))
#             logFile.write("\n" + str(e) + "\n")
#         try:
#             # finding the product title
#             title = soup.find(id="productTitle").get_text().strip().split()
#             # formatting the title for the first few words to get the idea
#             titleFinal = " ".join(title[0:3])
#             # finding the price of the product
#             price = soup.find(id="priceblock_ourprice").get_text()
#             # printing the name and the price.
#             floatPrice = float(price[5:11])
#             # calculating the price difference
#             percentDown = ((comparePrice / floatPrice) - 1) * 100
#             # format the percent so it tells you the difference
#             formattedPercent = float("%.2f" % round(percentDown,2))
#             # if the gathered value is less then the last value check and send text
#         except Exception as e:
#             print("\nError occured at {0}: {1}\n".format(str(currentTime), str(e)))
#             logFile.write("\n" + str(e) + "\n")
#         try:    
#             if formattedPercent >= 10.00:
#                 r = requests.post('https://maker.ifttt.com/trigger/price_change/with/key/mFJcPs0GfZCjSl6uFLKED3PYPvbt3zrJ6zRgrDR9ZvS',
#                                 params={
#                                     "value1":titleFinal,
#                                     "value2":price,
#                                     "value3":str(formattedPercent)})
#             comparePrice = floatPrice
#         except Exception as e:
#             print("\nError occured at {0}: {1}\n".format(str(currentTime), str(e)))
#             logFile.write("\n" + str(e) + "\n")
            
#         print("Gather Successful. Saved to log file.")
#         logFile.write("\nGather success {0}:\nProduct Name: {1}\nCurrent Price: {2}\nPercent Off: {3}\n".format(str(currentTime),titleFinal,str(price),str(formattedPercent)))
#         logFile.close()
#         os.system("sudo cp -rf /home/pi/Documents/amazonScraper/logFile.txt /home/pi/")
#     else:
#         print("Error connecting to Amazon.")
#         logFile.write("\nInternet Error, Amazon Connection unavailable.\n")

testCheck = AmS()

while True:
    testCheck.currentTime()
    testCheck.pageGather()
    testCheck.informationGrab()
    holdReturn = testCheck.checkData()
    if holdReturn == 1:
        testCheck.saveToFile()
    else:
        print("No change in price.")
    testCheck.timeCheck()
