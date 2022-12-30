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

my_restaurant1 = Restaurant("alibaba","Hanzhou")
my_restaurant2 = Restaurant("tencent","Shenzhen")
my_restaurant3 = Restaurant("sohu","Beijing")


my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()