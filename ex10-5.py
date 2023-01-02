#Author: Alberthao
#Topic: 文件的写入，file operation

filename='program.txt'
love_reason =""
with open(filename,'a') as file_object:
    while love_reason !='q':
        love_reason = input("Please input the reason why you love programming.(q for quit):\n")
        if love_reason == 'q':
            break
        else:
            file_object.write(love_reason+"\n")