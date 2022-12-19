# Author: Ablert Hao 
# Function: 复制列表,要区分切片复制和
food_in_menu=('Fried potato','cucumber','stewed beancurd with spinach','roast Beijing duck')

for food in food_in_menu:
    print(food)

#food_in_menu[0]='aaa'  #这一行的确会报错
print('\nWe renewed our menu as follow:')

food_in_menu=('Fried potato','Ice cream','stewed beancurd with spinach','roast Beijing chicken')
for food in food_in_menu:
    print(food)