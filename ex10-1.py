#Author: Alberthao
#Topic: 文件的读取，file operation，读取的文件名为learning_python.txt，位于和本文件相同目录下

#方式1：读取整个文件的方式
with open('learning_python.txt') as file_object:
    contents = file_object.read()

print(contents)


#方式2：逐行读取文件的方式
filename='learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

#方式3：存列表再读取文件的方式
filename='learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())