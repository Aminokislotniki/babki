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

