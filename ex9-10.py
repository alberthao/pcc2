#Author: Alberthao
#Topic: 类的知识，汽车类的拓展

"""restaurant.py里面保存了类所需的代码"""
from restaurant import Restaurant

my_restaurant = Restaurant("alibaba","Chinese")

print(f"My restaurant's name is {my_restaurant.restaurant_name}.")
print(f"My restaurant's cuisine type is {my_restaurant.cuisine_type}.")

my_restaurant.open_restaurant()
