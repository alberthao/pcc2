# Author: Ablert Hao 
# Function: if elif else的练习,人的一生
current_users=['albert','mary','Jack','Tom','admin','jerry']
current_users_lower=[]
for user in current_users:
    current_users_lower.append(user.lower())

new_users=['albeRt','mary_li','JACK','Tom_Xu','George','Bill']


for user in new_users:
    if (user.lower() in current_users_lower):
        print(f"Hello {user}, You need to find a new name for you.")
    else:
        print(f'Hello {user.title()}, this name is not occupied.')
