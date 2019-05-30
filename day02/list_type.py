

# alist = ['你好',1,'美国',0,8,9,6,4,72,1]
#
# def list():
#     print(alist[2])
#     print(alist[-3])
#     print(alist[4:])
#     print(alist[5:8])
#
# def list_del():
#     # alist.pop()
#     alist.pop(3)
#     print(alist)
#
# def list_add():
#     blist = [12,54,65,'2']
#     blist.append('5')
#     blist.append(7)
#     clist = ['5',8,2,4]
#     blist.extend(clist)
#     print(blist)
#
#
# def list_update():
#     dlist = [16,647,1654,116,114,98]
#     dlist[2]=200
#     dlist[3]=100
#     print(dlist)
#
#
# def list_order_by():
#     vlist = [16, 647, 1654, 116, 114, 98]
#     vlist.sort()
#     print(vlist)
#     vlist.sort(reverse=True)
#     print(vlist)
#
#
# def list_distinct():
#     jlist = [1,5,4,2,2,4,6,6,7,8,9,5,4,1,2,3,4,5]
#     # jlist = set(jlist)
#     jlist = set(jlist)
#     print(jlist)
#     print(len(jlist))


# 新建一个list变量，里面有五个元素，访问索引2，切片访问索引1到4，删除索引3，添加两个元素，第0位元素改成字符5，获取索引长度
alist = [1,2,3,4,5]
def list():
    print(alist[2])
blist = [1,2,3,4,5]
def list_2():
    print(blist[0:4])
clist = [1,2,3,4,5]
def list_3():
    clist.pop(3)
    print(clist)

dlist = [1, 2, 3, 4, 5]
def list_4():
    dlist[0]='5'

flist = [1, 2, 3, 4, 5]
def list_5():
    hlist = [6,7]
    flist.extend(hlist)
    print(flist)


glist = [1, 2, 3, 4, 5]
def list_6():
    print(glist)
    print(len(glist))


if __name__ == '__main__':

    list()
    list_2()
    list_3()
    list_4()
    list_5()
    list_6()