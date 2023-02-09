import time

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
from config import data_base as dtname

#Import sqllite for database
import sqlite3

#Import time lib
from datetime import datetime

import hashlib

import multiprocessing
print("Number of cpu : ", multiprocessing.cpu_count())
from multiprocessing import Process

bot = telebot.TeleBot(tele_token)

ks = telebot.types.ReplyKeyboardMarkup()
ks.row("💸Купить💸")
ks.row(" 🔎Информация 🔎", "☎️Звонок☎️")
ks.row("👽Профиль👽","👣Регистрация👣")
ks.row("☢Разработчкики☢️")

def status_ch(message, txt):
    try:
        conn = sqlite3.connect(dtname)
        cursor = conn.cursor()

        cursor.execute(f"UPDATE profiles SET status = '{str(txt)}' WHERE user_id =='{str(message.from_user.id)}'")
        conn.commit()
    except sqlite3.Error as error:
        print("Error sql2: ", error)

    finally:
        if conn:
            conn.close()

def level_get(message):
    try:
        conn = sqlite3.connect(dtname)
        cursor = conn.cursor()

        st = cursor.execute(f"SELECT levelOFbuy FROM profiles WHERE user_id =='{str(message.from_user.id)}'").fetchall()[0][0]

        conn.commit()
    except sqlite3.Error as error:
        print("Error sql2: ", error)

    finally:
        if conn:
            conn.close()
    return st

def status_get(message):
    try:
        conn = sqlite3.connect(dtname)
        cursor = conn.cursor()

        st = cursor.execute(f"SELECT status FROM profiles WHERE user_id =='{str(message.from_user.id)}'").fetchall()[0][0]

        conn.commit()
    except sqlite3.Error as error:
        print("Error sql2: ", error)

    finally:
        if conn:
            conn.close()
    return st

def new_user(message):
    if is_new(message):
        try:
            conn = sqlite3.connect(dtname)
            cursor = conn.cursor()

            current_datetime = datetime.now()
            hz = cursor.execute(f"INSERT INTO profiles (user_id, user_name, nasu, name, status, age, hz, levelOFbuy, voiceN)"
                                f" VALUES('{str(message.from_user.id)}', '{message.from_user.username}', 'None', 'None',"
                                f"'None', '100', '27', '1','1')")

            conn.commit()
        except sqlite3.Error as error:
            print("Error sql1: ", error)

        finally:
            if conn:
                conn.close()

def get_data(arg):
    '''This function catch data by command.
    In arg you put text with command(/mnasd 20)
    This function return what user input(20)'''
    return arg.split()[1:]

def is_new(message):
    try:
        conn = sqlite3.connect(dtname)
        cursor = conn.cursor()

        hz = cursor.execute(f"SELECT hz FROM profiles WHERE user_id =='{str(message.from_user.id)}'").fetchall()

        conn.commit()
    except sqlite3.Error as error:
        print("Error sql2: ", error)

    finally:
        if conn:
            conn.close()
    if len(hz)==0:
        return True
    else:
        return False

def voice():
    while True:
        print("sad")
        time.sleep(1)


@bot.message_handler(commands=["chvoice"])
def chvoice(message):
    new_user(message)
    bot.send_message(message.from_user.id, "Выберите голос. Отправте номер голоса который вам понравился.")
    audio = open('speakers/aidar.wav', 'rb')
    bot.send_voice(message.from_user.id, audio, '1️⃣  Голос')
    audio.close()
    audio = open('speakers/baya.wav', 'rb')
    bot.send_voice(message.from_user.id, audio, '3️⃣  Голос')
    audio.close()
    audio = open('speakers/eugene.wav', 'rb')
    bot.send_voice(message.from_user.id, audio, '4️⃣  Голос')
    audio.close()
    audio = open('speakers/kseniya.wav', 'rb')
    bot.send_voice(message.from_user.id, audio, '5️⃣  Голос')
    audio.close()
    audio = open('speakers/xenia.wav', 'rb')
    bot.send_voice(message.from_user.id, audio, '6️⃣  Голос')
    audio.close()
    status_ch(message, "chvoice")
