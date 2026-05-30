def read(file):
    try:
        f=open(file,'r')
        print(f.read())
        print('contents read')
    except FileNotFoundError:
        print('file not found')
read('greet.txt')            