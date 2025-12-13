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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXLVK627%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDiiXfn%2FFzHlpGKiQvEjiv6SV4WQXQCjf9hkMk%2BUzBlYgIgciMc%2FxIH01Da0k2rbkwA5%2BAR2OKeSr6hC8NmuhCrMx4q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDGw6dAGmShu8yZhZTyrcA9v6JDrIiryR9mhYVgpssd6bjw52iUMQ6pI0tipKFDyirYqJ8xO5pFIQBy2dWQzoz%2FqvB3cSUoMRtO84qS4zFVSlOjCg7BJdEX6YoK7B843x79oBdresgGMhRPr4GH%2FUHLTsBmEgVn6xYyg0%2ByJi4TmdocpXcfDUG9JAMHQveV5%2F%2FP1vZHGip6I4RvlZtRKITx%2FgfN3woBflYw3mr3%2B8r5wS2txf86B6c1udpyzu0DVXxns%2B3zKjvEtJPrh4MWWJ27NaC4gjXs9TF%2BD%2Blpa1qk%2BdTZIG5AsjWNW1ItDV7bDXNnxuWumPNE7mpqVPP8ODsIkTnYAfRXskuSSI0jxtvx9KzCxRtwpQLPJOx061MPYA7TpWrRR1b%2BI7s1hM8Ub%2FhH88Bvcuws51jZ%2B4MmvaWlkXWGeOV7zGXQt8hknI1eEFpkvj9bJkUh2RSVGjSLmgZNQF6kzxjqGcNYQbD8OT90VV9nBSpz2CpAOuYssXDEB19AnpOXDA5CozcHL0B4ULI5gSZ4ABDki0e841jQlggAiMemLdch7fpPDJUdgQ%2FRbGWHwcZj2V9xfAa7L8yHGvXGvmiOAlpI4a1qxzdkW7%2BuAtd%2F3Fd2s8x34jtrpjzlAh4aXhqBoWKKNXSMIiMIqN88kGOqUBzoufZZH8vIeT7Iq7RktNOrODCqpaT5A32bACj3NyxGH66Ts%2BKxGbbXf%2ByUaGYMNfipmf3gUQdF4biR37Fi9BDMEOtLf%2BcNTWhC04QyuEtMvAE4%2BkTQZ15y72yOYsGGbInuwVJ2CRh3c5%2BCZLZ2DIO8Q4cd6UkvpyBz6dN%2FwDq40ANMS8fRSq5dN6JwLoljef0NdEIHMKbGSqG507iEXO07n%2BX7o5&X-Amz-Signature=9d58c001dbbde4be2fc29397d1b2d3e650c6f81b1ba6195c244d5080a901e8df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





