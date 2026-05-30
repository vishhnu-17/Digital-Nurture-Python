def add(a,b):
    if(isinstance(a,int) and isinstance(b,int)):
        return a+b
   
try:
    
  a=add(int(input()),int(input()))
  
  
except:
    print('invalid number')        

