#Import telegramApi
import telebot
from telebot import types

#Import random
from random import choice

#Import token (if you have error on this line, create token.py and create label token like str)
from token import token

#Import sqllite for database
import sqlite3

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message()