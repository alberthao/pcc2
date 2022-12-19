# Author: Ablert Hao 
# Function: To print what is my favorite number.
guests=['Lao Hao','Lao Li','Miss Hao']

for guest in guests:
    invite_message=f"Welcome {guest}, I'd like to invite you to have dinner with me this Sunday."   
    print(invite_message)

print("I am sorry to announce that Miss Hao will not come this Sunday.")

guests.remove('Miss Hao')
guests.append('Lao Gao')

for guest in guests:
    invite_message=f"Welcome {guest}, I'd like to invite you to have dinner with me this Sunday."   
    print(invite_message)