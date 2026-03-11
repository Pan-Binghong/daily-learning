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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IIAMF2L%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQ63fajKKOAhGvqvkmqebyWED0Rur7YujIIeylsnA%2BDAIhAPYMiDQM8HPq6Vxe5OJQ5L28Qn%2BSYtOKgrRCpTngGuFqKv8DCFIQABoMNjM3NDIzMTgzODA1IgxmCJr1OTPROCLIxgsq3AMMcQnPgJLF6%2FGJGtfuc%2BhPqaYZs2XYMZ2voIu7E7lrdnVL%2BJurHkGccvTftl%2BDIJPr2seT8EzzjmfVv1gEJipg%2BA8woQ9mXIc1v0ju3bSFtUVoyUbaV1%2BDBgfpZnc3ENc5iEkhxPAiEk81HTkLUsbIB5oq7bw6yesG2aUjvh3A72MLpO8qVlL6nBQuUIa27ySNiQpfaUOKX6o0NatSByg3iVDWbVBV4GUHVN255kuFmJXBYPTlY%2BAS3F4kn%2F0vp2xEtcCRQOGKgG%2FVEl5QpgsTwER6l0psQWS5jR%2BoC%2F5hLzoFaQ5uo9jYYshXWD%2FAhqeYnvwFkzQPQEqkCimrb6Wdx%2F4NdgvdsqvKiBYEOn5MRv7ookxX72lVn6Ddhzq%2Fl8ZVploZmC%2FB0zEjGq%2FyrMwkcZA3lw3rbs0xSwq4HzdV5%2F82kA0xLFFVoS7JwjFjElATBVPaWFHkEJo28lvAcXdaYuVQUqi3KLxAiBQT6LWSelgGEkmiQ2O2Pun%2Fqa4qZmS9J1iasaVWQiEUQsw%2ByNegUmOGjHcCQpnlTAh24uAtxTnpxQQfLntf2%2FY0G8LYGLO4Qq2HvKvaINsbz5UHxG0VOzdGPTTf3CcT1VGdjCj1nscMg4w6gkyoH2f7azD68sLNBjqkAX1GTWCZ1ztN%2FV8tSTcNzeG%2F88tvz4lAwounqp7kFvUBJqEJJHBcNH56Wr4Xc77mUBZEepvbJ%2BFvybUF07FGRdUwoNRzhPiWKaEhqp3wXv%2FeBfLLHAn2%2BcjpFx8pz9xXAdon108R4VglA10BEvrDRDQ5n5C0gNRO5S%2FXuuvg%2BZFJRgKJ2tY%2BmzQBjspvhom1ZwaxNT5zlaSxwYLYXeI22BCFIkwj&X-Amz-Signature=72baadb285f6efdf0968e089575e3257a4997ad8422b8124eaedfa8a8ca882b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





