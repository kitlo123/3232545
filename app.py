import requests
import re
import random
import configparser
import twisted
import twisted.internet.protocol
import twisted.internet.reactor
from bs4 import BeautifulSoup
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
  
app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")

line_bot_api = LineBotApi(config['kit']['qut881@gmail.com'])
handler = WebhookHandler(config['kit']['12345678'])

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'

def weather():
   getPage("http://rss.weather.gov.hk/rss/CurrentWeather_big5.xml").addCallback(printPage)
   return content

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "weather":
        content = weather()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
   
if __name__ == '__main__':
    app.run()
