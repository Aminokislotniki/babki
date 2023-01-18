import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
import gspread
from datetime import datetime, timedelta
from fuzzywuzzy import process

bot = telebot.TeleBot('5683069905:AAGVpQBnaKoilz2UYWK1Ug3XoAENmDsTUyc');
id_chanel = "@sandbox_chanell"

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

def time(call_id):
    a=datetime.now()
    b=datetime.now()+timedelta(days=5,hours=5)
    c=b-a
    bot.answer_callback_query(call_id, c, show_alert=False)

def stavka_back(call_id):
    a = datetime.now()
    b = datetime.now() + timedelta(minutes=1)


    bot.answer_callback_query(call_id, "Ставка отменена успешно", show_alert=False)
    bot.answer_callback_query(call_id, "Ставка отменена успешно", show_alert=False)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,"Привет ,я бот аукционов Я помогу вам следить за выбранными лотами ,и регулировать ход аукциона.Удачных торгов 🤝 ")
    bot.send_message(message.chat.id, "лот ",reply_markup=stavka(list))



@bot.callback_query_handler(func=lambda call: True)
def call(call):
    id = call.message.chat.id
    flag = fs(call.data)
    data = dt(call.data)
    #bot.answer_callback_query(callback_query_id=call.id)

    if flag == "li":
        information(call.id)

    if flag == "lt":
        time(call.id)

    if flag == "lb":
        stavka_back(call.id)

    if flag == "li":
        information(call.id)

@bot.message_handler(commands=['new_car'])
def star_new_car(message):
    global car_init_dict
    my_id = str(message.from_user.id)
    # if access_check(my_id) == '2' or access_check(my_id) == '1':
    #     car_init_dict[message.chat.id] = ""
    #     text = "Для добавления нового авто - нужно будет заполнить все сведения о нём\n" \
    #             "Для этого нужно пройтись по дальнейшим шагам \nудачи :)\n\n" \
    #             "Начнём с марки Авто - напишите на английском МАРКУ авто\n\n" \
    #             "Пример1 - BWM\n" \
    #             "Пример2 - Alfa Romeo"
    #
    #     msg = bot.send_message(message.chat.id, text)
    #     bot.register_next_step_handler(msg, photo_car)




print("Ready")

bot.infinity_polling()