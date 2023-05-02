import telebot
from Barcode_reader_4 import BarcodeReader
from Barcode_parcer import parcer
from glob import glob
# from telebot import types

bot = telebot.TeleBot('6287514662:AAE3MdW3tGaGWM79Zdt3RuXqSkFHMLsjk54')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет')
	
@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Я Вас не понимаю, пожалуйста, отправьте картинку для того чтобы проверить стоимость")

@bot.message_handler(commands=['button'])
def button_message(message):
	markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=telebot.types.KeyboardButton("Кнопка")
	bot.send_message(message.chat.id,'Сообщение для кнопки')
	markup.add(item1)	
	
@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_message(message.chat.id, 'Фото принято')
    with open("image.png", 'wb') as new_file:
        new_file.write(downloaded_file)
    image = glob("image.png")
    code = str(BarcodeReader(image[0])).strip("b'")
    answer = parcer(code)
    bot.send_message(message.chat.id, answer)
    

bot.infinity_polling()