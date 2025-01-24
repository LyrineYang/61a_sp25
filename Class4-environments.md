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

2. 计算make_adder(2)，创建localframe f1，并创建返回函数adder，n被绑定到2，parent为f1

3. 计算composel，创建localframe f2，创建函数h，parent为f2

4. operator计算完成，调用h函数，创建localframe f3，parent为f2，x被绑定到3

5. 计算adder函数，创建f4，parent为f1，将k绑定到3，返回值5

6. 调用square函数，创建f5，parent为global，返回值25！

   ![image-20250124211123278](/Users/nianzhen/Library/Application Support/typora-user-images/image-20250124211123278.png)

lamda expressions
