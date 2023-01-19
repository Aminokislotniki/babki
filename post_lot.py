from telebot.types import ReplyKeyboardRemove, InputMediaPhoto
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot('5683069905:AAGVpQBnaKoilz2UYWK1Ug3XoAENmDsTUyc')
id_chanel = "@sandbox_chanell"
from keyboards import stavka
import json

f = open('lots/1.json', 'r', encoding='utf-8')
dict_lot = json.loads(f.read())
f.close()


def post_lot(dict_lot,message):
    buf=''
    for x in dict_lot:
        if x=='lot_name':
            buf+=(dict_lot[x])+"\n"
        if x=="descripchion":
            buf+=(dict_lot[x])+"\n"
        if x=="price":
            buf+='Цена '+(dict_lot[x])
    print(buf)
    bot.send_message(message.chat.id, buf, reply_markup=stavka(list))



post_lot(dict_lot)