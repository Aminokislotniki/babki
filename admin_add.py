import json


def create_new_admin_json(id_new_admin, user_name_new_admin, bot, chat_id):
    try:
        f = open("vocabulary/" + str(id_new_admin) + ".json", "r" , encoding="utf-8")
        f.close()
        bot.send_message(chat_id,"Данный пользователь уже является админом")
    except:
        admin = dict({
            "user": {"id_user": id_new_admin, "user_name": "@" + user_name_new_admin},
            "lots": [],
            "not_posted_lots": [],
            "arhive": []
        })
        with open('vocabulary/' + str(id_new_admin) + ".json", 'w', encoding='utf-8') as f:
            json.dump(admin, f, ensure_ascii=False, indent=4)
        bot.send_message(chat_id,"Пользователь @" + user_name_new_admin + " успешно добавлен")
