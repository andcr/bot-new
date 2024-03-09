import telebot
from telebot import types
import requests


bot = telebot.TeleBot("5090893413:AAEQNEFhqprBxqKExGQ0BjhhF_o4BFfkXlw")

users = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    if(chat_id in users):
        bot.send_message(chat_id, "Qaytganingizdan hursandmiz")
    else:
        users.append(chat_id)
        bot.send_message(chat_id, "Assalomu alaykum")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    chat_id = message.chat.id

    print(chat_id, message.from_user.username, text)

    if(text=="salom"):
        bot.send_message(chat_id, "Asalomu alaykum")
    elif(text=="/users"):
        bot.send_message(chat_id, str(len(users)))
    elif(text.startswith("/echo")):
        # /echo funkisyasini kiritgandan keyin soz yozing
        data = text.split(" ", 1)[1]
        bot.send_message(chat_id, data)
    elif(text=="/menu"):
        markup = types.ReplyKeyboardMarkup()
        itembtn1 = types.KeyboardButton('Adminga murojat qilish')
        itembtn2 = types.KeyboardButton('funksiyalar')
        itembtn3 = types.KeyboardButton('Admin haqida malumot')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(chat_id, "Funksiyani tanlang: ", reply_markup=markup)
    elif(text=="Adminga murojat qilish"):
        bot.send_message(chat_id, "manamunga murojat qiling: @uzb_proger10", reply_markup=types.ReplyKeyboardRemove())
    elif(text=="funksiyalar"):
        markup = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, "hozircha bizda funksiya yo'q(", reply_markup=markup)
    elif(text=="Admin haqida malumot"):
        bot.send_message(chat_id, "men Fatxulla Ibrohim 2010 yil 1 august kunida tug'ilganman hozirda Python va django dasturlash tillarini organyabman", reply_markup=types.ReplyKeyboardRemove())
    elif(text=="/message"):
        bot.send_message(chat_id, str(message))
    elif(text=="ism"):
        bot.send_message(chat_id, "@" + message.from_user.username)
    elif(text=="/admin"):
        bot.send_message(chat_id, "manamunga murojat qiling: @uzb_proger10")
    elif(text=="/id"):
        bot.send_message(chat_id, str(chat_id))
    # elif(text=="cat"):
    #     data = requests.get("https://aws.random.cat/meow").json()
    #     url = data["file"]
    #     bot.send_photo(chat_id, url)

bot.infinity_polling()