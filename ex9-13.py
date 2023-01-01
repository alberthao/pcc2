#Author: Alberthao
#Topic: 类的知识，Die类
from random import randint
from random import choice

class Die:
    def __init__(self):
        self.sides=6

    def roll_die(self):
        self.sides=randint(1,20)   #这里的20就对应20面体，如果是6面体，就写randinit(1,6)
        print(self.sides)

my_die= Die()
my_die.roll_die()
