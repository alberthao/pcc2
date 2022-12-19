# Author: Ablert Hao 
# Function: 测试if语句,和前一题解法一样。仅仅按照题目要求，修改了各个不同场景的输出
alien_color ='green'
if(alien_color=='green'):
    print('Hi, you got 5 points for this attack.')
elif(alien_color=='yellow'):
    print("You got 10 points for this attack.")
elif(alien_color=='red'):
    print("You got 15 points for this attack.")

#yellow的场景
alien_color ='yellow'
if(alien_color=='green'):
    print('Hi, you got 5 points for this attack.')
elif(alien_color=='yellow'):
    print("You got 10 points for this attack.")
elif(alien_color=='red'):
    print("You got 15 points for this attack.")

#red的场景,这个按照题目要求，增加了else语句，前面都是多个elif
alien_color ='red'
if(alien_color=='green'):
    print('Hi, you got 5 points for this attack.')
elif(alien_color=='yellow'):
    print("You got 10 points for this attack.")
elif(alien_color=='red'):
    print("You got 15 points for this attack.")
else:  
    print("Something wrong.")