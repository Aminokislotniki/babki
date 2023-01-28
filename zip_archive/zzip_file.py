import zipfile
import os
import time
import threading


def arhiv():
    while True:
        t = time.ctime()
        file_zip = zipfile.ZipFile(f'{str("дата: "+t[0:10]+t[19:]+" время: "+t[10:19]).replace(" ",":").replace(":", ".")}.zip', 'w')
        for folder, subfolders, files in os.walk('C:\\Новая папка\\git_auktion'):# НУЖНО УКАЗАТЬ ПУТЬ
            for file in files:
                    if file.endswith('.json'):
                        print(file)
                        file_zip.write(os.path.join(folder, file),
                                       os.path.relpath(os.path.join(folder, file), 'C:\\Новая папка\\git_auktion'),# НУЖНО УКАЗАТЬ ПУТЬ
                                       compress_type=zipfile.ZIP_DEFLATED)


        file_zip.close()
        print(file_zip)
        time.sleep(100)

t = threading.Thread(target=arhiv())
t.start()


