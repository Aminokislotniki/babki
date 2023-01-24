import time
import json


f = open('lots/35.json', 'r', encoding='utf-8')
dict_lot = json.loads(f.read())
f.close()

time_today=(int(time.time()))
time_break=""
for z in dict_lot:
    for x in dict_lot[z]:
        if x =="time_create":
            time_break+=str(dict_lot[z][x])
print(time_break)
c=time_today-int(time_break)
print(c)
    # if c > 0:
    #     c = (time.ctime(c))
    #     bot.answer_callback_query(call.id, "Время окончания аукциона:" + c, show_alert=False)
    # else:
    #     bot.answer_callback_query(call.id, "Аукцион уже закончен, участие невозможно" + c, show_alert=False)