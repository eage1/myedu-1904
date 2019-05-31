def for_demo():
    for i in range(6):
        print('hello world')

def for_demo2():
    for i in range(1,50,2):
        print(i)

def for_list():
    alist = ['1','5','6','7','8','窝',1,2,3]
    for b in alist:
        print(b)
    for b in range(len(alist)):
        print(b)

def for_for():
    for i in range(1,10):
        for o in range(1,i+1):
            print('%sx%s=%s'%(i,o,i*o),end=',')
        print('\n')

def jishu():
    for i in range(5):
        print(i)
        if i ==2:
            break

def for_for4():
    for i in range(1,10):
        for o in range(1,i+1):
            print('%sx%s=%s'%(i,o,i*o),end=',')
        print('')


if __name__ == '__main__':
    for_for4()