# Class5-functional abstraction

## lambda function environments lambda函数的环境

### environment diagram with lambda

lambda函数的父级框架是当**lambda表达式被评估时位于的框架**

示例：

```python
a = 1
def f(g):
    a = 2
    return lambda y: a * g(y)
f(lambda y: a + y)(a)
```

最后一行调用：

1. 评估operand f(lambda y: a + y)，括号内为函数lambda1，parent为global，在lambda1中a被绑定到1
2. 调用f创建局部框架f1，创建函数lambda2，parent为f1，a被绑定到2
3. 调用函数lambda2，parent为f1，在lambda1中，y绑定到1，返回值4

f(lambda y: a + y)中：**括号内的函数是在global定义的**，a的值为1

所有没有缩进的内容都属于global frame！

## return语句

 从一个函数中return代表着结束函数调用，并确定调用表达式的值

调用用户定义的函数的过程：switch to新环境，执行函数body，return语句切换回先前环境，并实际上给调用语句赋值

**在执行函数主体时只会执行一个返回语句**，到达即返回

### return在函数中的使用

例子：

```python
def search(f):
    x = 0
    while not f(x):
            return x
        x+=1
def positive(x):
    return max(0,square(x))
search(positive)
```

通过最后一行的调用可以找到第一个square大于100的数

这也是**计算反函数的策略**，y=f(x)，对x求解，**即利用枚举**x逼近y，示例代码：

```python
def inverse(f):
    return lambda y: search(lambda: f(x)==y)
```

这样我们就构造出了函数f的反函数

## abstraction抽象过程

函数抽象是给计算过程命名，并引用整个计算过程

### 函数命名

name对于程序的构造以及代码可读性非常重要，命名可用规则：

1. name应该传递所绑定的值的意义或目的
2. 绑定到名称的值的类型最好记录在函数的文档描述中
3. 函数的名字往往传递效果(print)，行为(behavior)和返回值(abs)

### 哪些值值得被命名

不必给**每个中间值**命名

1. 反复出现的复杂表达式，不要重复自己
2. 一个复杂表达式中有意义的部分，如：一元二次方程公式中的判别式值得被命名
3. **名字可以很长**！这没关系，只要名字实际上帮助描述代码
4. 名字也可以很短，特别是作为惯例时：n，k，i常作为整数，x作为实数，f，g，h作为函数

