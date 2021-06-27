import telegram
from telegram import bot
from telegram.ext import Updater, CommandHandler

bot = telegram.Bot(token='1773620815:AAG8Zc7VHs-nADqoud0FTTUqbHSTR3EISz8')
updater = Updater(bot=bot, use_context=True)


def startTelegramBot():
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def sendMessage(message):
    bot.send_message(chat_id=1745224096, text=message)
