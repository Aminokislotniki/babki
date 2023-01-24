from telebot.types import ReplyKeyboardRemove, InputMediaPhoto
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot('5683069905:AAHpxtupIwvp19ybNfh0Gn2FbPVMEbKzKbs')
id_chanel = "@sandbox_chanell"
from keyboards import stavka
import json


def post_lots(id_lot):

    f = open('lots/'+str(id_lot)+'.json', 'r', encoding='utf-8')
    dict_lot = json.loads(f.read())
    f.close()
    buf=''
    for x in dict_lot:
        print(x)
        if x=='lot_name':
            buf+=(dict_lot[x])+"\n"
        if x=="description":
            buf+=(dict_lot[x])+"\n"
        if x=="price":
            buf+='Цена '+(dict_lot[x])

    print(buf)
    return buf



