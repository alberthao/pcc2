#Author: Alberthao
#Topic: 读取或存储文件，用文件保存用户数据
#先要运行ex10-11-1.py，然后再运行本程序，否则json会报错。

import json

filename = "favorite_no.json"
with open(filename) as f:
    favorite_number = json.load(f)
    print(f"We remember your favorite number, it is {favorite_number}!")