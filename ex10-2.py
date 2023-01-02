#Author: Alberthao
#Topic: 文件的读取，file operation，读取的文件名为learning_python.txt，位于和本文件相同目录下

#逐行读取文件的方式
filename='learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        line = line.replace('Python','C')
        print(line.strip())
