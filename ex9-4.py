#Author: Alberthao
#Topic: 类的知识

class Restaurant:
    """一次模拟餐馆的尝试。"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """模拟打印餐馆名称 """
        print(f"The restaurant'name is {self.restaurant_name}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is opening.")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,number_served):
        self.number_served += number_served
 
my_restaurant = Restaurant("alibaba","Chinese")

print(f"My restaurant's name is {my_restaurant.restaurant_name}.")
print(f"My restaurant's cuisine type is {my_restaurant.cuisine_type}.")

my_restaurant.set_number_served(230)
print(f"{my_restaurant.number_served} has/have been to this restaurant.")

my_restaurant.increment_number_served(100)
print(f"{my_restaurant.number_served} has/have been to this restaurant.")

my_restaurant.describe_restaurant()

