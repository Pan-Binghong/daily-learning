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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUVK4DLK%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCuI7X7oofIfE8xEHiF8b0uqo%2Fm6CK8G9PR0EOOdw3KygIhAMRCUsbuWNIu9tyZTSLmXC1ax2sfnYJTcauWJ64Y32qVKv8DCBwQABoMNjM3NDIzMTgzODA1IgwYLPgH8whm31r6wzkq3APpCwfcq2AvfmOFqeng4flzGSyKtE4zdVoEMX262X6U8v9n7pfuVPRFnTgyDwqhLzMaJARzZBICquuttslHawlwW%2BaxAt18ogb%2B9zsAXSZljte%2FzydajcR4PTS12g7KCqF0rY%2FxFBWB8p5LbUbPeLIAw01AyQr8ABaCInEt%2FpMLlSvR%2FPCevrviy28BpF3KsvbwiJ%2F%2FxtK1MmtV8DucIJoBu6uBKj17iCxDROQR7QMk4VqxoDOmJydWEeFYglM3vVxHdtOyXRqOYGQBDVgLlvjTMRSQrsP9RB8NsTFEF4udx7I7g0y7R2US5VlCK8p86GuFebdkU20R9Jy0m1vQvg9VDtRhDHBUObI7LVib5hjjAQ5JGQxmwljgR8NRZpfyzRzPX%2Ffz3fO1m1MzhNUeSPd5her14TLu9GHDSRcBExgucsAg9EQbPpzRuMEKx2QSIKlX5gNNN0OthXGSup05pYxML9lKoXMFa241UkASAd4YBvwwpJ4HoJ%2BFjxqFLj9XoXmxysKsw507atVPPkKMiXUKRqVbyv%2FAW7Qg%2FMonKyYWBW0mf80emWj14C50brB7DmS9kBFTa%2F85c727A%2BWBDzjwwHyMNv2EYZ%2FZdf6AZX7AgciNcBl6I7HECIAPFzD5hNbLBjqkAXuaBUdBczMW1Poo%2F1EU3SVqrxXaWhoRHDdy9SQWdkTpi9bJkeDNaxJ9CXiKxORtaeCLhq8rpq7%2B78a17wscuOrJzMQYjEdOX4ZFMegVjx6yyZI0A1%2FF4nRrDbKyzL7EQfW4qrPJRamSAKt0S2XHrkTVJDTzpHU3SzMSAUAhk8%2BFI3pGlu413GUljT1Ml4XUhLI6P7bcz7%2Bg92Mqd6jbG8PJ3gFr&X-Amz-Signature=d9b9d36b011807f6e21149569fd40d4123242e3243e32926a2165c9159514216&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





