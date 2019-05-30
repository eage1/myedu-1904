a = 5
#def：声明方法的关键字；int_demo:方法的名字；（）：下面写方法的内容
def int_demo():
    #声明一个变量=前面是变量名aint，=后面是变量值，int类型的5
    aint = 5

    #type(aint):获取aint的数据类型（变量类型），print：打印出他的类型
    print(type(aint))


# def：声明方法的关键字；astr_demo:方法的名字；（）：下面写方法的内容
def astr_demo():
    # 声明一个变量=前面是变量名astr，=后面是变量值，astr类型的'5'
    astr ='5'


    # type(astr):获取astr的数据类型（变量类型），print：打印出他的类型
    print(type(astr))


# print(type(xxx(xxx)))
def type_zhuanhuanh():
    b = '5'
    print(type(int(b)))

# 字符串 转换成 数字类型
def type_zhuanhuan():
    b='100'
    print(type(b))
    b = int(b)
    print(type(b))


def float_demo():#局部变量 全局变量
    afloat = 1.1
    print(type(afloat))


def str_join():
    a =123
    b = '你好'
    c = 5.88
    print(str(a)+b+str(c))
# 如果有其他类型，第一种：需要用str（）方法转换成str 类型才能用+连接

def str_joino():
    a = 123
    b = '你好'
    c = '哈喽'
    # 如果两个变量都是字符串类型，直接用 + 连接
    print(str(a)+b+c)

def str_joint():
    a =123
    b = '你好BGO'
    c = 5.88
    print('a是%s,b是%s,c是%s'%(a,b,c))

# 方法中括号里面的东西叫参数，多个参数用，分隔开
def add(num1,num2):
    print(num1)
    print(num2)
    print(num1+num2)
    # 返回参数
    return num1+num2


#这是一个main方法，可以直接执行，main方法下面不能再有其他方法
if __name__ == '__main__':
    #打印
    print("Hello World")

    print ('Hello, Python!')

    #调用方法：写方法名字加（）
    # int_demo()
    #
    # astr_demo()
    #
    # float_demo()
    #
    # type_zhuanhuan()
    #
    # type_zhuanhuanh()
    #
    # str_join()
    #
    # str_joino()
    #
    # str_joint()
    # add(45,95682)是有返值 所以a的值就是95727
    a = add(45,95682)+3
    print('-----------')
    print(a)
    print(type(a))


    print('-----------')
    b = str_joino()
    print(b)
    print(type(b))

    a = add('你好','漫威')
    print(type(a))
    print(a[2])






