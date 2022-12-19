# Author: Ablert Hao 
# Function: 序数词的表示

pet1 = {'name':'George','type':'cat','owner':'Bill'}
pet2 = {'name':'Lisa','type':'dog','owner':'Tom'}
pet3 = {'name':'Lily','type':'fish','owner':'Jack'}

pets=[pet1,pet2,pet3]
i=1
for pet in pets:
#下一节更省力些的做法
    for key,value in pet.items():
        print(f"{i}# pet's "+str(key)+" is "+str(value)+'.')
    print('\n')
    i=i+1