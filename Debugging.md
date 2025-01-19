## Debugging

### traceback Messages

python中发生错误显示traceback

如下：

```shell
Traceback (most recent call last):
  File ".../ex.py", line 7, in <module>
    print(f(4))
          ^^^^
  File ".../ex.py", line 2, in f
    print(g(x + 1) + 2)
          ^^^^^^^^
  File ".../ex.py", line 5, in g
    return print(2) + 3
           ~~~~~~~~~^~~
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

most recent call 指的是最接近错误的函数，而most recent call last指的是错误发生时所在的函数被放置在信息的最后一组。所以**优先看底部**

如案例中：最后一组错误位于`g()`函数中，而这就是实际发生错误的地方

traceback的逻辑是：**从发生错误的地方向上追溯**，例如g中出错，f调用g，全局调用f自下而上的过程

### Error Messages

提供了两条信息：

1. **Error type**
2. **Error message**，即具体的错误提示

#### error types

1. SyntaxError 语法错误
2. indentationError 缩进错误 会显示缩进格式错误的行
3. typeError 类型错误 对一些类型使用了不可用的操作
4. NameError 名称错误 函数名称，变量名称不存在

### Debugging techniques

#### running doctests 写对拍

always look like:

```python
def foo(x):
    """A random function.

    >>> foo(4)
    4
    >>> foo(5)
    5
    """
```

看起来像是interpreter输出的部分是doctests，作用是检查实际输出与给定输出是否一致

运行doctests需要在终端中输入：

```shell
py -m doctest file.py
```

其中file是代码文件名字，如果输出与给定不符则会提示

#### printing 插入式调试

对特定值进行打印输出以确定程序运行是否与想象中一致

#### PythonTutor Debugging 创建环境图调试

[Online Python Tutor - Composing Programs - Python 3](https://pythontutor.com/cp/composingprograms.html#mode=edit)