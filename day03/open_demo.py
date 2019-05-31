def open_write():
    text_io=open('test.txt','w+')
    for i in range(5):
        text_io.write('雷猴123123123\n')

def open_write1():
    text_io=open('test.txt','a+')
    for i in range(5):
        text_io.write('雷猴123123123\n')

def gfdss():
    text_io=open('tess.txt','w+')
    for i in range(10):
        text_io.write('lei123\n')

def dfdw():
    text_io = open('tess.txt','r')
    # print(text_io.readlines())
    print(text_io.readline())


if __name__ == '__main__':
    dfdw()
