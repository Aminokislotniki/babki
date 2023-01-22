import json


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