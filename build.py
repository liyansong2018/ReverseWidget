# -*- coding: utf-8 -*-
import shutil
import os

def add_pic_path(file):
    '''
    Modify python file from QT Designer for adding complete resources path
    :param file: `.py` converted by `.ui`
    :return: null
    '''
    file_data = ''
    need_update = False
    try:
        with open(file, 'r', encoding='utf-8') as fp:
            for line in fp:
                if 'QPixmap' in line:
                    if 'ui/resources/pictures' not in line:
                        need_update = True
                        replaced = line.replace('resources/pictures', 'ui/resources/pictures')
                        print('[+] ' + replaced.strip())
                        file_data += replaced
                    else:
                        file_data += line
                else:
                    file_data += line
        if need_update:
            with open(file, 'w', encoding='utf-8') as fp:
                fp.write(file_data)
    except Exception as e:
        print(e)


def mov_lang():
    '''
    Move language file to resources directory
    :return: null
    '''
    ts_path = os.getcwd() + '/ui/'
    ts_path_new = ts_path + 'resources/language/'
    for file in os.listdir(ts_path):
        if '.qm' in file:
            print("[+] " + file)
            if os.path.isfile(ts_path_new + file):
                os.remove(ts_path_new + file)
            shutil.move(ts_path + file, ts_path_new)


# Modify pic path
add_pic_path('ui/main_window.py')
add_pic_path('ui/about_window.py')
add_pic_path('ui/format_window.py')
add_pic_path('ui/hash_window.py')
add_pic_path('ui/appchecker_window.py')

# Move language file
mov_lang()
