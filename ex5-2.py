# Author: Ablert Hao 
# Function: 测试if语句
car = 'subaru' 
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru') 
 
print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi') 


# 检查两个字符串相等和不等。 
str1 = 'Nanjing'
str2 = 'nanjing'
if str1==str2:
    print("\nStr1 is equal to str2.")
else:
    print("\nStr1 is not equal to str2.")

# 使用方法lower()的测试。 
if str1.lower()==str2:
    print("\nStr1.lower is equal to str2.")
else:
    print("\nStr1.lower is not equal to str2.")

# 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。 
num1=1
num2=2
num3=1.000
if num1==num2:
    print('\nnum1 is equal to num2.')
else:
    print('\nnum1 is not equal to num2.')

if num1==num3:
    print('\nnum1 is equal to num3.')
else:
    print('\nnum1 is not equal to num3.')

# 使用关键字and和or的测试。 
if num1==num2 and num1==num3:
    print('\nnum1 is equal to num2 and num3.')
else:
    print('\nnum1 is not equal to num2 or num3.')

# 测试特定的值是否包含在列表中。 
lists=['dog','cat','elephant','kangaroo','panda','mouse','deer']
my_pet='dog'
if my_pet in lists:
    print("\nMy pet is in the zoo.")

# 测试特定的值是否未包含在列表中。
my_new_pet='Tortoise'
if my_new_pet not in lists:
    print("\nMy new pet is not in the zoo.")
