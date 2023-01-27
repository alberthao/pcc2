#Author: Alberthao
#Topic: 读取或存储文件，用文件保存用户数据

import json

favorite_number = input("What is your favorate number?")

filename = "favorite_no.json"
with open(filename,'w') as f:
    json.dump(favorite_number,f)
    print(f"We'll remember your favorite number when you come back!")