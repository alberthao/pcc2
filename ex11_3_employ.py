#Author: Alberthao
#Topic: 测试代码
# 存储要测试的代码。 


class Employee: 
    """收集匿名调查问卷的答案。""" 
    def __init__(self, first_name, last_name, annual_salary): 
        """存储员工名字、姓、年薪。""" 
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.responses = [] 

    def give_raise(self,salary_raise=5000): 
        """增加年薪""" 
        if salary_raise == 5000:
            self.annual_salary+=5000
        else:
            self.annual_salary+=salary_raise
        print(f"We have add {salary_raise},so your salary is now {self.annual_salary}") 