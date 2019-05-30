# 新建一个字典变量,里面有两个键值对,访问一个值,删除一个键值对
# 添加一个键值对,更改任意一个值,再新建一个字典,将两个合并

adict = {'username':'hb','password':'123456'}
def dict_sel():
    print(adict['username'])

def dict_del():
    adict.pop('password')
    print(adict)

def dict_add():
    adict['age'] = 20
    print(adict)

def dict_updat():
    adict['username']='JK'
    print(adict)
    bdict={'list':[1,2]}
    adict.update(bdict)
    print(adict)

if __name__ == '__main__':
    dict_sel()
    dict_del()
    dict_add()
    dict_updat()