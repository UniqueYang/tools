#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import requests
import pyperclip
from telegram.ext import Updater

def send_message():
    REQUEST_KWARGS = {'proxy_url': 'http://127.0.0.1:7890'}
    owner_chat_id = xxxxxxxxx
    TOKEN = "xxx:xxxxxx"
    updater = Updater(TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    bot = dp.bot
    # url = "https://api.telegram.org/bot%s/sendMessage" % config.TOKEN
    # proxies = {'http': 'http://localhost:7890'}
    target = os.popen('xclip -o -target TARGETS -selection clipboard')
    st = target.read()
    searchObj = re.search( r'image', st)
    if searchObj:
        os.popen('xclip -selection clipboard -t image/png -o > /tmp/toiPhone.png')
        bot.send_photo(chat_id=owner_chat_id, photo=open('/tmp/toiPhone.png', 'rb'))
    else:
        file = re.match(r'file://(.*)', pyperclip.paste())
        if file:
            images = re.match(r'file://(.*).png', pyperclip.paste())
            if images:
                imagepath =images.group(1) + '.png'
                bot.send_photo(chat_id=owner_chat_id, photo=open(imagepath, 'rb'))
            else:
                bot.send_document(chat_id=owner_chat_id, document=open(file.group(1), 'rb'))
        else:
            os.popen('xclip -selection clipboard -o > /tmp/toiPhone.txt')
            f = open("/tmp/toiPhone.txt")
            lines = f.read()
            bot.send_message(chat_id=owner_chat_id, text=lines)


if __name__ == '__main__':
    send_message()
