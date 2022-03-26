# Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений.
# Посчитать их количество.

import re
pic = re.compile(r'<img src=\"\w+\.bmp\" \w+=\"\d+\" \w+=\"\d+\">|<img src=\"\w+\.jpg\" \w+=\"\d+\" \w+=\"\d+\">|' 
                           r'<img src=\"\w+\.png\" \w+=\"\d+\" \w+=\"\d+\">')
with open('pazzl.html', 'r', encoding='utf-8') as file:
    text = file.read()
    have = re.findall(pic, text)
    print(have)
    print('Количество кодов изображений: ', len(have))