import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
import gspread
import time
from fuzzywuzzy import process

bot = telebot.TeleBot('5683069905:AAGVpQBnaKoilz2UYWK1Ug3XoAENmDsTUyc');


def dt(s):
    s = s[1:]
    return s

def fs(st):
    return(st[0])
#ssss