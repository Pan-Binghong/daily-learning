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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOZXLC5A%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAZ5hJi9T4mMCY%2BsvniwNY%2BDu5lKb4IayvnrkbEzrDCEAiBMb2DyZEGZb%2FVw7oPqdoyWdq%2B7I67v2Y9E%2BBaUUllYyyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN9Mb4mdvbVqYtEHYKtwDu2thsBEdesqzzqlo6ulEungJq2gdtrWDbBVhuZb4%2BshXR4fyT7uNCj%2FHgBWvvvzrVYO%2F2EGQKF9xc0yApifb7Mb4FvnyyaktDiifu6n3pfWQrWhH3J1lM%2BA0QPMZnG1nctoo3jbxmV5zMjom%2Fg5ah7UCjhVIn5mT43ZSdwpF3uZr%2BcO%2B8x1JJl%2FO1iIeOj3QB9kNr3ceIItzmYwAw%2BRqnL1X%2BtVkO8l1j05zISj8jF3ycJ58OwgYCad4bSvRPFmaZMxxX97h%2FMSNmJ6ycU6yWxgQdHREU2EtDUcQ2Yqn6hi1I7YlFH1kDE4YjM5OWTGL6m2zmhSTJAJ8TEprCGq67qxg1C%2BwMDeoCrEeTLsVWOj1W7pw7ICbg6z0obGN%2FTp5jkq37qtnDOsDWPBHXKXbJy4thPe8tGkODJxZm%2BaDyAcTcOM50u4UWVFbxlZ2zLaJwKrClIfnSvZa9ttJ9sobWFx28Ol0U5IEdGZzE6LMxR0ooxOHhJ2sztZlBHTZW5zbBZfrVj7bDtSqf9zCyznEjhVH8suj8jCs8Ee5eN7hBEXySd3OkT1y%2BKbYTCgaRQT7vSHCIghxZpXoTQ%2FIeHUIOKU3mJt8C3ndMPCgzwuD%2B4PesyH9rrc7d4NZTA4wqLX0zAY6pgGpeEC8aT07%2FVf1WuxI7%2BILQq9mdHte2f6HToVjiu1s0lX5b0ra1Bl%2FAhEQMIVbIE8CmIAz2Pt%2BDSmI%2FEd0T3s32FTTdSSg8jP8lZPkSxb%2BThKNLW7pyoYBeYbg4N68AXLd6YSXO%2FgwmiL4FQ9Eg0IVTjNTp15XpO0ZfARcyCIJadkUYRhX%2B5meujZ9kmrppgG5ZFFzw0SCGtKixp9rLt6itklru117&X-Amz-Signature=4e9571d80ec246ff128785e03735d4547e10028160cc88bc16ee55bf939c4751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





