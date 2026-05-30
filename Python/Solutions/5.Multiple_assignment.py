def display_coordinates():
    try:
     tup=(int(input()),int(input()))
    except:
        print('invalid')
    else:
        x,y=tup
        print(f'x {x} y {y}')
display_coordinates()            
    
    