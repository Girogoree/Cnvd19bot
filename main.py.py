import telebot
from selenium import webdriver

token = '1038340873:AAFtHsBjjEnTNHIv51AJmuy7a2tB02hUlcc'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['info'])
def info(message):
	driver = webdriver.Chrome()
	driver.get('https://coronavirus.zone/')
	result = driver.find_element_by_tag_name('tbody')
	bot.send_message(message.chat.id, result.text)





bot.polling(none_stop=True)