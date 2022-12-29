#Author: Alberthao
#Topic: Function

# start from here
def build_car(merchant,model, **car_info):
    car_info['merchant'] = merchant
    car_info['model'] = model
    return car_info

car_profile = build_car('Audi','A6', prod_location='Shanghai', Color='Blue')
print(car_profile)