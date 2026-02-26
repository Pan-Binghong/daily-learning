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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCX6BUR3%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIBVGDLzYZ%2FJtk3z%2Byb4Y8CxSZZ4b7qdr%2FSHmTgFDjOmhAiAyUr590o94Col7%2FOT6nkSLnQdBfEGokSvp6n1DOX7RlCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMvGTkKleW23LjIpMSKtwDgK%2F1jQrbm4Wckt0WwL7%2F%2BY7mzPvvkdraMFuvMlIl0PMsApsBq2p%2FiXWQzsnnNIkzqS2cim%2Fcx%2B4wN7zKiVbk6vGAV%2Bo3Wr4scnmeDrfRzYOuQmCL%2FmfcfcjjVJ10gJW%2BlRDYhN1E0iJiexH3aceBLPvY%2FllDXpdav%2FV64RUH0d1N2R4iPZ3toF7qSkRlM6UQduLU%2F%2BvICHvs7%2BMacaN%2BUHmCnKSgt%2F9Fo6RHGHudI9urd0wXdJPY1LHOpB0rSEUogs1mrBlci6KB2VV8kj%2F2%2FY1nJfOF87EYGnmyiwb7mg6v2gHmH%2Ba19VrcScUEw2bxTdZid1UCv%2FqU6QPzssWdmjCDCECe125oJvA5B4iflzkxXLwsdVHu05vkIzkyrAG5nv3HKo5aXKRIgwj7pg1zEHydCf0ARQM%2BBeqEc7SRbMyPKhwckGMeQKrHtbpmXH9zHzRPQeG0srFg%2BhvXqL6fJOE36EMVj68nI9mYUFappelhW10fPf6PEtnObK1w6zos%2B2MwAR7qzWiM2oYCQu%2BST182MGbrE6AD3qfO8xSBFJ4GbCezgBnGnlFE9jECaDsgEWdbpwxkvRrOsSuGRmeFT4p%2BWm4et0Ot%2BVdsGmPvE9r9kac%2B2n8QM6VAFxkwhvb%2BzAY6pgHb0lgWWUBXzyrMnBXZpNfXvnHNuivOeb69ZksskdS8hcvvItuguVMVviTOzOv%2BPkO5f9xS9g4K1xEZdr%2FtAmLIMRTbzhRcqlo0zotGc71n%2FhN3FpFdFBsJcYHb9CpWD4sTV55B%2FXeRDRVy61mO8xsvx8xNFFnHtTVv3etWRcGVOYYCSeEHVoGVkRfdMLrU8WfnrfagxgXxS%2BP6sW9C9g%2BMEEoeK8KU&X-Amz-Signature=20cbbae268c6e3352bbc686134c48db94d6e7075926951d09cdd025c17221ac0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





