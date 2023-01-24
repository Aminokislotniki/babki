import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
import gspread
import time
from datetime import datetime, timedelta
from services_func import check_is_ban
from fuzzywuzzy import process
print(int(time.time()))
bot = telebot.TeleBot();
id_chanel = "@sandbox_chanell"
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



def dt(s):
    s = s[2:]
    return s

def fs(st):
    return(st[0:2])

list = ["+10","+20","+30","+40", "+50","+60"]

def stavka(list):
    stavka_keyboard = InlineKeyboardMarkup()

    button_list = [InlineKeyboardButton(text=x, callback_data="lf") for x in list]
    button_one = (InlineKeyboardButton("старт", callback_data="ls"))
    button_two = (InlineKeyboardButton("автоставка", callback_data="la" ))
    button_tree = (InlineKeyboardButton("Отменить", callback_data="lb"))
    button_four = (InlineKeyboardButton("время", callback_data="lt" ))
    button_five = (InlineKeyboardButton("Информация", callback_data="li"))

    stavka_keyboard.add(*button_list, button_one,button_two,button_tree,button_four,button_five)
    return stavka_keyboard
def information(call_id):
    bot.answer_callback_query(call_id, "Ставку можно отменить в течении 1 минуты, нажав на кнопку Отмена."
                                       "Выигранный лот необходимо выкупить в течении 5 дней, в противном случае БАН на 5 дней!!!", show_alert=True)

def time_lot(call_id,dict_lot):
    time_today=(int(time.time()))
    for x in dict_lot:
        if x =='time_create':
            time_break=dict_lot[x]
    print(time_break)
    c=time_today-int(time_break)
    if c>0:
        c=(time.ctime(c))
        print(c)

        bot.answer_callback_query(call_id,"Время окончания аукциона:" + c, show_alert=False)
    else:
        bot.answer_callback_query(call_id, "К сожалению, отменить ставку уже невозможно. Удачных торгов!!!", show_alert=False)

def stavka_back(call_id):
    a = datetime.now()
    b = datetime.now() + timedelta(minutes=1)

    bot.answer_callback_query(call_id, "Ставка отменена успешно", show_alert=False)
    bot.answer_callback_query(call_id, "Ставка отменена успешно", show_alert=False)
t=0
def start_lot(dict):
    t=datetime.now()
    print(t)

@bot.message_handler(commands=['start'])
def welcome(message):
    msg=bot.send_message(message.chat.id,"Привет ,я бот аукционов Я помогу вам следить за выбранными лотами ,и регулировать ход аукциона.Удачных торгов 🤝 ")
    #bot.register_next_step_handler(msg, post_lot)
    post_lot(dict_lot,message)
    check_is_ban(user_id)


@bot.callback_query_handler(func=lambda call: True)
def call(call):
    id = call.message.chat.id
    flag = fs(call.data)
    data = dt(call.data)
    #bot.answer_callback_query(callback_query_id=call.id)

    if flag == "li":
        information(call.id)

    if flag == "lt":
        time_lot(call.id,dict_lot)

    if flag == "lb":
        stavka_back(call.id)

    if flag == "li":
        information(call.id)

@bot.message_handler(commands=['new_car'])
def star_new_car(message):
    global car_init_dict
    my_id = str(message.from_user.id)
    if access_check(my_id) == '2' or access_check(my_id) == '1':
        car_init_dict[message.chat.id] = ""
        text = "Для добавления нового авто - нужно будет заполнить все сведения о нём\n" \
                "Для этого нужно пройтись по дальнейшим шагам \nудачи :)\n\n" \
                "Начнём с марки Авто - напишите на английском МАРКУ авто\n\n" \
                "Пример1 - BWM\n" \
                "Пример2 - Alfa Romeo"

        msg = bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(msg, photo_car)




print("Ready")

bot.infinity_polling()