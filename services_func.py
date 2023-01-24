import json
from babki.keyboards import edit_card_keyboard
from keyboards import quit_only_keyboard


def dt_serj(s):
    s = s[2:]
    return s


def fs_serj(st):
    return(st[0:2])


def check_is_ban(user_id):
    # Возвращает FALSE - если бана нет.
    # Возвращает TRUE - если есть бан.
    # Если вдруг не нашло такого пользователя - записывает в JSON рыбу и возвращает FALSE
    f = open("users_statistics.json", 'r', encoding='utf-8')
    buf_statistics = json.loads(f.read())
    f.close()
    print(buf_statistics.keys())
    if str(user_id) in buf_statistics.keys():
        return buf_statistics[str(user_id)]["ban"]["is_ban"]
    else:
        buf_statistics[str(user_id)] = dict({"ban": {"is_ban": False, "time": 0}, "bets": []})
        with open('users_statistics.json', 'w', encoding='utf-8') as f:
            json.dump(buf_statistics, f, ensure_ascii=False, indent=4)
        print("Создан новый пользователь  ID=" + str(user_id))
        return False


def check_is_admin(user_id, bot):
    try:
        name_file = "vocabulary/" + str(user_id) + ".json"
        f = open(name_file, 'r', encoding='utf-8')
        f.close()
        return True
    except:
        bot.send_message(user_id, "Вы не являетесь Администратором")
        return False


def check_is_super_admin(user_id, bot):
    try:
        f = open("users_statistics.json", 'r', encoding="utf-8")
        buf = json.loads(f.read())
        super_admins = buf["super_admin_id"]
        if user_id in super_admins:
            return True
        else:
            bot.send_message(user_id,"Вы не являетесь Супер Администратором")
            return False
    except:
        print("что-то пошло не так в функции check_is_super_admin")


def id_lot():
    f = open("users_statistics.json", "r", encoding="utf-8")
    buf = json.loads(f.read())
    f.close()
    id = buf["lot_id"]
    buf["lot_id"] = id+1
    with open('users_statistics.json', 'w', encoding='utf-8') as f:
        json.dump(buf, f, ensure_ascii=False, indent=4)
    return buf["lot_id"]


def view_card_of_lot(lot_id, bot, chat_id):
    try:
        f = open("lots/" + str(lot_id) + ".json", "r", encoding="utf-8")
        lot = json.loads(f.read())
        f.close()
        text = f'Название: {lot["lot_info"]["lot_name"]}\n' \
               f'Описание: {lot["lot_info"]["description"]}\n' \
               f'Город: {lot["lot_info"]["city"]}\n' \
               f'Условия доставки: {lot["lot_info"]["delivery terms"]}\n' \
               f'Продавец: {lot["lot_info"]["delivery terms"]}\n' \
               f'Стартовая цена: {lot["lot_info"]["start_price"]}\n' \
               f'Актуальная цена: {lot["lot_info"]["actual_price"]}\n'
        return text, lot


    except:
        bot.send_message(chat_id, "Какая-то хрень, но файл с ID - " + str(lot_id) + " не найден :(")
        return 0, 0

def edit_caption(message,bot, call, edit_part, id_lot, type_lot):
    if message.text == "/stop":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.send_message(message.chat.id, "Вы вышли из редактирования", reply_markup=quit_only_keyboard)
    elif message.content_type == "text":
        old_caption = call.message.caption
        old_caption = old_caption.split("\n")
        for i in range(len(old_caption)):
            if edit_part in old_caption[i]:
                old_caption[i] = edit_part+ ": " + message.text
                break
        new_caption = "\n".join(old_caption)
        bot.edit_message_caption(caption=new_caption, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=edit_card_keyboard(id_lot,type_lot))
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.delete_message(message.chat.id, message.message_id)


def save_new_caption_lot(caption, id_lot, admin_id, type_lot, bot, chat_id):
    names = ["Название", "Описание", "Город", "Условия доставки", "Стартовая цена"]
    keys = ["lot_name", "description", "city", "delivery terms", "start_price"]
    caption = caption.split("\n")
    new_data = dict()
    for i in range(len(names)):
        for x in caption:
            if names[i] in x:
                new_data[keys[i]] = x.replace((names[i]+": "), "")
    f = open("lots/" + str(id_lot) + ".json", "r", encoding="utf-8")
    lot = json.loads(f.read())
    f.close()
    lot["lot_info"].update(new_data)
    with open('lots/'+ id_lot + ".json", 'w', encoding='utf-8') as f:
        json.dump(lot, f, ensure_ascii=False, indent=4)

    lot_name_new = lot["lot_info"]["lot_name"]

    f = open("vocabulary/" + str(admin_id) + ".json", "r", encoding="utf-8")
    admin = json.loads(f.read())
    f.close()
    lots_list = admin[type_lot]
    for i in range(len(lots_list)):
        if lots_list[i]["lot_id"] == str(id_lot):
            admin[type_lot][i]["lot_name"] = lot_name_new
            break
    with open('vocabulary/'+ str(admin_id) + ".json", 'w', encoding='utf-8') as f:
        json.dump(admin, f, ensure_ascii=False, indent=4)
    bot.send_message(chat_id, "Лот " + lot_name_new + " успешно сохранен", reply_markup=quit_only_keyboard)

def post_to_channel_by_id(message,lot_id, bot):
    if message.text == "/stop":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id -1)
        bot.send_message(message.chat.id, "Вы вышли из отправки в канал, но вы можете продолжить редактировать лот", reply_markup=quit_only_keyboard)
    elif message.text == "/continue":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.send_message(message.chat.id, "Тут должна быть функция отправки в бот")
    else:
       msg = bot.send_message("Вы можете либо выйти через /stop\nЛибо подтвердить отправку через /continue")
       bot.register_next_step_handler(msg, post_to_channel_by_id, lot_id, bot)