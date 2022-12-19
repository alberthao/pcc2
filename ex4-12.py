# Author: Ablert Hao 
# Function: 复制列表,要区分切片复制和
pizzas=['Pepperozi','Strawberry','Grape']
friend_pizzas=pizzas[:]

pizzas.append('Stawberry')
friend_pizzas.append('Apple')

for pizza in pizzas:
    print('This is original: ',pizza)


for pizza in friend_pizzas:
    print('This is friend: ',pizza)

        