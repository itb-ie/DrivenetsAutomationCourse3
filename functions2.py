# create our own functions

def our_function():
    """
    This is my first function, it does nothing, just pass
    :return: None
    """
    pass  # this is an empty function


def our_function2(name):
    """
    This is my second function, it prints hello {name}
    This second function now has an argument
    :arg name: the name of the person to greet
    :return: None
    """
    print(f"Hello {name}!")


help(our_function2)
our_function2("Jane")


def our_function3(a, b, c):
    """
    Adds a, b, c and prints the result
    :param a: first value
    :param b: second value
    :param c: third value
    :return: None
    """
    result = a + b + c
    print(f"the result of adding: {a}, {b}, {c} is {result}")


our_function3(1, 2, 3)


def our_function4(a, b, c):
    """
    Adds a, b, c and returns the result
    :param a: first value
    :param b: second value
    :param c: third value
    :return: the result of a+b+c
    """
    result = (a + b) * c
    return result


result = our_function4(10, 20, 30)
result2 = our_function4(20, 30, 15)
print(f"I can use this {result > result2}")

print(our_function4(10, 20, 30))
print(our_function4(b=10, c=20, a=30))
print(our_function4(c=10, b=20, a=30))


def our_function5(a: int = 10, b: int = 20, c: int = 1):
    """
    Adds a, b, c and returns the result
    :param a: first value
    :param b: second value
    :param c: third value
    :return: the result of a+b+c
    """
    result = (a + b) * c
    return result


print(our_function5())
print(our_function5(c=100))
print(our_function5(a=1000, c=0))

a = 10


def f() -> int:
    """
    return 10 times the value of global variable a
    :return: int
    """
    a = 1
    return "xxxxx"


print(f())
print(f"a = {a}")

print(our_function5(22, 11, c=30))  # ok
print(our_function5(b=22, a=30))  # not ok
