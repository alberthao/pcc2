#Author: Alberthao
#Topic: Input

sandwich_orders=['chicken salad sanwich','pastrami','egg sanwich','pastrami','turkey sanwich','pastrami']

print("I'sorry.The pastrami flavor sandwich has been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_orders=sandwich_orders[:]
print("\nThe following orders have been made:")
print(finished_orders)