#!/usr/bin/python
# coding:utf-8

# TelegramBotWeb - main.py
# 2018/9/26 16:54

__author__ = "WangYuan <owensnow@qq.com>"

import telebot
from bot1.models import ToDoList
import logging
import time

telebot.logger.setLevel(logging.DEBUG)

#API_TOKEN = '670941114:AAHBBrx7ke3b45VYXI3dApazyBmpXyY53qE'
API_TOKEN = '756612443:AAEWZTUkf_JvuA4DvJ4h81Npg7FXgjQBbgs'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, bro...")


@bot.message_handler(commands=['list'])
def send_welcome(message):
    name = extract_unique_code1(message.text)
    print(name)
    bot.send_message(message.chat.id, "coming ASAP...")


@bot.message_handler(commands=['todo'])
def send_welcome(message):
    name = extract_unique_code1(message.text)
    context = extract_unique_code2(message.text)
    print(name)
    print(context)
    tdL = ToDoList()
    tdL.name = name
    tdL.context = context
    tdL.createdTime = time.time()
    tdL.save()
    bot.send_message(message.chat.id, "had record your todoList.You can input /list to check ")


@bot.message_handler()
def echo(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='what can i for u...')


def extract_unique_code1(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1]


def extract_unique_code2(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[2]


def extract_unique_code3(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[3]


if __name__ == '__main__':
    bot.polling()

