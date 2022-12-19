# Author: Ablert Hao 
# Function: if elif else的练习,人的一生
user_accounts=['albert','mary','jack','Tom','admin','jerry']
for user in user_accounts:
    if (user == 'admin'):
        print("Hello admin, would you like to see a status report?")
    else:
        print(f'Hello {user.title()}, thank you for logging in again. ')
