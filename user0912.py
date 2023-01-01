#Author: Alberthao
#Topic: 类的知识
from admin0912 import User
"""Admin类需要引用到User类,所以这里需要导入"""

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


