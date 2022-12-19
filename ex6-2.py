# Author: Ablert Hao 
# Function: 朋友们最喜欢的数字

friends_favorite_num = {'cuikai':'0','li_na':'1','zhang_peng':'15','hao_shuai':'7'}


#下一节更省力些的做法
for key,value in friends_favorite_num.items():
    print(str(key).title()+"'s favorite number is "+str(value)+'.')