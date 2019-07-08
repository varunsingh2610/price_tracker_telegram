#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as soup
def telegramBot(message):
"""
Function to send message in telegram.
You are required write bot_token and bot_chatID below. Which you will get from telegram app itself to get the message.
"""
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + \
        bot_chatID + '&parse_mode=Markdown&text=' + message

    response = requests.get(send_text)
    return response.json()



"""
Price Traker for OnePlus 7 in Amazon.in
"""
# I have used Oneplus 7 URL.
onplus_7 = 'https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
page = requests.get(onplus_7, headers=headers)
html = soup(page.content, "lxml")

title = html.find(id="productTitle").getText().strip()
price = html.find(id='priceblock_dealprice').getText()
if float(price.strip('₹ ').replace(',','')) < 32999: # This will send the price with URL if price drops below 32999
    telegramBot("Price drop!")
    telegramBot(title+" "+price+" "+onplus_7)
else:
    telegramBot(title+" "+price) # Only Product name and price if the price is not less than 32999
