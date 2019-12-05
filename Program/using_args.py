def using_args(*args):
    return args
# By using args we can send multiple value with one parameter
# args is tuple


def using_kwargs(**kwargs):
    return kwargs
# kwargs is used when we use positional argument. It also take multiple value in single parameter
# kwargs is dictionary


print(using_args(1, 2, 3, 5))
print(using_kwargs(a=1, b=4, c=5, d=8))
