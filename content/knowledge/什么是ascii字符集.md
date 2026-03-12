---
title: 什么是ASCII字符集
date: '2024-11-24T14:36:00.000Z'
lastmod: '2024-11-25T03:09:00.000Z'
draft: false
tags:
- Knowledge
categories:
- 知识
---

> 💡 （American Standard Code for Information Interchange，美国信息交换标准代码）是计算机科学中的一种字符编码标准，用于表示文本数据。它为每个字符分配了一个唯一的数字编码，主要用于通信设备、计算机和其他电子设备之间的数据交换。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKKRA5BN%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBeT4mLfCKdHnQ7r4eEzmEHKW4cbg4bAVF%2BayO4pvgjUAiAWRtskqx%2Fy07TK7knoRsvM2ZIKQy2UlS%2B5IzoHvRfLzCr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM3TBl%2F0C0H%2BX%2BFFU%2BKtwDC3BsZE2uHezhUCIzBrPdVP9%2F4c%2FJrdSrH49ABBmJ%2BGFmHtB610SBWhAHDHlTB8l9YYcdyyT9VFSXPq%2BAK%2Bt7R0ShdoIHF5cdTDA6wdn%2FNY9iwx%2BNNIlsUn2648DJtS8tsfaU2%2BRlQ05LLE1wzF4IvwLnBqUDsO180yHajsyIZHTKSKpYiK3cRoOuwi7D4UXHYoX6yzv3PbNT77F%2BSIg8kOS%2BvCLoZhhZfgR5sMUpb730wH9If79v1fbZhg%2B0xhzlE4GaXM8sY1KmE6tYt4RlR%2FwU6wAspXVEiJB7dKVt4MYfqvu2hD8VwcFZ9VIsmzGDABn%2F3qhIMGtM0l%2Fpw7Bk7Rso1EtA73o8HRMvcdPUBwRSEpmjO0dZUj%2FHawXce6jLFY31Z1ZxLPG%2B4SSuEukVLVrU%2FHH0%2BFVQstY4oJGTi3WtvNyUlKit187i0zY2XHL%2BQeNlavWjZUMjkgCpmLw0oyTrBWjt7A56d9DOwC7r9yFjvh7NmtT1BdtkdxzQF48hnAM3yIo8rJ%2BlTS4qr3DzX12SPajEtZaeLiYR4NdggWUJYw45eKiejAPLzA8%2FigxumXr8YcW1aecU%2BKoqDegaFp87RnK1DwgyMQu3paOTJITkJ3j5FqEURh%2FkDpowgLLIzQY6pgHrT%2BH7xG4IwJWj1sT2GMrWTPQP21rqjsP1hZl2T50%2Boj0PfJFirF2R7lOnDr5VVNCJCmILQOt24cIlVNu%2FnH6ltCwDmUi4CYLUDs6vgWG8lzAGIWp68l2Bi2SLOx3fkgK6jlWJkuHGLj0Lof7NmqEn8TNIDyC74Vts1bfFqxkaxQ6EmH0LRmVn4Kh3wNLYbhbwZno6C%2F0cI%2Bc5LwSIoC2Ak1c4GsjA&X-Amz-Signature=5e686fc3385fbf77c92469657448f76f9714bf7c01552b7ed3125718a6a37f07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 特点

### 范围：

ASCII码使用7位二进制数（0到127）来表示字符，共定义了128个字符。00000001

- 数字：0-9 （ASCII值为48到57）
- 大写字母：A-Z （ASCII值为65到90）
- 小写字母：a-z （ASCII值为97到122）
- 特殊符号：如空格（32）、换行（10）、感叹号（33）、@（64）等。
- 控制字符：如回车（13）、换页（12）、删除（127）等。
- 详细一览
---

### 为什么只使用7位？

早期计算机内存和存储资源有限，使用7位编码能够节省空间，同时满足当时的英文字符需求（128个字符足够表示所有常用符号和字母）。后来为了支持更多语言和符号，扩展了8位（256个字符）的编码，称为扩展ASCII。

---

## Python实现

```python
def show_ascii_info(char):
    """
    显示字符对应的ASCII码信息
    参数: char - 要查看的字符
    返回: 包含ASCII信息的字符串
    """
    ascii_value = ord(char)
    binary_value = bin(ascii_value)[2:].zfill(8)  # 转换为8位二进制
    hex_value = hex(ascii_value)[2:].upper()      # 转换为16进制
    
    return f"""
字符 '{char}' 的ASCII信息:
- ASCII码值: {ascii_value}
- 二进制: {binary_value}
- 十六进制: {hex_value}
"""

def show_common_ascii():
    """显示一些常见的ASCII码范围"""
    print("\n常见ASCII码范围:")
    print("1. 数字 (48-57):")
    for i in range(48, 58):
        print(f"{chr(i)} = {i}")
    
    print("\n2. 大写字母 (65-90):")
    for i in range(65, 91):
        print(f"{chr(i)} = {i}")
    
    print("\n3. 小写字母 (97-122):")
    for i in range(97, 123):
        print(f"{chr(i)} = {i}")

def main():
    print("ASCII码学习程序")
    print("-" * 30)
    
    # 测试一些字符
    test_chars = ['A', '1', 'z', '@', '中']  # 注意：'中'是Unicode字符
    
    for char in test_chars:
        try:
            print(show_ascii_info(char))
        except ValueError:
            print(f"注意: '{char}' 不是ASCII字符")
    
    # 显示常见ASCII码范围
    show_common_ascii()
    
    # 交互式测试
    while True:
        user_input = input("\n请输入一个字符(按回车退出): ")
        if not user_input:
            break
        try:
            print(show_ascii_info(user_input[0]))
        except ValueError:
            print(f"注意: '{user_input[0]}' 不是ASCII字符")

if __name__ == "__main__":
    main()

```

---

> Reference





