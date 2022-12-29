#Author: Alberthao
#Topic: Function

# start from here
def build_profile(first,last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','hao', location='nanjing,china', field='electrical engineering',language='Chinese')
print(user_profile)