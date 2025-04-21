def count_until_larger(num):
    last_num=num%10
    length=0
    flag=0
    num//=10
    while num>0:
        i=num%10
        num//=10
        length+=1
        if last_num<i:
            flag=1
            break
    if flag==1:
        return length
    else:
        return -1
print(count_until_larger(0))