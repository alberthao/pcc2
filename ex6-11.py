# Author: Ablert Hao 
# Function: 喜欢的数字

cities = {'nanjing':{'country':'China','population':600,'flower':'sunflower'},
          'Sydney':{'country':'China','population':800,'flower':'rose'},
          'seattle':{'country':'U.S.','population':600,'flower':'cacti'}
          }


#省力些的做法
for cityname,value in cities.items():
    print(f"\nCityname: {cityname}") 
    country = value['country'] 
    population = value['population'] 
    flower = value['flower'] 
 
    print(f"\tCountry: {country.title()}") 
    print(f"\tPopulation: {population}") 
    print(f"\tCity Flower: {flower.title()}") 