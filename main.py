import json
from variables import bot
from keyboards import type_of_lots_keyboard, active_lots_keyboard, nonpublic_lots_keyboard
from services_func import fs_serj, dt_serj


@bot.message_handler(commands=['view_lots'])
def view_lots(message):
    # тут должна быть проверка на админа
    # теперь отправляем пользователю 3 кнопки
    # bot.delete_message(message.chat.id,message.message_id)
    bot.send_message(message.chat.id, "Выберите тип лота, который вы хотите просмотреть", reply_markup=type_of_lots_keyboard)\


@bot.callback_query_handler(func=lambda call: True)
def call(call):
    print(call.data + " from " + call.from_user.username)
    flag = fs_serj(call.data)
    data = dt_serj(call.data)
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
                print(not_posted_lots)
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

    if flag =="sr":
        print("here archived lots")



print("Ready")
bot.infinity_polling()

