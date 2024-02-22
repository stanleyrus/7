def fn1():
    return 'Hello from my_module'


def fn3():
    return f'Hello 2 from {__name__}'


test_var = 'TEST VAR'

if __name__ == '__main__':
    print(fn3())
