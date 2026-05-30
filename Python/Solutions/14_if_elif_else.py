def grades(score):
    if(score<0 or score>100):
        print('invalid')
    if(score>=90):
        print('A')
    elif score>=80 :
        print('B')
    else:
        print('C')
grades(88)        