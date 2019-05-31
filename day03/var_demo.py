avar = '雷猴'
def d1():
    print(avar)
def d2():
    global avar
    avar = '雷猴世界'
    print(avar)


if __name__ == '__main__':
    d1()
    d2()