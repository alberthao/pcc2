# Author: Ablert Hao 
# Function: To print what is my favorite number.
guests=['Lao Hao','Lao Li','Miss Hao']

for guest in guests:
    invite_message=f"Welcome {guest}, I'd like to invite you to have dinner with me this Sunday."   
    print(invite_message)

print("I am happy to announce that I have found a bigger table for us.")

guests.insert(0,'Lao Jia')
guests.insert(len(guests)-2,'Mr. Gao')
guests.append('Mrs. Gao')

for guest in guests:
    invite_message=f"Welcome {guest}, I'd like to invite you to have dinner with me this Sunday."   
    print(invite_message)


print("I'm sorry that I can only invite two person.")

while len(guests)>2:  #注意这里的判断语句，要保证列表留下来两个人
    person_not_attend=guests.pop()
    print(f'{person_not_attend}, sorry to inform you that I cannot invite you this Sunday.')

for guest in guests:
    invite_message=f"Welcome {guest}, I'd like to invite you to have dinner with me this Sunday."   
    print(invite_message)

del guests[1]  #从大往小删除，要不然下标会变
del guests[0]
if len(guests)==0:
    print("Now it's empty")