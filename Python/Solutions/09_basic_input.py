def greet(name):
    if(len(name.strip())==0):
        print('invalid')
    else:
        print(f'hi {name}')
greet(input())            