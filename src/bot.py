import telebot
import os
from loguru import logger


class Bot:
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['nashenas_bot_Token'])
		self.echo_all=self.bot.message_handler(func=lambda message: True)(self.echo_all)
		self.send_welcome=self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)


	def send_welcome(self,message):
		self.bot.reply_to(message, "Howdy, how are you doing?")
		logger.info('somebody starts bot')
	
	def echo_all(self,message):
		self.bot.reply_to(message, (message.text))


	def run(self):
		logger.info('Start bot')
		self.bot.infinity_polling()
		logger.info('Done') 	


mybot=Bot()
mybot.run()





