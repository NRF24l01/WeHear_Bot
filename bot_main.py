#Import telegramApi
try:
    from telebot import types
    import telebot
except:
    import pip
    pip.main(['install', 'PyTelegramBotAPI'])

#Import random
import random
from random import choice

#Import token (if you have error on this line, create teletoken.py and create label token like str)
try:
    from teletoken import token as tele_token
except:
    tele_token = input("Input token: ")

#Import config
import config

#Import sqllite for database
import sqlite3

#Import time lib
from datetime import datetime

bot = telebot.TeleBot(tele_token)

ks = telebot.types.ReplyKeyboardMarkup()
ks.row("💸Купить💸")
ks.row(" 🔎Информация 🔎", "☎️Звонок☎️")
ks.row("👽Профиль👽","👣Регистрация👣")
ks.row("☢Разработчкики☢️")

def get_data(arg):
    '''This function catch data by command.
    In arg you put text with command(/mnasd 20)
    This function return what user input(20)'''
    return arg.split()[1:]

def is_new(message):
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        current_datetime = datetime.now()
        hz = cursor.execute(f"SELECT hz FROM profiles WHERE id =='{str(message.from_user.id)}'")

        conn.commit()
    except sqlite3.Error as error:
        print("Error sql8: ", error)

    finally:
        if conn:
            conn.close()

    if len(hz)==0:
        return True
    else:
        return False

@bot.message_handler(commands=["mname"])
def mname(message):
    name = get_data(message.text, reply_markup=ks)



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, config.def_start, reply_markup=ks)

@bot.message_handler(content_types=["text"])
def text_f_u(message):
    user_id = message.from_user.username
    current_datetime = str(datetime.now())
    if not user_id:
        user_id = f"user_{random.randint(1, 1000)}"
    res = current_datetime + " " + user_id +" "+str(message.from_user.id)+ "  '" + message.text + "'"
    print(res)
    if message.text == "💸Купить💸":
        try:
            bot.send_photo(message.from_user.id, photo=open('money.jpg','rb'), caption=config.def_buy, reply_markup=ks)
        except:
            print("No such file: money.jpg")
    elif message.text == "👣Регистрация👣":
        bot.send_message(message.from_user.id, config.def_reg, reply_markup=ks)
    elif message.text == "☢Разработчкики☢️":
        bot.send_message(message.from_user.id, config.def_cr)
    elif message.text == "🔎Информация 🔎":
        bot.send_message(message.from_user.id, config.def_info, reply_markup=ks)

bot.polling(none_stop=True,non_stop=True)