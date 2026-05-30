def check(n,m):
    try:
        print(n/m)
    except ZeroDivisionError:
        print('division by zero')    
check(int(input()),int(input()))        