def get_sum(a, b):
    """

    
    :param a: First param
    :param b: Second param
    :type a: int | float
    :type b: int | float
    :return: a + b
    :rtype: int
    """
    return a + b


print(get_sum(1, 2))
# print(help('print'))

# print(print.__doc__)
get_sum(1, 2)


def get_sum(a: int | float, b: int | float) -> int | float:
    return a + b


print(get_sum('a', 'b'))

print(get_sum(3, 2))

num1: int = 2
print(num1)
num1 = 'test'


list1: list[list[int]] = [[1, 2, 3]]
