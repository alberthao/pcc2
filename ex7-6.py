#Author: Alberthao
#Topic: Input

age=""
retry = True
fee = 0
while retry:
        age =input("How old are you?\n")
        
        if age == 'quit':
            break
        elif int(age) <=3:
            fee=0
            message=f"Your fee is {fee}. Hope you can enjoy this trip."
            print(message+"\n")
        elif int(age) <=12:
            fee=10
            message=f"Your fee is {fee}. Hope you can enjoy this trip."
            print(message+"\n")
        elif int(age) >12:
            fee=15
            message=f"Your fee is {fee}. Hope you can enjoy this trip."
            print(message+"\n")

 
        
