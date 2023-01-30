# здесь будет функция, добавления админом, нового лота
from telebot.types import ReplyKeyboardRemove, InputMediaPhoto
import time
import telebot
import json
from datetime import datetime, timedelta
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from services_func import dt_serj,fs_serj,id_lot
from post_lot import post_lots
from variables import bot
from keyboards import stavka_canal,keyboard_lot_bot,stavka,stavka1
#bot = telebot.TeleBot('5683069905:AAHCr6JGd2ztVfZMD-zWvebA3-P20qqCehI')
id_chanel = "@projectlimonbot"
lot_init_dict={}
dict_lot={}
id_l=""

@bot.message_handler(commands=['start'])
#возвращает карточку лота
def star_lot(message):
    id_ll=(message.text)[7:]
    buf,photo,times,min_stavka,start_price=post_lots(id_ll)
    print(id_ll)
    bot.send_message(message.chat.id,"Привет ,я бот аукционов Я помогу вам следить за выбранными лотами ,и регулировать ход аукциона.Удачных торгов 🤝 ")
    bot.send_photo(message.chat.id,photo=photo,  caption=buf,reply_markup=stavka(id_ll))


@bot.message_handler(commands=['new_lot'])
def star_new_lot(message):
    #global lot_init_dict
    lot_init_dict[message.chat.id] = ""
    text = "Так будет выглядеть опубликованный лот\n" \
            "Для этого нужно пройтись по дальнейшим шагам \nудачи :)\n\n" \
            "Начнём - напишите  название лота\n\n" \

    #msg = bot.send_message(message.chat.id, text)
    photo=open(r"C:\Users\37529\PycharmProjects\pythonProject4\Снимок экрана 2023-01-28 214100.png","rb")
    msg=bot.send_photo(message.chat.id, photo=photo, caption=text)
    bot.register_next_step_handler(msg, lot)

class Lot:
    def __init__(self, lot):
        self.lot = lot
        self.description = None
        self.price = None
        self.min_stavka = None
        self.type_stavka = None
        self.photo = None

def lot_obj_lot(obj_lot):
    all_atributes = obj_lot.__dict__
    text = ""

    for key, value in all_atributes.items():
        val = value
        if key != "photo":
            if value == None:
                val = ""
            text = text + key + " : " + val + "\n"
    return text

