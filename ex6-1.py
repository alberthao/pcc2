# Author: Ablert Hao 
# Function: 序数词的表示

neighbour = {'first_name':'Albert','last_name':'Eienstein','age':15,'address':'New Jersy'}
print(neighbour['first_name'])
print(neighbour['last_name'])
print(neighbour['age'])
print(neighbour['first_name'])

#下一节更省力些的做法
for key,value in neighbour.items():
    print("This person's "+str(key)+" is "+str(value)+'.')