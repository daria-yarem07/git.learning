from random import sample

items_1 = sample(range(0, 20), 6)
items_2 = sample(range(0, 20), 6)
print(items_1)
print(items_2)

x = set(items_1) & set(items_2)
print(x)
