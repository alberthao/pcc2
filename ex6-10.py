# Author: Ablert Hao 
# Function: 喜欢的数字

friends_favorite_num = {'cuikai':['0','6','8'],'li_na':['1','3','9'],'zhang_peng':['15'],'hao_shuai':['7','8','9']}


#省力些的做法
for key,value in friends_favorite_num.items():
    print(str(key).title()+"'s favorite numbers are "+str(value)+'.')