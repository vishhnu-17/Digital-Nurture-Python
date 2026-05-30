def validate(user,pswrd):
    if(user=='' or pswrd==''):
        print('empty not allowed')
    elif(user=='admin'):
        if(pswrd=='pass123'):
            print('login success')
        else:
            print('invalid pswrd')
    else:
        print('invalid username')
        
validate(input(),input())                         