#Import telegramApi
import telebot
from telebot import types

#Import random
import random
from random import choice

#Import token (if you have error on this line, create teletoken.py and create label token like str)
from teletoken import token as tele_token

#Import config
import config

#Import sqllite for database
import sqlite3

#Import time lib
from datetime import datetime

bot = telebot.TeleBot(tele_token)

ks = telebot.types.ReplyKeyboardMarkup()
ks.row(" 🔎Информация 🔎", "☎️Звонок☎️")
ks.row("👽Профиль👽","👣Регистрация👣")
ks.row("💸Купить💸")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, config.def_start, reply_markup=ks)

@bot.message_handler(content_types=["text"])
def text_f_u(message):
    user_id = message.from_user.username
    current_datetime = str(datetime.now())
    if not user_id:
        user_id = f"user_{random.randint(1, 1000)}"
    res = current_datetime + " " + user_id + "  '" + message.text + "'"
    print(res)
    if message.text == "💸Купить💸":
        bot.send_photo(message.from_user.id, photo=open('money.jpg','rb'), caption=config.def_buy)
    elif message.text == "👣Регистрация👣":
        bot.send_message(message.from_user.id, config.def_reg)

bot.polling(none_stop=True,non_stop=True)