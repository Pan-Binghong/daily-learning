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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHQRB2JV%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCICK6snblL926rx%2BQsAEzKgzSDAjJNzog9Pi%2F9InUAgALAiEAoOjSoiHppk7zhbENkqBh%2BudgkO9HgSPW%2Bg1qVHtKn7MqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCI68rgV99Y%2FZEXpoircAzMg%2FJ4yVRiTR8fXNDLXPy6vtXSpDFvpdfa%2B6PrD8b8ys2lMWTgTQBZoP%2FFudn6wi1gWzNdGB0kY79EvYqokCeAnlAqPs5VBwVhle%2FMRc0pWz6SdcjskVb0Zp7soq%2FPTA5H5JH69stNaQgAom%2FRmKpK9mSv%2Fk7uTSZDzWf9nn4B4gdGMZ9g0z%2B5ngo6qGN0Suh6gmJOIUCaWz%2B%2BUOHbRI5ItqOBu5vQ935QYrEiK3LnTs5PfFVmpkbl%2FxWq7jQuZJFJ5ASMyM9ZTkENov4l7ZmMrSsQLNSqA7p%2BAdulJH0lFJ7K%2BzwazjZEcU4m8D24chZwP%2FCaBL07KN%2FhiBwoXkOyH4D67RoTHf7%2BLRJ%2Fhhs%2BZ3%2BoMs%2FbgNTy7MdbmvVDL0cfQU793A8QIkInP5r4H%2BvZ3RrZHgM70zYJYkNO%2BlpenIAPqrMyQefv3YBRKpljuOXPEGm6iL0FkJAGCFAL2Op5kP7wqKNBUoccQBKhEBN7qQtSHCyGJjI3ezcbXlEW9uAJH0S8ZOhi5wsMNJWMH8yRJhM%2BuDydUOlKHuICMd%2B8kFFALL6KUHGcTooaPhDbCm46RJo8QXgcE20qhN5IOWXzPAQGVrt97L6d3gsHwEcusAKCaIr2AX5hNKM79MOSTrs0GOqUB0Kbpy26yW4%2BR6FU4z5nGIx04x6DuEQGfv3IWpoV2Ne7ztoELUWjC6QhAF%2BHhFTW%2FoDF6fIpOsEvEiAYadmLsL%2BwwEoEP6WDS4rom0q328AmcKZSo1Bh8qrY%2B8Qfb3OQIgnO8O2L72J%2BvjDmXy2CjzOTdw5%2FFMjONGBOHo0BwBttwoeLptVm8EVgpQuHiDH8A2BeuC6DVMa7kEjyLW0MhB%2Bf32ffD&X-Amz-Signature=41a0ae13de7982aa9cedfdfa3756091230a8feb85ac4d090733a79899946e7c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





