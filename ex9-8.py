#Author: Alberthao
#Topic: 类的知识

class User:
    """一次模拟餐馆的尝试。"""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        """模拟打印用户名称 """
        print(f"The user's first name is {self.first_name}.")
        print(f"The user's last name is {self.last_name}.")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}, nice to meet you.")

class Privileges:
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    """模拟管理员用户。"""
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()

user1 = Admin("Jack","Ma")
user1.greet_user()
user1.privileges.show_privileges()


