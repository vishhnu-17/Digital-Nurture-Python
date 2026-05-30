def check_cart(l):
    if(len(l)==0):
        print('invalid cart')
    for i in range(len(l)):
        if(l[i]<0):
            print('invalid item')
            break
        else:
            print('items are',l[i])
check_cart(eval(input()))            