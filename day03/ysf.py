def yunsuan(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)


def bijiao(a,b):
    print(a==b)
    print(a != b)
    print(a>b)
    print(a<b)
    print(a<=b)
    print(a>=b)

def deng(a):
    a+=1
    print(a)
    a-=1
    print(a)
    a/=1
    print(a)
    a*=1
    print(a)




if __name__ == '__main__':
    yunsuan(8,2)
    bijiao(7,1)
    deng(7)