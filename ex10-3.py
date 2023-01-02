#Author: Alberthao
#Topic: 文件的写入，file operation

filename='guest.txt'
with open(filename,'a') as file_object:
    name = input("Please input your name:\n")
    file_object.write(name+"\n")