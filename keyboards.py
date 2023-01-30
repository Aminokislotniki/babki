from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#from post_lot import post_lots
import json

type_of_lots_keyboard = InlineKeyboardMarkup()
active_lots = InlineKeyboardButton("Активные", callback_data="sa*0")
nonpublic_lots = InlineKeyboardButton("Неопубликованные", callback_data="sn*0")
archive_lots = InlineKeyboardButton("Архивные", callback_data="sr*0")
exitbutton = InlineKeyboardButton(text="выход", callback_data="sq")
type_of_lots_keyboard.add(active_lots, nonpublic_lots, archive_lots)
type_of_lots_keyboard.add(exitbutton)

quit_only_keyboard = InlineKeyboardMarkup()
quit_only_keyboard.add(InlineKeyboardButton("Выход", callback_data="sq"))

def active_lots_keyboard(active_lots_list, page_number):
    keyboard = InlineKeyboardMarkup(row_width=2)
    backbutton = InlineKeyboardButton(text="предыдущие", callback_data="sa*" + str(page_number-1))
    nextbutton = InlineKeyboardButton(text="следующие", callback_data="sa*" + str(page_number+1))
    returntomenu = InlineKeyboardButton(text="назад в меню", callback_data="ss")
    exitbutton = InlineKeyboardButton(text="выход", callback_data="sq")
    if len(active_lots_list) < 9:
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sa:" + x["lot_id"]) for x in active_lots_list]
        keyboard.add(*button_list)
    elif 9*(page_number+1) < len(active_lots_list) and 8*page_number <=0:
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sa:" + x["lot_id"]) for x in active_lots_list[page_number*8:(page_number+1)*8]]
        keyboard.add(*button_list)
        keyboard.add(nextbutton)
    elif 8*(page_number+1) >= len(active_lots_list):
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sa:" + x["lot_id"]) for x in active_lots_list[page_number * 8:(page_number + 1) * 8]]
        keyboard.add(*button_list)
        keyboard.add(backbutton)
    else :
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sa:" + x["lot_id"]) for x in active_lots_list[page_number * 8:(page_number + 1) * 8]]
        keyboard.add(*button_list)
        keyboard.add(backbutton, nextbutton)
    keyboard.add(returntomenu, exitbutton)
    return keyboard


def nonpublic_lots_keyboard(nonpublic_lots_list, page_number):
    keyboard = InlineKeyboardMarkup(row_width=2)
    backbutton = InlineKeyboardButton(text="назад", callback_data="sn*" + str(page_number-1))
    nextbutton = InlineKeyboardButton(text="вперед", callback_data="sn*" + str(page_number+1))
    returntomenu = InlineKeyboardButton(text="назад в меню", callback_data="ss")
    exitbutton = InlineKeyboardButton(text="выход", callback_data="sq")
    if len(nonpublic_lots_list) < 9:
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sn:" + x["lot_id"]) for x in nonpublic_lots_list]
        keyboard.add(*button_list)
    elif 8*(page_number+1) < len(nonpublic_lots_list) and 9*page_number <=0:
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sn:" + x["lot_id"]) for x in nonpublic_lots_list[page_number*8:(page_number+1)*8]]
        keyboard.add(*button_list)
        keyboard.add(nextbutton)
    elif 9*(page_number+1) >= len(nonpublic_lots_list):
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sn:" + x["lot_id"]) for x in nonpublic_lots_list[page_number * 8:(page_number + 1) * 8]]
        keyboard.add(*button_list)
        keyboard.add(backbutton)
    else :
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sn:" + x["lot_id"]) for x in nonpublic_lots_list[page_number * 8:(page_number + 1) * 8]]
        keyboard.add(*button_list)
        keyboard.add(backbutton, nextbutton)
    keyboard.add(returntomenu, exitbutton)
    return keyboard



def arhive_lots_keyboard(arhive_lots_list, page_number):
    keyboard = InlineKeyboardMarkup(row_width=2)
    backbutton = InlineKeyboardButton(text="назад", callback_data="sr*" + str(page_number-1))
    nextbutton = InlineKeyboardButton(text="вперед", callback_data="sr*" + str(page_number+1))
    returntomenu = InlineKeyboardButton(text="назад в меню", callback_data="ss")
    exitbutton = InlineKeyboardButton(text="выход", callback_data="sq")
    if len(arhive_lots_list) < 9:
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sr:" + x["lot_id"]) for x in arhive_lots_list]
        keyboard.add(*button_list)
    elif 8*(page_number+1) < len(arhive_lots_list) and 9*page_number <=0:
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sr:" + x["lot_id"]) for x in arhive_lots_list[page_number*8:(page_number+1)*8]]
        keyboard.add(*button_list)
        keyboard.add(nextbutton)
    elif 8*(page_number+1) >= len(arhive_lots_list):
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sr:" + x["lot_id"]) for x in arhive_lots_list[page_number * 8:(page_number + 1) * 8]]
        keyboard.add(*button_list)
        keyboard.add(backbutton)
    else :
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sr:" + x["lot_id"]) for x in arhive_lots_list[page_number * 8:(page_number + 1) * 8]]
        keyboard.add(*button_list)
        keyboard.add(backbutton, nextbutton)
    keyboard.add(returntomenu, exitbutton)
    return keyboard



def stavka(id_l):
    stavka_keyboard = InlineKeyboardMarkup()
    button_one = (InlineKeyboardButton("Участвовать", callback_data="ly"+str(id_l)))
    button_four = (InlineKeyboardButton("Время", callback_data="lt" + str(id_l)))
    button_five = (InlineKeyboardButton("Информация", callback_data="li"))
    stavka_keyboard.add( button_one,button_four,button_five)
    return stavka_keyboard

