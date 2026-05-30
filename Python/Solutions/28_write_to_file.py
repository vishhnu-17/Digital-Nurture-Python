def create(file):
    try:
     f=open(file,'w')
     f.write('hello world')
     print('successfully written')
     f.close()
    except:
        print('file not found') 
create('greet.txt')        
    