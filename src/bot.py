import telebot
import os
from loguru import logger

bot = telebot.TeleBot(os.environ['nashenas_token'])

logger.info('Start bot')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	logger.info('somebody starts bot')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, str(eval(message.text)))


bot.infinity_polling()
logger.info('Done') 

class Bot:
















