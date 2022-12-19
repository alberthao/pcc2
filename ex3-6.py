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