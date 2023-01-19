# здесь будет функция, добавления админом, нового лота
from telebot.types import ReplyKeyboardRemove, InputMediaPhoto
import telebot
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot('5683069905:AAGVpQBnaKoilz2UYWK1Ug3XoAENmDsTUyc')
id_chanel = "@sandbox_chanell"
lot_init_dict={}

# Класс нужный для добавления  от админов
bot.send_message(id_chanel, "А как тут команды вызвать?")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(id_chanel,"Привет")


class Lot:
    def __init__(self, lot):
        self.lot = lot
        self.id_lot = None
        self.description = None
        self.price = None
        self.min_stavka = None
        self.type_stavka = None
        self.data = None
        self.photo = []


def lot_obj_lot(obj_lot):
    all_atributes = obj_lot.__dict__
    text = ""

    for key, value in all_atributes.items():
        val = value
        if key != "photo":
            if value == None:
                val = ""
            text = text + key + " : " + val + "\n"
    return text


def lot(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != "":
        print(message.id)
        new_lot = Lot(message.text)
        lot_init_dict[message.chat.id] = new_lot
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
        msg = bot.send_message(message.chat.id, "Теперь отправьте описание лота")
        bot.register_next_step_handler(msg, description)
    else:
        msg = bot.send_message(message.chat.id,
                           "что-то пошло не так, попробуй снова\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, lot)


def description(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != "":
        lot_init_dict[message.chat.id].description = message.text
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.delete_message(message.chat.id, message.message_id-2)
        msg = bot.send_message(message.chat.id, "Теперь отправьте цену лота")
        bot.register_next_step_handler(msg, price)

    else:
        msg = bot.send_message(message.chat.id,
                           "что-то пошло не так, попробуй снова\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, description)

def price(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != "" and message.text.isdigit():
        lot_init_dict[message.chat.id].price = message.text
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)

        msg = bot.send_message(message.chat.id,
                               "Теперь отправьте минмальную ставку")
        bot.register_next_step_handler(msg, min_stavka)
    else:
        msg = bot.send_message(message.chat.id,
                           "что-то пошло не так, попробуй снова\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg,price)


def min_stavka(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != ""and message.text.isdigit():
        lot_init_dict[message.chat.id].min_stavka = message.text
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        msg = bot.send_message(message.chat.id, "Теперь отправьте тип ставки:\n цифра '1'-% от стоимости (от 2 до 10, но не меньше "
                                                "минимальной ставки\n-или введи шаг ставки(т.е. возрастающая в 10 раз")
        bot.register_next_step_handler(msg, type_stavka)
    else:
        msg = bot.send_message(message.chat.id,
                               "что-то пошло не так, попробуй снова\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, min_stavka)

def type_stavka(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала.  Пришли название лота")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добaвления лота")

    elif message.content_type == "text" and message.text.replace(" ", "") != ""and message.text.isdigit():
        lot_init_dict[message.chat.id].type_stavka = message.text
        bot.send_message(message.chat.id, lot_obj_lot(lot_init_dict[message.chat.id]))
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        msg = bot.send_message(message.chat.id, "Осталось загрузить фото")
        bot.register_next_step_handler(msg, photo_lot)
    else:
        msg = bot.send_message(message.chat.id,
                               "что-то пошло не так, попробуй снова\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, type_stavka)

def photo_lot(message):
    if message.text == "/new_lot":
        msg = bot.send_message(message.chat.id, "Начнём с начала. Пришли Марку Авто")
        bot.register_next_step_handler(msg, lot)

    elif message.text == "/stop":
        bot.send_message(message.chat.id, "Вы вышли из добовления новой машины")

    elif message.content_type == "photo":
        print(message)
        media = []
        for x in message.photo:
            print(x.file_id)
            media.append(x.file_id)
            bot.send_photo(message.chat.id, photo=x.file_id)
            # car_init_dict[message.chat.id].photo.append(x.file_id)
        print(lot_init_dict[message.chat.id].photo)

        with open('1.json', 'w', encoding='utf-8') as f:
            json.dump(dict, f, ensure_ascii=False, indent=4)

        # media_group = []
        # for num, file_id in enumerate(car_init_dict[message.chat.id].photo):
        #     media_group.append(InputMediaPhoto(media=file_id, caption=card_obj_car(car_init_dict[message.chat.id]) if num == 0 else ""))
        # bot.send_media_group(message.chat.id, media_group)

        # for num, url in enumerate(media):
        #     media_group.append(InputMediaPhoto(media=url, caption="11111111" if num == 0 else ''))
        # bot.send_media_group(message.chat.id, media_group)
    else:
        msg = bot.send_message(message.chat.id,
                               "что-то пошло не так, попробуй снова\nДля выхода пришли '/stop'\nДля обновления карточки пришли '/new_lot'")
        bot.register_next_step_handler(msg, photo_lot)


print("Ready")

bot.infinity_polling()