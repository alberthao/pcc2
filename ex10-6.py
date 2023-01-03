#Author: Alberthao
#Topic: 对异常的捕获和处理

print("Give me two numbers, and I'll add them.")
first_number = input("\nFirst number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("You can't input strings or fraction!")
else:
    print(answer)