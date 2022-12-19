# Author: Ablert Hao 
# Function: 测试if语句,和前一题解法一样。仅仅按照题目要求，修改了未通过场景的输出
alien_color ='green'
if(alien_color=='green'):
    print('Hi, you got 5 points for this attack.')
else:
    print("I'm sorry, you got 10 points for this attack.")

#未通过的场景
alien_color ='yellow'
if(alien_color=='green'):
    print('Hi, you got 5 points for this attack.')
else:
    print("I'm sorry, you got 10 points for this attack.")