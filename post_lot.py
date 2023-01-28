from telebot.types import ReplyKeyboardRemove, InputMediaPhoto
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot('5683069905:AAHpxtupIwvp19ybNfh0Gn2FbPVMEbKzKbs')
id_chanel = "@sandbox_chanell"
#from keyboards import stavka_canal
import json


def post_lots(id_lot):
    f = open('lots/'+str(id_lot)+'.json', 'r', encoding='utf-8')
    dict_lot = json.loads(f.read())
    f.close()
    buf=''
    photo=""
    min_stavka=''
    times=''
    start_price=''
    for z in dict_lot:
        for x in dict_lot[z]:
            if x=='lot_name':
                buf+=(dict_lot[z][x])+"\n"
            if x=="description":
                buf+=(dict_lot[z][x])+"\n"
            if x=="start_price" and z=="lot_info":
                buf+='Цена:'+str(dict_lot[z][x])
            if x=="photo":
                photo=(dict_lot[z][x])
            if x=="min_stavka":
                min_stavka=dict_lot[z][x]
            if x=="time_create":
                times=dict_lot[z][x]
            if x=="start_price":
                start_price=dict_lot[z][x]

    print(photo,min_stavka)
    return buf,photo,times,min_stavka,start_price



