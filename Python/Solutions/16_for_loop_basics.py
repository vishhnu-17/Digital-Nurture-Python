def print_numbers(n):
    if(n<0):
        print('invalid range')
    else:
        for i in range(n):
            print(i+1)
print_numbers(int(input()))                