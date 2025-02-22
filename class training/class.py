## writing a function that can print
## 1
## 12
## 123
## 12
## 1
def grow(x):
    if x<10:
        print(x)
    else:
        grow(x//10)
        print(x)
def shrink(x):
    if x<10:
        print(x)
    else:
        print(x)
        shrink(x//10)

def inverseCascade(n):
    grow(n//10)
    print(n)
    shrink(n//10)