# generator

**生成器是特殊的迭代器**，是从生成器函数返回的，生成器函数与普通函数的区别是，生成器函数利用yield关键字而不是return函数返回值。

生成器函数返回的生成器是一个iterator，可以调用next函数取值

```python
def plus_minus(x):
  yield x
  yield -x
t = plus_minus(3)
>>> next(t)
3
>>> next(t)
-3

```

在例子中，generator是生成器

**生成器函数是一个产生值而不是返回值的函数**

生成器函数可以产生多次，生成器是一个调用生成器函数时自动创建的iterator

创建的生成器会对生成器函数中的yield进行迭代。

当调用生成器函数返回的生成器时，函数主题开始执行直到到达yield语句，而yield函数产生的值将作为next调用的结果。此时函数将会在yield处暂停，但保留函数执行时的环境，以便下次调用next可以从上次暂停的地方继续，核心：**惰性计算**：直到调用才需要计算

生成器函数常常在执行过程中处理迭代器

yield from语句会从iterator或着可迭代对象中产生所有值

事实上 yield from语句是一种对for语句的简写，会遍历可迭代对象中的所有元素并逐个产生他们

```python
def a_then_b(a,b):
  yield from a
  yield from b
def a_then_b(a,b):
  for x in a:
    yield x
  for x in b:
    yield x

```

上下两个函数是完全等效的，注意yieldfrom函数是逐个遍历并返回

```python
def prefixes(s):
    if s:
        yield from prefixes(s[:-1])  # 递归调用，处理前缀（去掉最后一个字符）
        yield s  # 生成当前字符串
list(prefixes('abcde'))
```

对yieldfrom形成一个整体的感觉，在这个例子中，prefixes(s[:-1])是一个迭代器，而迭代到最后返回空值，返回到prefixes(a),此时产生了a值作为整个迭代器的第一个值

如何利用prefixes生成字符串的所有子串？

```python
def substrings(s):
  if s:
    yield from prefixes(s)
    yield from substrings(s[1:])
```



return有时候是与field非常相似的，只需要记住他们之间的本质区别，有时候可以进行更换

