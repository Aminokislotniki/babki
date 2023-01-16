import gspread
import sqlite3 as sl


gc = gspread.service_account(filename="calm-vine-332204-924334d7332a.json")
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1k4ZGEXPsrz6mrV4Nh0JlEXuGGpX93Txk0C_66uh5IdI/edit?usp=sharing')
worksheet = sht2.sheet1
list_of_lists = worksheet.get_all_values()

with sl.connect('auction.db') as con:
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS lot''')
    cur.execute('''CREATE TABLE IF NOT EXISTS lot(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    марка TEXT,
    модель TEXT,
    картинка BLOB,
    год_выпуска TEXT,
    объем_двигателя TEXT,
    тип_двигателя TEXT,
    пробег TEXT, 
    тип_авто TEXT,
    цена TEXT,
    местонахождение TEXT,
    VIN TEXT,
    все_фото BLOB,
    description TEXT,
    id_car INTEGER
    )''')
    for i in list_of_lists[1:51]:
        cur.execute(f'''INSERT INTO lot(марка, модель,картинка ,год_выпуска ,объем_двигателя,тип_двигателя,
        пробег, тип_авто,цена,местонахождение,VIN ,все_фото ,description ,id_car )
         VALUES("{i[0]}","{i[1]}","{i[2]}", "{i[3]}", "{i[4]}","{i[5]}","{i[6]}","{i[7]}", "{i[8]}", "{i[9]}",
        "{i[10]}","{i[11]}", "{i[12]}",{i[13]} )
    ''')
    cur.execute('''SELECT *FROM lot''')
    for result in cur:

        print(result)

    cur.execute('''DROP TABLE IF EXISTS users''')
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    user_id INTEGER
        
        )''')
