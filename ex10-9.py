#Author: Alberthao
#Topic: 对文件异常的捕获和处理
# 读取本文件所在文件夹内的cats.txt和dogs.txt,其中animal.txt、lalala.txt不存在，用于演示try:except
# 静默异常

def read_files(filename):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"The file {filename} has following:\n{contents.title()}.")

filenames = ['dogs.txt','cats.txt','animal.txt','lalala.txt']
for file in filenames:
    read_files(file)