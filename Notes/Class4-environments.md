
# Class4-environments

## 高阶函数的环境

将函数作为参数或者作为返回值的函数

```python
def square(x):
  return x*x
def apply_twice(f,x):
  return f(f(x))
result=apply_twice(square,4)
```

可以尝试绘制代码执行过程中的环境图

调用用户定义函数步骤：

1. 创造新框架
2. 绑定形参，实参
3. 执行函数主体

只有**嵌套定义函数**可能出现多框架（>3）环境

即使是在本题中函数内嵌套函数，调用时内部函数parent frame也为global frame

**嵌套执行先算operand再调用operator！**

## 嵌套定义函数的环境

make_adder函数的例子：**出现了多frame环境！**

```python {.line-numbers}
def make_adder(n):
    def adder(k):
        return k+n
    return adder
add_three = make_adder(3)
result=add_three(4)
```

环境图与绑定关系：

1. 在调用make_adder函数时，创建local-frame f1，将3绑定到n，这时定义函数adder，注意：先前adder并没有被定义，**因为在定义函数时body是不被执行的**。在f1中将adder与函数相绑定。**我们无法在global frame中引用**
2. 将adder函数return到add_three时，这个函数在全局中实际可用了。**return语句的作用是将信息从本地框架带回到全局框架中。**
3. 调用add_three函数时，实际调用的是adder函数，创造local-frame f2，夫框架是f1，将k绑定到4，此时n的值在f1中查找为3

![511737712267_.pic](/Users/nianzhen/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/a1df856470021f1107719fb66424d682/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/511737712267_.pic.jpg)

### 为什么我们需要有函数的parent

当调用函数时，我们可以对该local-frame写下正确的parent-frame。如adder的parent func. 是make_adder，调用时parent frame即为f1

我们需要正确的parent frame是因为我们需要据此来刻画环境

#### 每个用户定义的函数都有parent frame

除了嵌套def语句，别的函数parent frame均为global frame

内部def语句位于外部def函数调用时创建的localframe

#### 函数的夫级是定义或创建该函数的frame

#### 框架的夫级是被调用函数的夫级

所以，在这个例子中，函数adder在f1中被def，夫级为 f1，我们调用adder时创建的frame f2 夫级是adder的夫级，即f1

### 环境图绘制方法

1. 定义函数：def + 函数签名。函数夫级是当前所在框架。将名字绑定到当前框架中的函数值
2. 调用函数：添加local frame，绑定形参实参，执行函数body，当需要name绑定的value时，逐层查找直到到达global frame

## 形参的局部作用域

示例：

```python
def f(x,y):
  return g(x)
def g(a):
  return a+y
f(1,2)
```

当我们运行这段程序时，实际会报错，这时**因为调用g(x)时形成了2-frame环境**，local-frame中a被绑定到1。但在这个环境中我们无法查到y的值，**y在local和global frame中都没有绑定到值！**而y实际上是在另一个环境中被绑定的。

## 函数的组合

示例：

```python
def make_adder(n):
  def adder(k):
    return k+n
  return adder
def square(x):
  return x*x
def triple(x):
  return 3*x
def composel(f,g):
  def h(x):
    return f(g(x))
  return h
composel(square,make_adder(2))(3)
```

这是一个组合的函数，在最后一行的调用中发生了什么？

1. 计算operator：composel(square,make_adder(2))

2. 计算make_adder(2)，创建local-frame f1，并创建返回函数adder，n被绑定到2，parent为f1

3. 计算composel，创建local-frame f2，创建函数h，parent为f2

4. operator计算完成，调用h函数，创建local-frame f3，parent为f2，x被绑定到3

5. 计算adder函数，创建f4，parent为f1，将k绑定到3，返回值5

6. 调用square函数，创建f5，parent为global，返回值25！

   ![image-20250124211123278](/Users/nianzhen/Library/Application Support/typora-user-images/image-20250124211123278.png)

## lambda expressions

是对函数求值的表达式（也就是定义函数的过程），用于动态**创建匿名函数**

```python
square=lambda x: x*x
```

可以通过**直接写函数体**的方式定义函数，格式如下：

```python
lambda x: x*x
```

1. lambda关键字：类似def，但此时不需要函数名
2. lambda后跟形式参数x
3. 冒号后相当于：return values of x*x

本质是一个**计算结果为函数的表达式！**

**important: no “return” keyword!**，这也限制了只能使用一个表达式作为lambda函数body

lambda 表达式在python中并不是非常常见，但对于函数式编程非常重要

lambda表达式不能包含语句：如不能在lambda表达式中写while

### lambda与def的异同

```python
square=lambda x: x*x
def square(x):
    return x*x
```

相同点：

1. 都创建有相同域，范围和行为的函数
2. 都有父级框架，即定义函数时所在的框架
3. 将函数与名字绑定：**lambda先创建匿名函数再赋值**，在def语句中，函数创建和绑定名字是一起发生的

不同之处：**只有def语句为函数提供了内在名称**，当在解释器中查询时：用lambda定义的函数会显示函数名为 `<lambda>`，用def定义函数则可查询出def时绑定的名字。事实上是细微的差异

## 函数currying（柯里化）

是一种操作函数的方法：

使用lambda创造make_adder函数：

```python
def make_adder(n):
    return lambda k: n+k
```

调用make_adder函数时，我们实际上进行了两次**单参数调用**，包括在过程中返回函数的函数调用，才真正得到答案

而对于add函数，我们只需要接受多个函数并进行一次调用即可得到答案

```python
def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g
```

curry2函数实际上把两参数函数转换成接受单参数的高阶函数（make_adder）

curry2函数也可以利用**lambda表达式表达：更简洁直观**

```python
curry2 =lambda f : lambda x : lambda y : f(x,y)
```

currying化就是这样一个过程，允许函数局部只接受一个参数，**将多参数函数转化成单参数高阶函数**，**该高阶函数返回一个利用剩余参数的函数**

### 为什么要使用currying？

1. **灵活性**：通过柯里化，你可以创建更多的局部函数，复用代码并使函数调用更具灵活性。

2. **部分应用**：你可以通过柯里化将一个函数的部分参数固定下来，简化后续调用。

3. **函数式编程**：柯里化是函数式编程的重要概念，促进了函数的组合和复用
