def assert_int():
    a = '成功'
    b = '操作成功'
    c = 1>5
    try:
        assert a in b
        assert c
    except:

        print('断言失败')

if __name__ == '__main__':
    assert_int()