@bot.message_handler(commands=["mage"])
def mfio(message):
    new_user(message)
    age = get_data(message.text)
    try:
        age = int(age[0])
        try:
            conn = sqlite3.connect(dtname)
            cursor = conn.cursor()

            current_datetime = datetime.now()
            hz = cursor.execute(
                f"UPDATE profiles SET age = '{str(age)}' WHERE user_id == '{str(message.from_user.id)}'").fetchall()

            conn.commit()
            bot.send_message(message.from_user.id, "Возраст изменён")
        except sqlite3.Error as error:
            print("Error sql5: ", error)

        finally:
            if conn:
                conn.close()
    except:
        bot.send_message(message.from_user.id, "Попробуйте снова.")
@bot.message_handler(commands=["mfio"])
def mfio(message):
    new_user(message)
    fio = get_data(message.text)
    try:
        conn = sqlite3.connect(dtname)
        cursor = conn.cursor()

        current_datetime = datetime.now()
        hz = cursor.execute(
            f"UPDATE profiles SET nasu = '{' '.join(fio)}' WHERE user_id == '{str(message.from_user.id)}'").fetchall()

        conn.commit()
        bot.send_message(message.from_user.id, "ФИО изменена")
    except sqlite3.Error as error:
        print("Error sql3: ", error)

    finally:
        if conn:
            conn.close()

@bot.message_handler(commands=["mname"])
def mname(message):
    new_user(message)
    #print("h")
    name = get_data(message.text)
    try:
        conn = sqlite3.connect(dtname)
        cursor = conn.cursor()

        current_datetime = datetime.now()
        hz = cursor.execute(f"UPDATE profiles SET name = '{' '.join(name)}' WHERE user_id == '{str(message.from_user.id)}'").fetchall()

        conn.commit()
        bot.send_message(message.from_user.id, "Имя изменено")
    except sqlite3.Error as error:
        print("Error sql4: ", error)

    finally:
        if conn:
            conn.close()



@bot.message_handler(commands=["start"])
def start(message):
    new_user(message)
    bot.send_message(message.chat.id, config.def_start, reply_markup=ks)

@bot.message_handler(content_types=["text"])
def text_f_u(message):
    new_user(message)
    user_id = message.from_user.username
    current_datetime = str(datetime.now())
    if not user_id:
        user_id = f"user_{random.randint(1, 1000)}"
    res = current_datetime + " " + user_id +" "+str(message.from_user.id)+ "  '" + message.text + "'"
    print(res)
    if status_get(message) != 'chvoice':
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
        elif message.text == "☎️Звонок☎️":
            if level_get(message)==1:
                bot.send_message(message.from_user.id, "Отправляйте мне текст. Когда закончите отправте /stop", reply_markup=ks)
                status_ch(message, "lvl1")
    elif status_get(message) == 'chvoice':
        try:
            voice = int(message.text)
            if voice > 0 and voice < 7:
                bot.send_message(message.from_user.id, 'Голос изменён.')
                try:
                    conn = sqlite3.connect(dtname)
                    cursor = conn.cursor()

                    current_datetime = datetime.now()
                    hz = cursor.execute(f"UPDATE profiles SET voiceN = '{voice}' WHERE user_id == '{str(message.from_user.id)}'").fetchall()

                    conn.commit()
                except sqlite3.Error as error:
                    print("Error sql4: ", error)

                finally:
                    if conn:
                        conn.close()
            else:
                bot.send_message(message.from_user.id,
                                 'Попробуйте ещё раз. (Отправте только цифру от 1 до 6 включительно)')
            status_ch(message, "None")
        except:
            bot.send_message(message.from_user.id, 'Попробуйте ещё раз. (Отправте только цифру от 1 до 6 включительно)')
    elif status_get(message) == "lvl1":
        with open('vords.txt', 'r', encoding="UTF-8") as v:
            has = v.split('\n')
            ha = choice(has)
            nam = hashlib.sha1(ha.encoding()).hexdigest()
        try:
            conn = sqlite3.connect(dtname)
            cursor = conn.cursor()

            cursor.execute(f"INCERT INTO tts (us_id, txt, status, voice, file_name) VALUES ('{str(message.from_user.id)}', '{message.text}', 'go', '{nam}')").fetchall()

            conn.commit()
        except sqlite3.Error as error:
            print("Error sql4: ", error)

        finally:
            if conn:
                conn.close()
        hhh = Process(target=voice)
        hhh.start()

bot.polling(none_stop=True,non_stop=True)