def ijf_a():
    try:
        a=5/0
    except:
        print('报错了')

if __name__ == '__main__':
    ijf_a()
    try:
        print('错误之前')
        a=5/1
        print('错误之后')
    except:
        print('报错了')

    print('123')