#Author: Alberthao
#Topic: Input

person_max =int(input("How many people are there in your group?"))
if person_max > 8:
    message = f"I'm sorry we have no more seat here."
    print("\n"+message)