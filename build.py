# MIT License
#
# Copyright (c) 2021 Yansong Li
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Modify resource path in `ui` file created by: PyQt5 UI code generator 5.15.4.

Use it after we modify `ui` file by PyQt Designer.
"""
"""修改PyQt Designer自动生成的Python文件里的资源路径，以及统一语言文件的路径。

在每次修改UI后运行。
"""

# -*- coding: utf-8 -*-
import shutil
import os

def add_pic_path(file):
    """
    Modify python file from QT Designer for adding complete resources path
    :param file: `.py` converted by `.ui`
    :return: null
    """
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


def mov_lang(src, dst):
    """
    Move language file to resources directory
    :param src: source path
    :param dst: destination path
    :return: null
    """
    for file in os.listdir(src):
        if '.qm' in file:
            print("[+] " + file)
            if os.path.isfile(dst + file):
                os.remove(dst + file)
            shutil.move(src + file, dst)


# Modify pic path
add_pic_path('ui/main_window.py')
add_pic_path('ui/about_window.py')
add_pic_path('ui/format_window.py')
add_pic_path('ui/hash_window.py')
add_pic_path('ui/appchecker_window.py')
add_pic_path('ui/pechecker_window.py')
add_pic_path('ui/comment_window.py')

# Move language file
src = os.getcwd() + '/ui/'
dst = src + 'resources/language/'
mov_lang(src, dst)

src = os.getcwd() + '/'
dst = src + '/ui/resources/language/'
mov_lang(src, dst)