def lot(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != "":
        new_lot = Lot(message.text)
        lot_init_dict[message.chat.id] = new_lot
        dict_lot["lot_info"]={}
        dict_lot["lot_info"].update({"lot_name":message.text})
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        msg = bot.send_message(message.chat.id, "Теперь отправьте описание лота")
        bot.register_next_step_handler(msg, description)
    else:
        msg = bot.send_message(message.chat.id,
                           "Ты неверно написал, напиши снова или\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, lot)

def description(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != "":
        lot_init_dict[message.chat.id].description = message.text
        dict_lot["lot_info"].update({"description":message.text})
        print(dict_lot)
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.delete_message(message.chat.id, message.message_id-2)
        msg = bot.send_message(message.chat.id, "Теперь отправьте цену лота")
        bot.register_next_step_handler(msg, price)

    else:
        msg = bot.send_message(message.chat.id,
                           "Ты неверно написал, напиши снова или\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, description)

def price(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != "" and message.text.isdigit() and int(message.text)>0:
        lot_init_dict[message.chat.id].price = message.text
        dict_lot["service_info"]={}
        dict_lot ["lot_info"].update({"start_price":int(message.text)})
        dict_lot["service_info"].update({"start_price": int(message.text)})
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        msg = bot.send_message(message.chat.id,
                               "Теперь отправьте минмальную ставку")
        bot.register_next_step_handler(msg, min_stavka)
    else:
        msg = bot.send_message(message.chat.id,
                           "Ты неверно написал, напиши снова или\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg,price)

def min_stavka(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != ""and message.text.isdigit()and int(message.text)>0:
        lot_init_dict[message.chat.id].min_stavka = message.text
        dict_lot["service_info"].update({"min_stavka":int(message.text)})
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        msg = bot.send_message(message.chat.id, "Теперь отправьте тип ставки:\n цифра '1'-% от стартовой цены (от 2 до 50, но не меньше) "
                                                "минимальной ставки\n-или введи шаг ставки")
        bot.register_next_step_handler(msg, type_stavka)
    else:
        msg = bot.send_message(message.chat.id,
                               "Ты неверно написал, напиши снова или\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, min_stavka)


def type_stavka(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала.  Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != ""and message.text.isdigit() and int(message.text)>0:
        lot_init_dict[message.chat.id].type_stavka = message.text
        dict_lot["service_info"].update({"type_stavka":int(message.text)})
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        msg = bot.send_message(message.chat.id, "Осталось загрузить фото")
        bot.register_next_step_handler(msg, photo_lot)
    else:
        msg = bot.send_message(message.chat.id,
                               "Ты неверно написал, напиши снова или\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, type_stavka)



def photo_lot(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "photo":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)

        photo1=( message.photo[-1].file_id)
        dict_lot["service_info"] .update( {"id_admin": message.from_user.id})
        bot.send_photo(message.chat.id, photo1,lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.send_message(message.chat.id,"Вот карточка лота.\nЧто делаем дальше?\nНажми опубликовать\n Переходи в канал для опубликования: https://t.me/projectlimonbot\n"
                                         "для создания нового лота пришли '/new_lot'",reply_markup=keyboard_lot_bot())
        dict_lot["lot_info"].update( {"user_name_admin": message.from_user.username})
        dict_lot["lot_info"].update({'photo':photo1})


    else:
        msg = bot.send_message(message.chat.id,
                               "Ты неверно написал, напиши снова или\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, photo_lot)

#конвертер времени
def convert_sec(times):
    sec_to_min=60
    sec_to_hour=60*sec_to_min
    sec_to_day=24*sec_to_hour
    days=times//sec_to_day
    times %=sec_to_day
    hour = times//sec_to_hour
    times %= sec_to_hour
    min = times//sec_to_min
    times %= sec_to_min
    sec=times
    t=("\n%d дня, %d часа, %d минуты, %d секунды" % (days, hour, min, sec))
    return t

#проверка втемени аукциона
def time_lot(call_id,data):
    f = open('lots/'+str(data)+'.json', 'r', encoding='utf-8')
    dict_lot = json.loads(f.read())
    f.close()
    time_today=(int(time.time()))
    time_break=""
    a=60*60*24*5
    for z in dict_lot:
        for x in dict_lot[z]:
            if x == "time_create":
                time_break += str(dict_lot[z][x])
    time_break=int(time_break)+a
    print(time_break)
    print(time_today)
    times = int(time_break)-time_today
    if times > 0:
        bot.answer_callback_query(call_id, "аукцион закончиться через \n "+convert_sec(times), show_alert=False)
    else:
        bot.answer_callback_query(call_id, "Аукцион уже закончен, участие невозможно,\n посмотрите другие лоты" , show_alert=False)

#cтавка отмены
def stavka_back(call_id,data):
    a = datetime.now()
    f = open('lots/' + str(data) + '.json', 'r', encoding='utf-8')
    dict_lot = json.loads(f.read())
    f.close()
    for z in dict_lot:
        if z=="history_bets":
            mas_bets=dict_lot[z]
    print(mas_bets)
            # for x in dict_lot[z]:
            #     print(x)
    # if b>a:
    #     bot.answer_callback_query(call_id, "Ставка отменена успешно", show_alert=False)
    # else:
    #     bot.answer_callback_query(call_id, "Ставкy отменить невозможно", show_alert=False)

def information(call_id):
    bot.answer_callback_query(call_id, "Ставку можно отменить в течении 1 минуты, нажав на кнопку Отмена."
                                       "Выигранный лот необходимо выкупить в течении 5 дней, в противном случае БАН на 5 дней!!!", show_alert=True)

#ставка при первом нажатии участвовать
def stavka_lot(call_id,user_name,id,data):
    time_stavka = datetime.now() + timedelta(minutes=1)
    print(time_stavka)
    start_price = ""
    f = open('lots/' + str(data) + '.json', 'r', encoding='utf-8')
    dict_lot = json.loads(f.read())
    f.close()
    for z in dict_lot:
        for x in dict_lot[z]:
            if x == "start_price":
                start_price = int(dict_lot[z][x])
    dict_lot["lot_info"]["actual_price"] = start_price
    dict_lot["history_bets"].append([id,user_name,start_price])

    with open('lots/' + str(data) + '.json', 'w', encoding='utf-8') as f:
        json.dump(dict_lot, f, ensure_ascii=False, indent=15)
    user_name = user_name[0:3] + "***"
    bot.send_message(call_id, " Ваша ставка принята\n " + str(start_price) + user_name, reply_markup=stavka1(data))


#ставка с процентами
def percent_stavka(mas_st,user_name,call_id,id):
    actual_price = ""
    start_price = ""
    f = open('lots/' + str(mas_st[0]) + '.json', 'r', encoding='utf-8')
    dict_lot = json.loads(f.read())
    f.close()
    for z in dict_lot:
        for x in dict_lot[z]:
            if x == "actual_price":
                actual_price = (dict_lot[z][x])
            if x == "start_price":
                start_price = (dict_lot[z][x])

    actual_price_new=int(start_price*float(mas_st[1])/100)+start_price
    print(actual_price_new)
    if actual_price_new>actual_price:
        dict_lot["lot_info"]["actual_price"] = actual_price_new
        dict_lot["history_bets"] .append([id, user_name, actual_price_new])


        with open('lots/' + str(mas_st[0]) + '.json', 'w', encoding='utf-8') as f:
            json.dump(dict_lot, f, ensure_ascii=False, indent=15)
        user_name = user_name[0:3] + "***"
        bot.send_message(call_id, " Ваша ставка принята\n " + str(actual_price_new) + user_name, reply_markup=stavka1(mas_st[0]))
    else:
        bot.send_message(call_id, " Ваша ставка не принята\n " + str(actual_price) + user_name,
                         reply_markup=stavka1(mas_st[0]))



#ставка с цифрами
def dinamic_stavka(mas_st,user_name,call_id,id):
    #print(data_st)
    actual_price = ""
    f = open('lots/' + str(mas_st[0]) + '.json', 'r', encoding='utf-8')
    dict_lot = json.loads(f.read())
    f.close()
    for z in dict_lot:
        for x in dict_lot[z]:
            if x == "actual_price":
                actual_price = (dict_lot[z][x])
    actual_price_new = int(actual_price + float(mas_st[1]))
    print(actual_price)
    dict_lot["lot_info"]["actual_price"] = actual_price_new
    dict_lot["history_bets"] .append ([id, user_name, actual_price_new])
    with open('lots/' + str(mas_st[0]) + '.json', 'w', encoding='utf-8') as f:
        json.dump(dict_lot, f, ensure_ascii=False, indent=15)
    user_name = user_name[0:3] + "***"
    bot.send_message(call_id, " Ваша ставка принята\n " + str(actual_price_new) + user_name,
                     reply_markup=stavka1(mas_st[0]))


@bot.callback_query_handler(func=lambda call: True)
def call(call):
    id = call.message.chat.id
    user_name = call.message.chat.username
    flag =fs_serj(call.data)
    data = dt_serj (call.data)
    # bot.answer_callback_query(callback_query_id=call.id)

    #запись лота
    if flag == "ls":
        bot.answer_callback_query(callback_query_id=call.id)
        dict_lot["lot_info"].update({"actual_price":None})
        dict_lot["service_info"].update({"message_id_in_channel":None})
        dict_lot["service_info"] .update({"status": "activ"})
        dict_lot["service_info"] .update({"time_create": (int(time.time()))})
        dict_lot["service_info"].update({"winner_dict":{"user_name":None, "price_final": None}})
        dict_lot["history_bets"] = []
        id_l=id_lot()
        with open('lots/'+str(id_l)+'.json', 'w', encoding='utf-8') as f:
            json.dump(dict_lot, f, ensure_ascii=False, indent=15)

        bot.send_photo(id_chanel, dict_lot ["lot_info"]["photo"], caption=post_lots(id_l), reply_markup=stavka_canal(id_l))
        bot.delete_message(call.message.chat.id,call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id-1)

    #сборка лота
    if flag == "ld":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(id, " попробуй снова, пришли '/new_lot'")
        dict_lot.clear()

    #ставка
    if flag=="ly":
        data = (call.data)[2:]
        print(call.data)
        stavka_lot(id, user_name, id,data)

        #
    if flag == "lf":
        mas_st=data.split('!')
        print(mas_st)
        percent_stavka(mas_st,user_name,id,id)

    #время
    if flag == "lt":
        data=(call.data)[2:]
        print(data)
        time_lot(call.id,data)

    #информация
    if flag == "li":
        information(call.id)

    # автоставка
    if flag == "la":
        mas_st = data.split('!')
        print(data)
        print(user_name)
        dinamic_stavka(mas_st,user_name,id,id)

    #для отмены ставки
    if flag == "lb":
        print(data)
        stavka_back(call.id,data)

#bot.send_photo(2077212957,"AgACAgIAAxkBAAIicGPLzbi0TdFyeMpjwj90yzAsu7mBAAI_xTEbO7VhSiazPrxb8uMrAQADAgADeQADLQQ",caption="dd")




print("Ready")

bot.infinity_polling()