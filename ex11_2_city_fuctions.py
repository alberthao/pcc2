#Author: Alberthao
#Topic: 测试代码
# 存储要测试的代码。 


def get_city_name(city,country,population=''): 
    """生成整洁的城市名和国家名""" 
    if population: 
        full_name = f"{city}, {country} - {population}"  
    else: 
        full_name = f"{city}, {country}" 
    return full_name.title() 
 
