from random import sample

items = sample(range(0, 50), 10)
print(items)

x = items.index(int(input()))
items[x] = int(input())
print(items)