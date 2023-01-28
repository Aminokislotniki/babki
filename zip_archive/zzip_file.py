import zipfile
import os
import time
import threading

zip_path = 'C:\\Новая папка\\git_auktion' # путь по которому созоется файл.zip(нужно указать свой путь)
zip_paht_del = 'C:\\Новая папка\\git_auktion' # удаляет в архиве весь путь сохраняя структуру(чтоб не создавались лишние папки)
def arhiv(time_):
    while True:
        t = time.ctime()
        file_zip = zipfile.ZipFile(f'{str("дата: "+t[0:10]+t[19:]+" время: "+t[10:19]).replace(" ",":").replace(":", ".")}.zip', 'w')
        for folder, subfolders, files in os.walk(zip_path):
            for file in files:
                    if file.endswith('.json'):
                        print(file)
                        file_zip.write(os.path.join(folder, file),
                                       os.path.relpath(os.path.join(folder, file),zip_paht_del ),
                                       compress_type=zipfile.ZIP_DEFLATED)


        file_zip.close()
        print(file_zip)
        time.sleep(time_)

t = threading.Thread(target=arhiv, args=(100,))# 100 время на которое функция засыпает
t.start()


