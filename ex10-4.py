#Author: Alberthao
#Topic: 文件的写入，file operation

filename='guest_book.txt'
name =""
with open(filename,'a') as file_object:
    while name !='q':
        name = input("Please input your name(q for quit):\n")
        if name == 'q':
            break
        else:
            print(f"Welcome {name}.")
            file_object.write(name+" has visited.\n")