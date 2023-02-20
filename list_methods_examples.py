import random

# appends, add an element to a list
a = [1, 2, 3]
a.append(11)  # this is how you append!!
print(a)
a = a.append(11)  # this is NOT how you append!!!
print(f"after assign an append: a = {a}")

a = "i LIKE cars!"
a.capitalize()  # this is NOT how to do string operations!!
print(a)
a = a.capitalize()  # this is how you do string operations
print(a)


a = [1, 2, 3]
b = a
print(f"b is a is {b is a}, so changing b will change also a, and the other way around")
b[0] = 99
a[2] = -7
print(a, b)

a = [1, 2, 3]
b = a.copy()
print(f"b is a is {b is a}, so changing b will NOT change also a, and the other way around")
b[0] = 99
a[2] = -7
print(a, b)

a = [1, 2, 3, 2, 3, 4, 2, 5, 2]
print(f"2 shows up {a.count(2)} times")

# extend same as +
a = [1, 2, 3]
b = [9, 10, 11]
a.extend(b)
print(a, a+b)
print(a.index(10))
a.insert(2, 99)
print(f"a before pop: {a}")
print(a.pop(), a.pop(2))
print(f"a after pop: {a}")
a.remove(9)
print(f"a after removing the value 9: {a}")

a.reverse()
print(a)
print(a[::-1])  # does the same thing as reverse, BUT!

a = []
for i in range(100):
    a.append(random.randint(1, 100))
print(f"unsorted a: {a}")
a.sort(reverse=True)
print(f"reverse sorted a: {a}")






