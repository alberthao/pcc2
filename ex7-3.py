#Author: Alberthao
#Topic: Input

my_no =int(input("What is your favorite number?"))
if my_no%10==0:
    message = f"Your favorite number {my_no} and it can be divided by 10."
    print("\n"+message)
else:
    message = f"Your favorite number is {my_no} and it can NOT be divided by 10."
    print("\n"+message)