from telebot.types import ReplyKeyboardRemove, InputMediaPhoto
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot('5683069905:AAHpxtupIwvp19ybNfh0Gn2FbPVMEbKzKbs')
id_chanel = "@sandbox_chanell"
from keyboards import stavka
import json

f = open('lots/3.json', 'r', encoding='utf-8')
dict_lot = json.loads(f.read())
f.close()

bot.send_message(id_chanel," ")
print(data)
print(dict_lot)
def post_lots(dict_lot):
    photo1=""
    buf=''
    for x in dict_lot:
        if x=='lot_name':
            buf+=(dict_lot[x])+"\n"
        if x=="description":
            buf+=(dict_lot[x])+"\n"
        if x=="price":
            buf+='Цена '+(dict_lot[x])
        if x == 'photo':
            photo1=x
    print(buf)
    bot.send_photo(id_chanel,buf, photo1)


post_lots(dict_lot)



