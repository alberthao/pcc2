#Author: Alberthao
#Topic: Function

def make_shirt(size,logo="I love Python"): #我们用def表示定义函数,并为logo设置初始值
    """"""
    print(f"This T-shirt is Size {size} and we will print \"{logo}\" on it.")

make_shirt('Big size')
make_shirt(size='middle size')
make_shirt(size='small size',logo="Let's make the world beautiful.")