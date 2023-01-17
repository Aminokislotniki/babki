from telebot.types import InputMediaPhoto
from variables import id_chanel
from variables import bot
# Вывод обьявления в канал, по ID

# [Массив картинок(ссылок или пути)][Описание][Город][Условия доставки][ID - администратора(который создал лот)][Стоимость]

def posting_ad_by_ID(id_lot):
    #lot =  obj_DB.find(id_lot)     создаем обьект/массив найденой строчки из DB

    text = f' {lot[2]}\n' \
           f' {lot[3]}\n' \
           f' {lot[4]}\n' \

    bot.send_photo(id_chanel, photo=lot[1][0], caption=text,reply_markup= ??????)

    # Если медиа групп
    # media_group = []
    # for num, url in enumerate(lot[1]):
    #    media_group.append(InputMediaPhoto(media=url, caption = text if num == 0 else ''))
    #    bot.send_media_group(id_chanel, media_group)

