# Author: Ablert Hao 
# Function: 复制列表,要区分切片复制和
pizzas=['Pepperozi','Strawberry','Grape']
friend_pizzas=pizzas[:]

pizzas.append('Stawberry')
friend_pizzas.append('Apple')
print('My favorite pizzas are:', pizzas)
print('My friend’s favorite pizzas are:', friend_pizzas)