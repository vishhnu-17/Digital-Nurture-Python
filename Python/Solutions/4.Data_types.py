sal=float(input())
tax=float(input())
if sal<0:
    print('invalid salary')
if(tax<0):
    print('invalid tax')
def calc(sal,tax):
    return sal*(100-tax)            
amt=calc(sal,tax)
print(f'final sal {amt:.2f}')