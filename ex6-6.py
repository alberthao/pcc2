# Author: Ablert Hao 
# Function: 朋友们最喜欢的数字

favorite_languages = { 
    'jen': 'python',  
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    } 
person_should_interview=['jen', 'sarah','tom','jack','bill', 'edward', 'phil']
#取消下一行的注释，可以尝试一下set的功能，注意，集合可以快速的取回不重复值，集合可以通过list()转为list
#print(set(favorite_languages.values()))
#print(list(set(favorite_languages.values())))

for person in person_should_interview:
    if person in favorite_languages.keys():
        print(f'Hi, {person.title()}, Thank you for having take the interview.')
    else:
        print(f'Hi, {person.title()}, Will you please take an interview as soon as possible?')