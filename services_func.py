import json
import traceback

def dt_serj(s):
    s = s[2:]
    return s


def fs_serj(st):
    return(st[0:2])


def check_ban(user_id):
    # Принимает  int - user_id
    # Возвращает True - если у пользователя НЕТ бана
    # Возвращает False - если пользователь в бане
    # Если какая-то лабуда пишет в терминал сообщение
    f = open("users_statistics.json", 'r', encoding='utf-8')
    buf_statistics = json.loads(f.read())
    f.close()
    if user_id in buf_statistics.keys():
        if buf_statistics[str(user_id)]["ban"] == "False":
            return True
        elif buf_statistics[str(user_id)]["ban"] == "True":
            return False
        else:
            print("Что-то пошло не так в функции  - check_ban")
    else:
        buf_statistics[str(user_id)] = dict({"ban": "False", "bets": []})

        with open('users_statistics.json', 'w', encoding='utf-8') as f:
            json.dump(buf_statistics, f, ensure_ascii=False, indent=4)
        return True


def check_is_admin(user_id, bot):
    # Принимает  int - user_id, bot - обьект телебота, для отправки сообщения
    # Возвращает True - если пользователь является админом
    # Возвращает False - если у пользователя нет прав доступа и отправляет ему сообщение об этом
    try:
        name_file = "vocabulary/" + str(user_id) + ".json"
        f = open(name_file, 'r', encoding='utf-8')
        f.close()
        return True
    except:
        bot.send_message(user_id, "Вы не являетесь Администратором")
        return False


def viev_card_lot(lot_id):
    print(lot_id)
    # try:
    f = open("lots/" + str(lot_id) + ".json", 'r', encoding='utf-8')
    lot = json.loads(f.read())
    f.close()
    # except Exception as e:
    #     print(e)
    #     return print("Что-то не так в функции viev_card_lot")

    text = ""
    for keys, value in lot["lot_info"].items():
        if keys != "photo":
            text += value + "\n"
    return text, lot["lot_info"]["photo"]
