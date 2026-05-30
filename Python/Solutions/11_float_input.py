def kg_pounds(w):
    if(w<0):
        print('invalid')
    else:
        print(f'kg to pound is {w* 2.20462}')  
w=input('enter weight')
try:
    kg_pounds(float(w))
except ValueError:
    print('enter valid float weight')              