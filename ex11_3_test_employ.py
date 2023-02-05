#Author: Alberthao
#Topic: 测试代码
# 存储要测试的代码。 


import unittest 
from ex11_3_employ import Employee

class TestEmployee(unittest.TestCase): 
    """针对 Employee 类的测试。""" 
    def setUp(self): 
        """创建一个调查对象和一组答案，供使用的测试方法使用""" 
        first_name = "albert"
        last_name = "hao"
        annual_salary = 120000
        self.MyEmployee = Employee(first_name,last_name, annual_salary)


    def test_give_default_raise(self):
        self.MyEmployee.give_raise()
        self.assertEqual(self.MyEmployee.annual_salary,125000)
    
    def test_give_custom_raise(self):
        self.MyEmployee.give_raise(3000)
        self.assertEqual(self.MyEmployee.annual_salary,123000)
    
if __name__ == '__main__': 
    unittest.main() 