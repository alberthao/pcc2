#Author: Alberthao
#Topic: Input

sandwich_orders=['chicken salad sanwich','egg sanwich','turkey sanwich']
finished_orders=[]

while sandwich_orders:
    current_order=sandwich_orders.pop()
    
    print(f"I made your {current_order}.")
    finished_orders.append(current_order)

print("\nThe following orders have been made:")
for finished_order in finished_orders:
    print(finished_order)