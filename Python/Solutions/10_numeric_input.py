def next_year_age(age):
    if(age<0):
        print('invalid')
    else:
        print(f'next year youll be {age+1}')
a=input()
if(a.isdigit()):
    next_year_age(int(a))
else:
    print('invalid input')                
    