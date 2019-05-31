import os
if __name__ == '__main__':
    p=os.getcwd()
    print(p)
    q=os.path.abspath('..')
    print(q)
    w=os.path.abspath('../../..')
    print(w)