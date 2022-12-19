# Author: Ablert Hao 
# Function: 序数词的表示

favorite_places = {'zhangsan':['Guilin','Qufu','Xian'],'lisi':['Nanjing Fuzimiao','Taishan'],'Wangwu':['Tianmen Square','Tian Temple','Summer Palace']}

for key,value in favorite_places.items():
#下一节更省力些的做法
    for place in value:
        print(f"{key}'s favorite palce has:",place)
    print('\n')