#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
# import logging
import os
import pyperclip
import re
import webbrowser
# from concurrent.futures import ThreadPoolExecutor
# executor = ThreadPoolExecutor(max_workers=4)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Handler
from telegram.ext.dispatcher import run_async
# Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

# logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in
# error.
@run_async
def getMessage(update, context):
    if update.message.text:
        messages = update.message.text
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        url = re.findall(pattern,messages)

        if url:
            webbrowser.open_new_tab(url[0])
        else:
            pyperclip.copy(messages)

    elif update.message.photo:
        fileId = update.message.photo[-1].file_id
        newFile = context.bot.get_file(fileId)
        newFile.download('/tmp/fromiPhone.png')
        os.popen('xclip -selection clipboard -t image/png -i /tmp/fromiPhone.png')

    elif update.message.document:
        fileId = update.message.document.file_id
        newFile = context.bot.get_file(fileId)
        newFile.download('/home/yang/Downloads/'+ update.message.document.file_name)

    else:
        pass

# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    REQUEST_KWARGS = {'proxy_url': 'http://127.0.0.1:7890'}
    TOKEN = "xxxx:xxxxxx"
    updater = Updater(TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # dp.add_error_handler(error)

    dp.add_handler(MessageHandler(Filters.photo | Filters.text | Filters.document, getMessage))

    #sendMessage(dpBot,owner_chat_id)
    updater.start_polling()

if __name__ == '__main__':
    main()
