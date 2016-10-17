#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from Database import Database

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

msg_db = Database()

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def like(bot, update):
    msg_db.insert(update.message)
    bot.sendMessage(update.message.chat_id, text=msg_db.getStr(update.message))

def getTopLiked(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text=msg_db.getTopNStr(chat_id, 10))

def getTopN(bot, update):
    # Should make this more robust
    num_top = update.message.text.split()[1]
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, text=msg_db.getTopNStr(chat_id, num_top))

def checkArgs(args, type_args):
    if(len(args) == len(type_args)):
        return "Use of topN: \"/topn [number]\""

def main():
    with open("botCode.txt", "r") as f:
        lines = f.readlines()

    api_token = lines[0].rstrip('\n')

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(api_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("l", like))
    dp.add_handler(CommandHandler("top", getTopLiked))
    dp.add_handler(CommandHandler("topn", getTopN))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
