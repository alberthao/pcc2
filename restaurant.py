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
 
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['straberry','grape']
    
    def show_flavor(self):
        for flavor in self.flavors:
            print(f"We have {flavor}'s flvor icecream.")