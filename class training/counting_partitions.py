## counting partitions:
## 设计函数count_partition(n,m)接受两个参数n，m，用于计数最大长度为m对n进行分割的方法数
def counts(n,m):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        return counts(n-m,m)+counts(n,m-1)
print(counts(5,3))
## 特例分析法！举出一个特殊情况来探究递归式
## 与伟伟道来7关系密切，实则就是建立从过去到现在的递推！