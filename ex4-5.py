# Author: Ablert Hao 
# Function: To print what is my favorite number.
num_list=[]

for i in range(1,1000001):
    num_list.append(i)
    
print("The minimum number is: ", min(num_list))
print("The maximum number is: ", max(num_list))
print("The sum of all of the number is: ", sum(num_list))