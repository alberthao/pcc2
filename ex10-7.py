#Author: Alberthao
#Topic: 对异常的捕获和处理

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't input strings or fraction!")
    else:
        print(answer)