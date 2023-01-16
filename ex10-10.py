#Author: Alberthao
#Topic: 对文件异常的捕获和处理
# 读取本文件所在文件夹内的alice.txt,该文件从古藤堡计划下载，原书书名是Alice's Adventures in Wonderland


def count_files(filename, newword):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        occur_num = words.count(newword)
        print(f"The file {filename} has {occur_num} '{newword}'.")
        occur_num_all = 0
        for word in words:
            if word.lower() == newword.lower():
                occur_num_all += 1
        print(f"The file {filename} has {occur_num_all} '{newword}'. Every forms are included.\n")


filename = 'alice.txt'
count_files(filename,'row')
count_files(filename,'as')
count_files(filename,'As')