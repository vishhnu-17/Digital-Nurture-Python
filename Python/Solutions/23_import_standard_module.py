import math
def area(r):
    if(r<0):
        print('invalid radius')
    else:
        print(f'area is {math.pi*r*r:.2f}')
area(60)      