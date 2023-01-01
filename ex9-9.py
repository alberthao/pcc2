#Author: Alberthao
#Topic: 类的知识，汽车类的拓展

class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一条消息，之处汽车的里程"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值。
        拒绝将里程往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer.")
    
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    
    def  describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 200
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    def __init__(self, make, model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()