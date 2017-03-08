import requests
import json
import random
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def message(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def news(bot, update):
    news_dict = json.load(open('news_base.json'))
    text = news_dict[random.randint(0, len(news_dict))]['text']
    bot.sendMessage(chat_id=update.message.chat_id, text=text)




token = '344289277:AAFW7MqEyssWyinS39XuEJz8F2wjBfZJtqk'
method = ''
url = 'https://api.telegram.org/bot' + token + method

updater = Updater(token=token)
dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

# echo_handler = MessageHandler(Filters.text, echo)
# dispatcher.add_handler(echo_handler)

message_handler = CommandHandler('message', message)
dispatcher.add_handler(message_handler)

news_handler = CommandHandler('news', news)
dispatcher.add_handler(news_handler)

