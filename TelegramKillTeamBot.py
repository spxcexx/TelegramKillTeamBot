import telebot
import os
import sqlite3
from dbfiles.dbktpy import *
from telebot import types

PATH = os.path.abspath(__file__ + "/.." + "/..")

bot = telebot.TeleBot("")
question_list = []
owner_id = 1109954939
keyboard = types.ReplyKeyboardMarkup(True)
btn1 = types.KeyboardButton('Связь с администрацией ❓')
btn2 = types.KeyboardButton('О боте 📋')
btn3 = types.KeyboardButton('Discord 📢')
btn4 = types.KeyboardButton('Профиль 👤')
btn5 = types.KeyboardButton('Команды 🔰')
keyboard.add(btn1, btn2)


#main commands
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,"Привет! Я - оффициальный бот KillTeam. Написан лично создателем. Чтобы узнать что я умею напиши: /help",reply_markup=keyboard)


@bot.message_handler(commands=["discord"])
def discord(message):
    bot.reply_to(message,'[KillTeam Discord](https://discord.gg/sPUSqXFt9f)', parse_mode='MarkdownV2')


@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(message, "Вот что я умею:\n1./discord - получение ссылки на оффициальный дискорд сервер\n2./questiontoadm - Вы можете задать вопрос к администрации бота. Оффтоп - бан на 2 часа.")




