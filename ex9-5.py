#Author: Alberthao
#Topic: 类的知识

class User:
    """一次模拟用户的尝试。"""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        """登录次数自动加1 """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """模拟打印用户名称 """
        self.login_attempts = 0

    def describe_user(self):
        """模拟打印用户名称 """
        print(f"The user's first name is {self.first_name}.")
        print(f"The user's last name is {self.last_name}.")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}, nice to meet you.")

user1 = User("Jack","Ma")
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"user1 has login for {user1.login_attempts} times." )

user1.reset_login_attempts()
print(f"user1 has login for {user1.login_attempts} times." )