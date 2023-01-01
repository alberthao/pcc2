#Author: Alberthao
#Topic: 类的知识，汽车类的拓展

from admin0912 import User
"""admin0912.py里面保存了user类所需的代码"""
from user0912 import Privileges, Admin
"""user0912.py里面保存了privileges、admin类所需的代码"""
"""user0912.py里面还需要导入依赖的User类"""

user1 = Admin("Jack","Ma")
user1.greet_user()
user1.privileges.show_privileges()
