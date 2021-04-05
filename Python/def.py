# 関数の定義


# def sample_function(x, y):
# def sample_function(arg1, arg2):
# def sample_function(arg1, *arg2):
# def sample_function(arg1, arg2 = 'x', arg3 = 'y'):
    print(arg1, arg2, arg3)


#z = sample_function(1, 2)
#print(z)



# sample_function('a', 'b') #順番に引数を指定する
# sample_function(arg1='c', arg2='d') #キーワードを指定する
# sample_function(arg2='f', arg1='e') #キーワードの場合は順番通りでなくてもよい


sample_function('a', 'b', 'c') #引数を全部指定している
sample_function('a', arg2 ='b') #3番目を省略できる
sample_function('a') #2,3番目を省略する
