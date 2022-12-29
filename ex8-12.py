#Author: Alberthao
#Topic: Function

# start from here
def make_sandwiches(*flavors):
    print("\nMaking a sandwich with the following ingrediants:")
    for flavor in flavors:
        print(f"-{flavor}")

make_sandwiches("apples","grape","chicken")

make_sandwiches("pork","beef","chicken","sugar")

make_sandwiches("chicken")

