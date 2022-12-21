#Author: Alberthao
#Topic: Input

ingridiant=""
while ingridiant !='quit':
        ingridiant =input("What is your favorite pizza flavor?\n")
        message = f"We will add {ingridiant} to our pizza and I hope you will like it."
        if ingridiant != 'quit':
            print(message+"\n")
        
