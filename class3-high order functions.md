# class3-high order functions

## control statements

if or while 与函数不同，控制代码的哪些部分被执行和执行次数

if语句的执行程序：

1. 评估首行表达式
2. 如果为真，执行相应套件，并跳过以下的组合

### 函数表达控制语句

如何用函数表达控制语句？我们需要三个要素（形参）：条件判断句，if套件，else套件

```python
def if_(c,t,f):
    if c:
        return t
    else:
        return f
    
```

调用函数的执行程序与if语句不同：

1. 先求operand，再评估operator

2. 在operand的计算结果作为参数的基础上调用函数

### 函数表达与直接表达控制语句的差异

如下两种不同的函数，用于计算平方根的实数部分：

```python
def real_sqrt(x):
    if x>=0:
        return sqrt(x)
    else:
        return 0
```

```python
def real_sqrt(x):
    return if_(x>=0,sqrt(x),0)
```

第一种函数能够正常计算负数的平方根实数部分，**而第二种会报错**

原因是：**调用表达式不允许对部分求值而对另一部分跳过**，而始终在调用前计算所有operand

在第二种中，计算operand时计算了sqrt(x)，这就是导致报错的原因

## control expressions

### 与或非计算

evaluate `and` 表达式的步骤：`<left>` `and` `<right>`

1. evaluate 子表达式<left>
2. 如果为false，则`and`表达式值为<left> 值 v
3. 否则计算右边表达式，此时<right> value 与整个式子一致

evaluate `or` 表达式：

1. evaluate 子表达式<left>
2. 如果<left> value v为真，整个式子值为v
3. 否则表达式的值与<right>一致

### “短路”的作用

示例：

```python
from math import sqrt
def has_big_sqrt(x): #to find x>0 while sqrt(x) is enough big
    return x>0 and sqrt(x)>10
def reasonable(n):
    return n==0 or 1/n
```

当有x<0,或n=0的输入时，两函数均不会报错，这是因为直接将sqrt(x)，1/n给**短路**，没有进行计算

## higher-order function

函数式编程：通过定义接受参数的函数来概括模式，抽象概念

### assert语句

在函数中插入assert语句：

```python
def area_square(r):
    assert r>0,'A len should be positive'
    return r*r
```

在这个函数中，先evaluate assert后面的语句，若为真则不输出任何值，若为false 则报错，并打印错误信息，输出单引号下的内容

### 函数作为参数的高阶函数

函数之间通用的结构不仅是数字，也可能是计算过程

高阶函数适合用于抽象计算过程：

我们需要对如下的计算过程进行抽象，即用函数表达这样的求值过程
$$
\sum_{i=1}^{5} i = 1 + 2 + 3 + 4 + 5 = 15
$$

$$
\sum_{i=1}^{5} i^3 = 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 1 + 8 + 27 + 64 + 125 = 225
$$

```python
def one(x): #单一参数的函数
    return x
from math import pow 
def cube(x):
    return pow(x,3)


def sum_all(n,term): 
    #有一个形式参数term，在这个例子中分别被绑定到one函数和cube函数
    i=1
    sum=0
    while i<=n:
        sum+=term(i) #这里调用term，实际上是调用传入的函数
        i+=1
    return sum

sigma1=sum_all(5,one)
sigma2=sum_all(5,cube)
```

在函数作为实际参数时，是以**函数名的形式传入的**！

**higher-function is a function that takes another function as an argument**

高阶函数是以另一个（一些）函数作为参数的函数

## function as return values 将函数作为返回值的函数

函数可以作为返回值意味着**我们可以动态创建新函数**

出现于**函数主体中定义函数的情况**

make_adder函数示例：

```python
def make_adder(n):
    """Return a function take argument K and return K+N
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k+n
    return adder
```

当一个函数在另一个函数 body 内定义，**创建的函数被绑定到本地框架的名称**，也就是说此时**形成了一个多 local-frame 的 environment**

add_three = make_adder(3):相当于将adder函数赋值给了add_three函数

而此时adder函数中的n被绑定到3，最后调用add_three(4)时：4被绑定到k，返回4+3=7！

图片展示了嵌套定义时实际发生了什么：![55fdd03e5671261d4ee8d795ba738eb](C:\Users\Oscar\Desktop\学习资料\55fdd03e5671261d4ee8d795ba738eb.png)



### 嵌套定义函数的调用方式

输入make_adder(1)(2)，会发生什么？作为调用函数表达式处理！

**此时make_adder(1)被作为operator，而2被作为operand**！

1. 对operator求值：make_adder(1)，1被绑定到n，**返回adder函数**：

   故对operator求值的结果是body为 return k+1 的adder函数

2. **此时调用函数adder**，将2作为operand直接传入，return 2+1=3

#### operator, operand的定义：

1. operator：任何计算结果为函数的表达式
2. operand：任何计算结果为值的表达式

### purpose of higher-order functions

#### 函数是一等值

==函数可以作为参数传递，也可以作为返回值返回！！==

#### higher-order functions

高阶函数是以函数作为参数或作为返回值的函数

#### 高阶函数的作用

1. 抽象表达计算方式
2. 从程序中删除了重复的部分，这也是函数式编程的目的
3. 分离函数间的不同功能
