def prefixes(s):
    if s:
        yield from prefixes(s[:-1])  # 递归调用，处理前缀（去掉最后一个字符）
        yield s  # 生成当前字符串
