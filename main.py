import json
from variables import bot
from keyboards import type_of_lots_keyboard, active_lots_keyboard, nonpublic_lots_keyboard
from services_func import fs_serj, dt_serj, check_ban, check_is_admin, check_is_super_admin, id_lot
# from admin_add import catch_reply

@bot.message_handler(commands=['start'])
def statistics(message):
    try:
        f = open("users_statistics.json", 'r', encoding='utf-8')
        buf_statistics = json.loads(f.read())
        f.close()
        if str(message.from_user.id) not in buf_statistics.keys():
            print("new user " + str(message.from_user.id))
            print(buf_statistics)
            buf_statistics[str(message.from_user.id)] = dict({"ban":"False", "bets":[]})

            with open('users_statistics.json', 'w', encoding='utf-8') as f:
                json.dump(buf_statistics, f, ensure_ascii=False, indent=4)

        else:
            # кусок else - можно убрать - чисто для проверки, что работает
            print("old user " + str(message.from_user.id))
    except:
        print("Что-то пошло не так в команде /start")

@bot.message_handler(commands=['admin_add'])
def start_admin(message):
    if check_is_super_admin(message.from_user.id, bot):
        bot.send_message(message.chat.id,
                         "Перешлите сюда сообщение от человека, которого вы хотите добавить в Администраторы")
        # msg = bot.send_message(message.chat.id, "Перешлите сюда сообщение от человека, которого вы хотите добавить в Администраторы")
        # bot.register_next_step_handler(msg, catch_reply)



@bot.message_handler(commands=['view_lots'])
def view_lots(message): 
    # Проверка на админа
    if check_is_admin(message.from_user.id, bot):
        # теперь отправляем пользователю 3 кнопки
        bot.send_message(message.chat.id, "Выберите тип лота, который вы хотите просмотреть", reply_markup=type_of_lots_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def call(call):
    print(call)
    print(call.data + " from " + call.from_user.username)
    flag = fs_serj(call.data)
    data = dt_serj(call.data)


    # Флаг для выхода из команды /view_lots
    if flag == "sq":
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            print()

    # Флаг для возврата в меню выбора типа Лотов
    if flag =="ss":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Выберите тип лота, который вы хотите просмотреть", reply_markup=type_of_lots_keyboard)

    # Флаг для выброса Активнивных Лотов (parametr "lots")
    if flag =="sa":
        if data[0] =="*":
            page = data.split("*")
            page = int(page[1])
            try:
                name_file = "vocabulary/" + str(call.from_user.id) + ".json"
                f = open(name_file, 'r', encoding='utf-8')
                buf_admin_file = json.loads(f.read())
                f.close()
                active_lots = buf_admin_file['lots']
                if len(active_lots) > 0:
                    bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text= "Выберете нужный лот\nстраница - " + str(page+1), reply_markup=active_lots_keyboard(active_lots, page))
                else:
                    bot.send_message(call.message.chat.id, "Активных лотов не найдено")
            except Exception:
                bot.send_message(call.message.chat.id, "Вы не создавали Лоты")

        if data[0] == ":":
            try:
                bot.send_message(call.message.chat.id, "ID лота = " + data[1:])
                # тут должна быть попытка считать файл лота

                # Должен быть вызов функции Кати - на вывод лота ( Либо же мой - на вывод + редактировать и удалить)
                # !!! Обсудить на уроке
            except:
                bot.send_message(call.message.chat.id,"Что-то пошло не так")

    # Флаг для выброса Неопубликованных Лотов (parametr "not_posted_lots")
    if flag == "sn":
        if data[0] == "*":
            page = data.split("*")
            page = int(page[1])
            try:
                name_file = "vocabulary/" + str(call.from_user.id) + ".json"
                f = open(name_file, 'r', encoding='utf-8')
                buf_admin_file = json.loads(f.read())
                f.close()
                not_posted_lots = buf_admin_file['not_posted_lots']
                if len(not_posted_lots) > 0:
                    bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                          text="Выберете нужный лот\nстраница - " + str(page + 1),
                                          reply_markup=nonpublic_lots_keyboard(not_posted_lots, page))
                else:
                    bot.send_message(call.message.chat.id, "Неопубликованных лотов не найдено")
            except Exception:
                bot.send_message(call.message.chat.id, "Вы не создавали Лоты")

        if data[0] == ":":
            try:
                bot.send_message(call.message.chat.id, "ID лота = " + data[1:])
                # тут должна быть попытка считать файл лота

                # Должен быть вызов функции Кати - на вывод лота ( Либо же мой - на вывод + редактировать и опубликовать)
                # !!! Обсудить на уроке
            except:
                bot.send_message(call.message.chat.id,"Что-то пошло не так")

    # Флаг для выброса Архивных Лотов (parametr "arhive")
    if flag =="sr":
        if data[0] == "*":
            page = data.split("*")
            page = int(page[1])
            try:
                name_file = "vocabulary/" + str(call.from_user.id) + ".json"
                f = open(name_file, 'r', encoding='utf-8')
                buf_admin_file = json.loads(f.read())
                f.close()
                arhive_lots = buf_admin_file['arhive']
                if len(arhive_lots) > 0:
                    bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                          text="Выберете нужный лот\nстраница - " + str(page + 1),
                                          reply_markup=nonpublic_lots_keyboard(arhive_lots, page))
                else:
                    bot.send_message(call.message.chat.id, "Неопубликованных лотов не найдено")
            except Exception:
                bot.send_message(call.message.chat.id, "Вы не создавали Лоты")

        if data[0] == ":":
            try:
                bot.send_message(call.message.chat.id, "ID лота = " + data[1:])
                # тут должна быть попытка считать файл лота

                # Должен быть вызов функции Кати - на вывод лота ( Либо же мой - на вывод + редактировать и опубликовать)
                # !!! Обсудить на уроке
            except:
                bot.send_message(call.message.chat.id,"Что-то пошло не так")





print("Ready")
bot.infinity_polling()

