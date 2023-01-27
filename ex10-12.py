#Author: Alberthao
#Topic: 读取或存储文件，用文件保存用户数据
# 如果以前存储了数字，就加载它。 
# 否则，提示用户输入数字并存储它。 

import json  
 
def get_stored_username(): 
    """如果存储了用户名，就获取它。""" 
    filename = 'username.json' 
    try: 
        with open(filename) as f: 
            username = json.load(f) 
    except FileNotFoundError: 
       return None 
    else: 
        return username 
 
def get_new_username(): 
    """提示用户输入用户名。""" 
    username = input("What is your name? ") 
    filename = 'username.json' 
    with open(filename, 'w') as f: 
        json.dump(username, f) 
    return username 
 
def greet_user(): 
    """问候用户，并指出其名字。""" 
    username = get_stored_username()
    username_true = input(f"Is this name '{username}' your name?(Yes/No): ") 
    if username_true.lower() =="yes" or username_true.lower() =="y": 
        print(f"Welcome back, {username}!") 
    else: 
        username = get_new_username() 
        print(f"We'll remember you when you come back, {username}!") 
 
greet_user() 