#Author: Alberthao
#Topic: 对文件异常的捕获和处理
# 读取本文件所在文件夹内的cats.txt和dogs.txt,其中animal.txt不存在，用于演示try:except

def read_files(filename):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(f"The file {filename} has following:\n{contents.title()}.")

filenames = ['cats.txt','dogs.txt','animal.txt']
for file in filenames:
    read_files(file)