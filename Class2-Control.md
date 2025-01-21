#  Class2-Control

python执行程序时，会在不同的环境中计算表达式，在**一个环境图中可以有多个环境**！

## 多环境

### 用户定义函数的生命周期

#### 定义函数语句

1. 遇到def创造新函数
2. 在当前框架中函数名与函数绑定

#### 调用表达式

1. 分别evaluate operator,operand
2. 在operand计算结果基础上调用函数（即operator计算结果）

#### 调用过程

1. 创建新框架
2. 绑定形参实参
3. 在新环境中执行main body

### 在同一环境图中引入多环境

**环境是一系列的frame**，这一系列的frame总是以global frame为结尾

通常因为函数嵌套产生，示例：

```python
from operator import mul
def square(x):
    return mul(x,x)
square(square(3))
```

![a8db55e243b24c65f679c8cb9a3238a](C:\Users\Oscar\Desktop\学习资料\a8db55e243b24c65f679c8cb9a3238a.png)

这是环境图，在evaluate operand的过程中创造local frame f1，计算后调用外层square，创造frame f2，图中有三个环境，global frame,f1-global frame,f2-global frame.

#### 名字在特定环境中才有意义

**当评估name对应的value时，评估的实际上是在一系列有顺序的frame中最早找到的那个name**

查找顺序遵循`LEGB规则`

，如在,f1-global frame环境中，寻找mul和x的value，在f1中x已经被binding to 9，寻找mul发现没有，在parent frame即global frame中找到

## 不同的python功能

`/` 严格的除法，double精度 相当于来自operator库中的truediv

`//`int精度除法，向下取整 相当于来自operator库中的floordiv

```python
from operator import truediv,floordiv
truediv(1023,10) #输出102.3
floordiv(1023,10) #输出102
```

### 函数直接返回多个值

```python
def div_excat(n,d):
    return n//d,n%d
int,remainder=def(5,3) #直接将两个返回值分别赋给了int,remainder!
```

print语句会自动加endl，输出同一行就放在一个print语句里

### def函数时可以设置默认值

```python
def div_excat(n,d=10): #在d没有实际参数传入时默认赋值d=10
    return n//d,n%d
int,remainder=def(5,3)
```

注意设置默认值的条件是==没有实际参数传入！==

## 条件语句 optional statements

statement is executed by the interpreter to perform an action

大意为：语句是被解释器执行的，用于执行某些操作

条件语句的结构直接由一个示例给出：

```python
def abs(x):
    if x<0:
        return -x
    elif x>=0:
        return x
```

注意python中没有else if 只有elif

#### python中的bool value

1. false values: False, 0, ' ', None
2. true values: anything else

#### python中的且或非

1. 且：&&，在python中为`and`
2. 或：||，`or`
3. 非：！，`not`

注：同样存在**短路**现象

## 迭代（循环语句）

### while statements

```python
i,total=0,0
while i<3:
    i++
    total+=i
```

while语句的执行

1. 计算首行条件是否为真
2. 若为真则执行套件语句，并回到步骤1
