def if_demo():
    a = 5>7

    if a :
        print('a 是 Ture')

    else :
        print('a 是 Flase')


def elif_demo():
    a = 9
    if a==1:
        print('a是1')
    elif a==2:
        print('a是2')
    elif a==3:
        print('a是3')
    elif a==4:
        print('a是4')
    else:
        print('a不是1,2,3,4')

if __name__ == '__main__':
    elif_demo()