# Author: Ablert Hao 
# Function: To print out numbers which are cubes of numbers from 1 to 10.
num_list=[]
for num in range(1,11):
    num=num**3
    num_list.append(num)

for num in num_list:
    print(num)

