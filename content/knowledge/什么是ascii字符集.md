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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBA43MDZ%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIDaUwBhmE4oe%2FvlarlDgYA9LP3bfWNns6jD1v%2BAXajiMAiEAyJoIxfKyzdkeeqboRthHKe3dn2VayUX8dmNoygpSnD4q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOEB61Qpf9TtKFP3USrcA0dfyNW6D8vkmwGwLeIS%2F1JwQ8jk4KNjNiW5GUXakvP2sOvIMlsuILGzlSkAYFMhPSfUu%2FqHed7VbbP4mKOWiZWuePlQ2M33uHNOGJb3MaSe1ISJkMCcFlzH7XjAZkwJiQALHte1BLfJZctx8dJ85mdN6ntTe9DCn%2BAxAunOloRL1j2nn%2FCCwXt9qVZiBYDA3xc2%2BWWe7g7bQyswvuQx8fgsce7bbUHCQP%2FPZpFUQblexLwrr2TKMHWrbm046Iw6dHdGk9x7%2BK2l4FB%2FDAsKMN2MhA1YTUHDWWRzBXCTsozH14lDIoXd%2B4lYgRirmLR1T4XM7PKQwfp1KORECZP0iL1muh0Yb9gO1fyJAiGVkzqM97zKGF%2F9DXDH8jCvQnBQOK3UQk0fBS6qhYAy6q96eR4kHR8d6lSdZo4LasepqA%2B8rtKtCusvLlRFqTFOLw4mneapJn6sMjuMZDWE6M5FBeDLl1fOk2hn8IWMMSS9cfsIkuGCFQx3I9D0bR4CEL5gc%2BPOIQF5YjWYH5clj%2Fqj9r3E9QHD3dnRkSaQg6z9FMO0V8qk9gYlS8sG6nPVqptze5MlWmeCWi8705wcUwN%2FuT2HZCNzWi7WU3rxXW41FButEJPs3rt38mNz1nEiMNeY5soGOqUBHxV%2FUBcxJex8%2BWjqLu4lxMkxJITUKIMSS8JA3ZPC1CmlCGsADIbU6HrqLfGd4u4v3fTpPxlpyOZKsryzNvroSGf7GLenunUYAn8namDIx1UcYJeRfINQchEEJO9Deueo7BmPmCN1qqFNE2r7lVG9E%2FFs7ffDe7U%2BBHr2QtPMcx7%2FdvUVRs2SwX62FmvGhIhZYqMrQqQI6VZpKbvnhSFlnqKjr9YD&X-Amz-Signature=06b858cc319866c98011412fade000d67db436ec2db8717f85dcef56592402d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





