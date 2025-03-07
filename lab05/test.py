list = range(10)
f = lambda x: x >= 5
t = filter(f, list)
print(next(t))
