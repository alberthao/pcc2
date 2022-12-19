# Author: Ablert Hao 
# Function: 朋友们最喜欢的数字

glossaries = {'dictionary':'a collection of key-value pairs. ',
              'list':'a collection of items in a particular order.',
              'tuple':'an immutable list.',
              'loop':'one of the most common ways a computer automates repetitive tasks.',
              'set':'a collection in which each item must be unique.',
              'function':'a blocks of code which can perform a particular task that you\'ve defined in it.',
              'class':'a way by which you can represent real-world things and situations, and you create objects based on these classes.'}

#用这种方法方便些，就不用那种一个关键词一个关键词的打印的笨办法了
for key,value in glossaries.items():
    print('A '+str(key)+" is "+str(value))