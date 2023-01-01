#Author: Alberthao
#Topic: 类的知识，彩票类
import random
from random import randint
from random import choice

class Lottery:
    def __init__(self):
        self.lottery_list=['a','b','l','e','t','0','1','2','3','4','5','6','7','8','9']

    def roll_lottery(self):
        self.results=random.sample(self.lottery_list,4)   #这里的4就对应返回多少个数字
        print(self.results)

    def roll_win(self):
        if self.results == ['a','b','3','5']:
            print("You win.")
        else:
            print('Not win. Go on!')

my_lottery= Lottery()
my_lottery.roll_lottery()
my_lottery.roll_win()