def stavka1(data):
    f = open('lots/' + str(data) + '.json', 'r', encoding='utf-8')
    dict_lot = json.loads(f.read())
    f.close()
    min_stavka=""
    type_stavka=""
    start_price=""
    for z in dict_lot:
        for x in dict_lot[z]:
            if x == "min_stavka":
                min_stavka = int(dict_lot[z][x])
            if x==    "type_stavka":
                type_stavka=int(dict_lot[z][x])
            if x== "start_price":
                start_price=int(dict_lot[z][x])
    print(min_stavka)

    if type_stavka !=1:
        stavka_keyboard = InlineKeyboardMarkup()
        button_1 = (InlineKeyboardButton("+"+str(min_stavka), callback_data="la"+str(data)+'!'+str(min_stavka)))
        button_2 = (InlineKeyboardButton("+"+str(min_stavka*min_stavka), callback_data="la"+str(data)+'!'+str(min_stavka*min_stavka)))
        button_3 = (InlineKeyboardButton("+"+str(min_stavka*min_stavka*min_stavka), callback_data="la"+str(data)+'!'+str(min_stavka*min_stavka*min_stavka)))
        button_4=  (InlineKeyboardButton("+"+str(min_stavka*10),callback_data="la"+str(data)+'!'+str(min_stavka*10)))
        button_5 = (InlineKeyboardButton("+"+str(min_stavka*min_stavka*10), callback_data="la"+str(data)+'!'+str(min_stavka*min_stavka*10)))
        button_6 = (InlineKeyboardButton("+"+str(min_stavka*min_stavka*min_stavka*10), callback_data="la"+str(data)+'!'+str(min_stavka*min_stavka*min_stavka*10)))
        button_7 = (InlineKeyboardButton("Автоставка", callback_data="lh"+str(data) ))
        button_8 = (InlineKeyboardButton("Отменить", callback_data="lb"+str(data)))
        button_9 = (InlineKeyboardButton("Время", callback_data="lt"+str(data) ))
        button_10 = (InlineKeyboardButton("Информация", callback_data="li"))
        stavka_keyboard.add(button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10)

    else:
        list1=[]
        x=2.5
        while len(list1)<6:
            if start_price*x//100>min_stavka :
                list1.append(x)
            x+=2.5
        print(list1)
        stavka_keyboard = InlineKeyboardMarkup()
        button_list = [InlineKeyboardButton(text=str(x)+"%", callback_data="lf"+str(data)+"!"+str(x)) for x in list1]
        button_7 = (InlineKeyboardButton("Автоставка", callback_data="lh" + str(data)))
        button_8 = (InlineKeyboardButton("Отменить", callback_data="lb" + str(data)))
        button_9 = (InlineKeyboardButton("Время", callback_data="lt" + str(data)))
        button_10 = (InlineKeyboardButton("Информация", callback_data="li"))
        stavka_keyboard.add(*button_list, button_7,button_8,button_9,button_10)


    return stavka_keyboard

#
def stavka_canal(id_l):
    lot_keyboard = InlineKeyboardMarkup()
    button_tree = (InlineKeyboardButton("Участвовать",url="https://t.me/aminokislotnik_bot?start=",callback_data="ly"+str(id_l)))
    button_four = (InlineKeyboardButton("время", callback_data="lt"+str(id_l)))
    button_five = (InlineKeyboardButton("Информация", callback_data="li"))
    lot_keyboard.add(button_tree,button_four,button_five)
    return lot_keyboard


def keyboard_lot_bot():
    keyboard_lot_bot = InlineKeyboardMarkup()
    button_1 = (InlineKeyboardButton("Опубликовать", callback_data="ls"))
    button_2 = (InlineKeyboardButton("Удалить", callback_data="ld"))
    keyboard_lot_bot.add(button_1, button_2)
    return keyboard_lot_bot

def card_view_keyboard(id_lot, type):
    keyboard = InlineKeyboardMarkup()
    button_edit = (InlineKeyboardButton("Редактировать", callback_data="se*" + type + ":" + str(id_lot)))
    button_public_in_channel = (InlineKeyboardButton("Опубликовать", callback_data="sp*" + str(id_lot)))
    exitbutton = InlineKeyboardButton(text="Выход", callback_data="sq")
    keyboard.add(button_edit)
    if type =="n":
        keyboard.add(button_public_in_channel)
    keyboard.add(exitbutton)
    return keyboard

def edit_card_keyboard(id_lot, type_lot):
    print("edit_card_keyboard", type_lot)
    keyboard = InlineKeyboardMarkup(row_width=2)
    names = ["Название","Описание", "Город", "Условия доставки", "Стартовая цена"]
    button_list = [InlineKeyboardButton(text=x, callback_data="se:" + type_lot + "*" + str(id_lot) + "?" + x) for x in names]
    save_button = InlineKeyboardButton(text="Сохранить", callback_data="sw*" + type_lot + ":" + str(id_lot))
    button_public_in_channel = (InlineKeyboardButton("Опубликовать", callback_data="sp*" + str(id_lot)))
    exitbutton = InlineKeyboardButton(text="Выход", callback_data="sq")
    keyboard.add(*button_list)
    keyboard.add(save_button)
    if type_lot == "n":
        keyboard.add(button_public_in_channel)
    keyboard.add(exitbutton)
    return keyboard
