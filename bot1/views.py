# -*- coding: utf-8 -*-
from django.shortcuts import render
import telebot
from bot1.models import ToDoList
import logging
import time

telebot.logger.setLevel(logging.DEBUG)

API_TOKEN = '756612443:AAEWZTUkf_JvuA4DvJ4h81Npg7FXgjQBbgs'
bot = telebot.TeleBot(API_TOKEN)


