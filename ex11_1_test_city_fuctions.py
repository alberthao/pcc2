#Author: Alberthao
#Topic: 测试代码
# 存储要测试用例的代码。 


import unittest 
from ex11_1_city_fuctions import get_city_name
class NamesTestCase(unittest.TestCase): 
    """测试 ex11_1_city_fuctions。""" 
    def test_first_last_city(self): 
        """能够正确地处理像 如 Santiago, Chile 这样的地名吗？""" 
        formatted_name = get_city_name('Santiago', 'Chile') 
        self.assertEqual(formatted_name, 'Santiago, Chile') 

if __name__ == '__main__': 
    unittest.main() 
