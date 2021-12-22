import telebot
import os
from loguru import logger

bot = telebot.TeleBot(os.environ['nashenas_token'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

logger.info('Start bot')
bot.infinity_polling()
logger.info('Done') 

