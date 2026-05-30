def eligible(m):
    if(m<0 or m>100):
        print('invalid marks')
    elif(m>=40):
        print('pass')
    else:
        print('fail')
eligible(int(input()))        
            