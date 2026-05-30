def split_bill(tot,n):
    if(tot<0 or n<0):
        print('invalid')
    else:
        print(f'split per person {tot//n}')
tot=1250
n=4
split_bill(tot,n)           