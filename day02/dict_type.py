import json

adict = {'username':'admin','password':'123456'}

def dict_sel():
    print(adict['password'])

def dict_updat():
    adict['username']='hb'
    print(adict)

def dict_del():
    adict.pop('password')
    print(adict)

def dict_add():
    # 增加
    adict['age']= 21
    print(adict)
    # 合并一
    bdict = {'list':[12,4],'tuple':[5,4]}
    adict.update(bdict)
    print(adict)
    # 合并二
    cdict ={'password':'77777','class':'1904'}
    ddict =dict(adict,**cdict)
    print(ddict)

def dict_zhuanhuan():
    dict_str="{'password':'77777','class':'1904'}"
    str_dict = json.dumps(adict)
    print(str_dict)
    print(type(str_dict))

if __name__ == '__main__':
    # dict_sel()
    # dict_updat()
    # dict_del()
    # dict_add()
    dict_zhuanhuan()
