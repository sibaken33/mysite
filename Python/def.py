# 関数の定義


# def sample_function(x, y):
# def sample_function(arg1, arg2):
# def sample_function(arg1, *arg2):
# def sample_function(arg1, arg2 = 'x', arg3 = 'y'):
# def sample_function(arg1, **arg2):

def sample_function(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)


#z = sample_function(1, 2)
#print(z)



# sample_function('a', 'b') #順番に引数を指定する
# sample_function(arg1='c', arg2='d') #キーワードを指定する
# sample_function(arg2='f', arg1='e') #キーワードの場合は順番通りでなくてもよい


# sample_function('a', 'b', 'c') #引数を全部指定している
# sample_function('a', arg2 ='b') #3番目を省略できる
# sample_function('a') #2,3番目を省略する

# sample_function('a', key1='x', key2='y', key3='z')
# sample_function('a', 'b', 'c', 'd', key1='x', key2='y', key3='z')

def sample_function1():
    """ 数値を返却 """
    return 1

def sample_function2():
    """ 何も返さない関数 """
    pass

def sample_function3():
    """ 複数の値を返却 """
    return 3, 'b'

x = sample_function1()
print(x)
y = sample_function2()
print(y)
a, b = sample_function3()
print(a, b)
