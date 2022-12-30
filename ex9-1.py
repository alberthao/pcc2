#Author: Alberthao
#Topic: 类的知识

class Restaurant:
    """一次模拟餐馆的尝试。"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """模拟打印餐馆名称 """
        print(f"The restaurant'name is {self.restaurant_name}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is opening.")

my_restaurant = Restaurant("alibaba","Chinese")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()