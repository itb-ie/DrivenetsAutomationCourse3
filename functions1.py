import math
import random

a = int("123")
print(a)
print(id(a))
print(min([1, 2, -3, -99, 100]))

deg = 30/180 * math.pi  # 30 degrees, because sin(30) = 0.5
print(math.sin(deg))
print(math.sin(math.radians(30)))

print("random".center(50, "-"))
print(random.random())
print(random.randint(1, 2))
print(random.choice(["apple", "pear", "banana", "kiwi", "pineapple", "dragonfruit", "mango", "strawberry"]))

s = 0
for i in range(10):
    s += random.randint(1, 10)
print(s)

