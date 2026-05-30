def area(l,b):
    if(l<=0 or b<=0):
        print('invalid dimensions')
    else:
        return l*b
try:    
  ans=area(int(input()),int(input()))
  if(ans!=None):
      print(f'area {ans}')
except:
    print('invalid input')          