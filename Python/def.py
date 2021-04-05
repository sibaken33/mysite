#def sample_function(x, y):
def sample_function(arg1, arg2):
    print(arg1, arg2)

#z = sample_function(1, 2)
#print(z)

sample_function('a', 'b') #順番に引数を指定する
sample_function(arg1='c', arg2='d') #キーワードを指定する
sample_function(arg2='f', arg1='e') #キーワードを指定する

