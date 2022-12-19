# Author: Ablert Hao 
# Function: 序数词的表示

neighbour1 = {'first_name':'Albert','last_name':'Eienstein','age':15,'address':'New Jersy'}
neighbour2 = {'first_name':'Jack','last_name':'Chen','age':45,'address':'New Jersy'}
neighbour3 = {'first_name':'Bill','last_name':'Gates','age':66,'address':'Seattle'}

people=[neighbour1,neighbour2,neighbour3]
i=1
for neighbour in people:
#下一节更省力些的做法
    for key,value in neighbour.items():
        print(f"{i}# person's "+str(key)+" is "+str(value)+'.')
    print('\n')
    i=i+1