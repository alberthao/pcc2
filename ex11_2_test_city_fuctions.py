#Author: Alberthao
#Topic: 测试代码
# 存储要测试用例的代码。 


import unittest 
from ex11_2_city_fuctions import get_city_name
class NamesTestCase(unittest.TestCase): 
    """测试 ex11_1_city_fuctions。""" 
    def test_first_last_city(self): 
        """能够正确地处理像 如 Santiago, Chile 这样的地名吗？""" 
        formatted_name = get_city_name('Santiago', 'Chile') 
        self.assertEqual(formatted_name, 'Santiago, Chile') 
    def test_first_last_middle_name(self): 
        """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗？""" 
        formatted_name = get_city_name( 
            'Santiago', 'Chile', 'population 5000') 
        self.assertEqual(formatted_name, 'Santiago, Chile - Population 5000')


if __name__ == '__main__': 
    unittest.main() 
