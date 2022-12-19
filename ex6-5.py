# Author: Ablert Hao 
# Function: 朋友们最喜欢的数字

rivers = {'nile':'Egypt',
          'yellow river':'China',
          'mississippi River':'U.S',
          'St.Lawrence River':'Canada'}

#用这种方法方便些，就不用那种一个关键词一个关键词的打印的笨办法了
for key,value in rivers.items():
    print("The "+str(key).title()+" runs through "+str(value)+'.')