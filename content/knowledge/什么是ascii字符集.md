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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZATP7GF%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaW2cIAGBWdaGt9HsATQUfYwB0kOREZRJ2bqdnqNwpAwIhAMdhCY%2BBtKvRtICZQEafcV5oH0PHvUFbDpYKmvWJZ7DQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuREHyDLyP52e0ssEq3AP%2FOAkk7OEtC9n00b3Y203KoQisRJVHzriE5tdBROUShSYhuJphFw%2B8j%2FOADB%2BAzKYi0cBrkRfzHPioiHCwyfqPxUqAEFjq22I8jgslzouBDVzhZnlDazKE%2FwbGd62cIQr2eNgQgyQ57iMlrIcVELEoCJ0aDw8ok9E2J%2BPYvkmv9OV88qfbK3%2Fz9CpCdXa1uigKqzn8cBja0OsoP79MPm5%2BYs5qcRETZgg1EVnYV7POj7rI0S4mfnTJ8f%2BwPIDbBzqU518ZT%2BrdmKxL2DLtHEP79ksNxrMYHoP2czko9xSw6kgCPjCyYFsbEG%2BVTMvlbPyn3Xl7sp736QlQlVOPWe93Ph6VoVumbNU4hPfyL33hWqmRlxU133%2BOeroCw5LVUb5mj2OQabTNlgV%2FUd0%2F%2B%2BotYM5QuWq6WJkWP%2B3AoHeinDS5U8ReHTE1mBaAmU8f0DnM%2BaWgHjwbY3llYMRG8u9SZ6lL5LXaKDHtAh6PTvtlx5VUyBWZUA0MCfV43gqRL3MXH2CxzXw15J0GUIA2YtY%2BRjyngZfweydfqsHTNABoj%2Bc%2F7MJvT%2BzC%2BLCqOa%2BigITRa7SbH85eLA5ZUzH0mE%2FXPPE4Kth6EdhBWTtj8f2yhgsr4kE3GfBf%2BjqM%2FTCHkfvLBjqkAfLUXox0xtd01jJAiDH1gOEPyE33gWW3%2Bju6KfzaCxzMXRljiuGithzJlRzzMvzM9FQ46aug0hgOrEhBiRZ46WVzq2Oqpemj9ARxatKUTsJRNNw9V46IRJDlRpoJeK8vupZhqrIe2pkPLVv1iS%2FXM8N7%2Fp9ZrUYj3AZBouGVhWrGGocu%2BqAmde3wYRz9UJQlQXHzgp6SU47htr9Qwb1YIjXMW4Fj&X-Amz-Signature=9bc353fb0b8f622e00bf7a0ce2fc8b5d16b42c360739d146fd1d70cfc685db8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





