import json
import random
from main import write_to_file, make_news_list
from telegram.ext import Updater, CommandHandler

print('enter your token for start your bot')
token = input()


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def news(bot, update):
    api_url = 'https://api.vk.com/method/'
    write_to_file(make_news_list(api_url))
    news_dict = json.load(open('news_base.json'))
    new = news_dict[random.randint(0, len(news_dict))]
    text = '%s...\n\nhttps://vk.com/wall%s_%s' % (new['text'][0:100], new['owner_id'], new['id'])
    bot.sendMessage(chat_id=update.message.chat_id, text=text)


updater = Updater(token=token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

news_handler = CommandHandler('python_news', news)
dispatcher.add_handler(news_handler)

print('go to your bot page and type /python_news')
