## Implementing a Function def remove(n, digit) :
""" '''''Return all digits of non-negative N
that are not DIGIT, for some non-negative DIGIT less than 10.
>> remove (231, 3)
21
> remove (243132, 2)
4313
100000
kept, digits = 0, 0
while
n, last = n // 10, n% 10
if
kept = _
digits =
return
Scroll for details """
def remove(n,digit):
    kept,digits = 0,0
    while n>0:
        n,last=n//10,n%10
        if last!=digit:
            kept+=1
            digits=digits+last*pow(10,kept-1)
    return digits
print(remove(24313, 8))

higher_order_lambda = lambda f: lambda x: f(x)
g=lambda x: x*x
higher_order_lambda(g)(2)