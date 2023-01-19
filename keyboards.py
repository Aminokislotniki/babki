from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

type_of_lots_keyboard = InlineKeyboardMarkup()
active_lots = InlineKeyboardButton("Активные", callback_data="sa*0")
nonpublic_lots = InlineKeyboardButton("Неопубликованные", callback_data="sn*0")
archive_lots = InlineKeyboardButton("Архивные", callback_data="sr*0")
exitbutton = InlineKeyboardButton(text="выход", callback_data="sq")
type_of_lots_keyboard.add(active_lots, nonpublic_lots, archive_lots)
type_of_lots_keyboard.add(exitbutton)


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


