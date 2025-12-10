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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAQBA5Z5%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIDWJIztIqrpKalHkk65sXZXH2n%2Bw5vUcMvCW%2BUpAT8I%2FAiEAm1ZxrA3O3hE8%2B97skt3%2Fm603fxiS0rLMYeKfMTH3YW4qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhYxZxjZnC6eHoVVCrcA1zfU50HZgl4tZDfzcJ%2F3ssffa4%2BHDGddU1LLJRQH2uPYQ1TYyHZrDFUZXLy0YJls7RPWacUmmVviR7pxpOztBaU2jt7Dv6dYuhxLC3Ez4ZqBe09Ycq2wpZLTRV4NjqY8duNCN6kh1oO6RfpGOzDI0ghXQm2eusOLwmIL8dLW11BWNqSw%2F7yvbndFPNhczKFUwR3weDpNjZagFVwUfyDSoJzmCg%2B%2Bdofp3abTFbpxckxh4PgRTIzdyDzaEjT%2Fm4Xg4nPV6NOS98EXSkf2v5qAoUKCSM07bFY9fqgY5vFt8TSQoi6ynoC%2FyAQ2GdXNoWpio0G%2BZnQl2wVD0cIIwoazMZ2dGN7DZyOh9aY1ZkZeh2%2B7YsVaQDACQwX%2FlScU%2BshD%2BMGZ9Fpw8pO%2Bq862rEuafXYDqx4yeB6Cfx%2B9%2BV3TN%2B6fbsviT39fMd5N4%2FGPUiJBX5gy2g7NJDBuyHL2noCKyUf8pee7P35wJ5bFYjbexAR9Ek7jvdY5HAhQObdDhTiVXmcLJXBVfFNmvagWY2XvDAaxY64qoej%2BCxEJ2s5S84L3FP6D247sE5QUl1Bdt5NJN5lm7vrkv%2Bcy9rm7%2FFq2rruqp4O5yeYO%2Bq1k94mqaZ%2BzHNZgv6fD9Ba2SsYMKzA48kGOqUBdInQkpW4XEWfmwSABMVSnk3T3u%2BBLiKJ5kjbJj0B6BUujFM9MEaMdBhkh6WcTN4MRq1UVW0F9HxSr3hhXu56uOLtCBw98IzkKi4ZJ7YD5YXqG%2FakDpTqF3F3X2aN8Koih9MV%2F64DEQLUM9KfJ1VD2VYegWDYO6Dt0Bb5YjhM4%2FDi4aT7ufmGd5ktMWJKeig9Cbio2BOeE19O9U9h5%2BmAYt3T%2FwwM&X-Amz-Signature=f1deb2fe2f67bb834ccb336aefd8849b3018293f2e233945a62932e65dd84930&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





