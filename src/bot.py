import telebot
import os
from loguru import logger
from src.utils.io import write_json



class Bot:
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['nashenas_bot_Token'])
		logger.info('Start Bot ..')

		self.send_welcome=self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
		self.echo_all=self.bot.message_handler(func=lambda message: True)(self.echo_all)
		


	def send_welcome(self,message):
		self.bot.reply_to(message, "Howdy, how are you doing?")
		logger.info('somebody starts bot')
	
	def echo_all(self,message):
		write_json(message.json, 'data.json')
		self.bot.reply_to(message, (message.text))


	def run(self):
		logger.info('Running Bot...')
		self.bot.infinity_polling()
		
		 	
if __name__ == '__main__':


    mybot=Bot()
    mybot.run()





