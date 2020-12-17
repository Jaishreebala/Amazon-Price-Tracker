# # import bs4
# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup

# myURL = "https://www.newegg.ca/p/pl?d=graphics+card"

# # Openning up connection, grabbing the page
# uClient = uReq(myURL)
# htmlContent = uClient.read()
# uClient.close()

import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os
from dotenv import load_dotenv
load_dotenv()


URL = "https://www.amazon.com/Apple-AirPods-Charging-Case-Renewed/dp/B07SKLLYTW/ref=sr_1_6?dchild=1&keywords=airpods&qid=1604272769&sr=8-6"
headers = {"user-agent": os.getenv('USER_AGENT')}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_ourprice").get_text().strip()
itemFound = False


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("jeezricodes@gmail.com", os.getenv('HASH'))

    subject = "Hello Cheap Human! The price has fallen down to your cheap standards!"
    body = "Here is the link to your product: {} \n Enjoy Being Cheap, Child!".format(
        URL)
    msg = "Subject: {}\n\n{}".format(subject, body)
    server.sendmail(
        'jeezricodes@gmail.com', 'jeezricodes@gmail.com', msg
    )
    print("Hello Cheap Human! The price has lowered")
    server.quit()


def checkPrice():
    global itemFound
    priceInNumeric = float(price[1:])
    print("checking price")
    if(priceInNumeric < 100):
        sendMail()
        itemFound = True


while(not itemFound):
    checkPrice()
    time.sleep(86400)
