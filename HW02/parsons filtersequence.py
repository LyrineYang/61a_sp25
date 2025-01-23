def filter_sequence(cond,start,stop):
    i=start
    sum=0
    while i<=stop:
        if cond(i):
            sum+=i
        i+=1
    return sum
print(filter_sequence(lambda x: x % 2 == 0, 0, 10))
print(filter_sequence(lambda x: x % 2 == 1, 0, 10))