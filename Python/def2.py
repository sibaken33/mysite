"""　オブジェクトとしての関数 """
# def sanple_function():
#     text = 'sample'
#     print(text)
#     retrun '戻り値'

# text = sample_function()
# print(text)

# f = sample_function()
# print(text)

# f = sample_function

# text = f()
# print(text)

def param_func():
    return 'sample'

def sample_function(f):
    x = f()
    print(x)


sample_function(param_func)