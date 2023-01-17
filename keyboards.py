from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

type_of_lots_keyboard = InlineKeyboardMarkup()
active_lots = InlineKeyboardButton("Активные", callback_data="sa*0")
nonpublic_lots = InlineKeyboardButton("Неопубликованные", callback_data="sn*0")
archive_lots = InlineKeyboardButton("Архивные", callback_data="sr*0")
type_of_lots_keyboard.add(active_lots, nonpublic_lots, archive_lots)


def active_lots_keyboard(active_lots_list, page_number):
    keyboard = InlineKeyboardMarkup(row_width=3)
    backbutton = InlineKeyboardButton(text="назад", callback_data="sa*" + str(page_number-1))
    nextbutton = InlineKeyboardButton(text="вперед", callback_data="sa*" + str(page_number+1))
    if len(active_lots_list) < 10:
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sa:" + x["lot_id"]) for x in active_lots_list]
        keyboard.add(*button_list)
    elif 9*(page_number+1) < len(active_lots_list) and 9*page_number <=0:
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sa:" + x["lot_id"]) for x in active_lots_list[page_number*9:(page_number+1)*9]]
        keyboard.add(*button_list)
        keyboard.add(nextbutton)
    elif 9*(page_number+1) >= len(active_lots_list):
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sa:" + x["lot_id"]) for x in active_lots_list[page_number * 9:(page_number + 1) * 9]]
        keyboard.add(*button_list)
        keyboard.add(backbutton)
    else :
        button_list = [InlineKeyboardButton(text=x["lot_name"], callback_data="sa:" + x["lot_id"]) for x in active_lots_list[page_number * 9:(page_number + 1) * 9]]
        keyboard.add(*button_list)
        keyboard.add(backbutton, nextbutton)
    return keyboard

