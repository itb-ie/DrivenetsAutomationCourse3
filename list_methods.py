from functools import reduce
# print(reduce(lambda acc, x: acc + "\n" + x if not x.startswith("__") else acc, dir(list), "Non-magic methods of the list class:"))

print(list(filter( lambda x:not x.startswith("__"), dir([]))))

