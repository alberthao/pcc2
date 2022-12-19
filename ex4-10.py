# Author: Ablert Hao 
# Function: To print out numbers which are cubes of numbers from 1 to 10.
num_list=[num**3 for num in range(1,11)]

print("The first three items in the list are:",num_list[0:3])
print("Three items from the middle of the list are:",num_list[4:7])
print("The last three items in the list are:",num_list[-3:])