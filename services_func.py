import json


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
    if user_id  in buf_statistics.keys():
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
