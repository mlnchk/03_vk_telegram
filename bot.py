import json
import random
from telegram.ext import Updater, CommandHandler


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def news(bot, update):
    news_dict = json.load(open('news_base2.json'))
    new = news_dict[random.randint(0, len(news_dict))]
    text = '%s...\n\nhttps://vk.com/wall%s_%s' % (new['text'][0:100], new['owner_id'], new['id'])
    bot.sendMessage(chat_id=update.message.chat_id, text=text)


token = '344289277:AAFW7MqEyssWyinS39XuEJz8F2wjBfZJtqk'

updater = Updater(token=token)
dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

news_handler = CommandHandler('news', news)
dispatcher.add_handler(news_handler)
