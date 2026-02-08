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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BQAMJYC%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnyqZXEemhGzlzxtAIlNKQuSMetJWQ%2BcojHqJdpsjYTQIgcbLUYgWm3PPPWeKlLc12SG2LkW0BsdPwUkzFVDdbYjcq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDDOVDUhOqyaWyutSsSrcA5aVqTZMAnK068ozBrDYS%2FIi%2BCF%2BGHcU9imhNWyX2TccYknvKS4SqSKzUb3O1rNO5LAV4cw1vNZ%2BqyVXIse7x%2ByQR4M7Y3fsk5m%2F5mj3fW16cwexrZeBFQz3Y1%2BEXhBLgIYBozZHRmSaGO5YII6S8n1p9Y49XrFQkBb91oXUW57vHLyhqBJW112df2BNVH0p71uj%2FaqCQF76ISZMxtqUK4YQiXeL8mz0vMFUh19GY60Yp1jHyHO%2FfxgGndNvbUooe5S%2Bn5%2BO2ocoxXSqwDr3hA1Jnac%2BLBiNfwlGXzwHk1PsOTue%2B5P6%2FvYCDuv8QYVRaAldbUXj3p8UrBi7y6rJH%2FA1ZpbhB%2Bz5S17VhKuFVo56cwlLJepH2lOhu1E7uYq%2FXL1wR%2BYnRgXzjv%2FDH7KuwXDpSRjSh6HHgInIJ8R8yYH%2F28WczP%2FH9XUmJOAD8SKW%2BCnQKjB1f26C9SXX3LqOFs4c72xVFGvs1qt4tWX%2Bf8VuAKP03XqZikZ493otF1SsFejs77Ks7jQhclwCPD0%2FP6fZzv%2Fc4whYXiizsvCL%2BUgSy9Hu%2FI6H0I8P0a46WdoEXfGoDjNYXhAjJRy0%2FXlmXpfVNFq0CE9d8kVLCyRyAC8ymZHXTvBN7uEF5%2FIJMNqMoMwGOqUBce1QB8yLZdGMvjUQUWQki9OSVrUM7fOKxlBb8%2FI07OwH6QNmNO5J9B9CVW8pdbx7EJPenCWhBtlchQ5yL9uvD%2FPTRiDI1Fld%2Fg41Mrw2bRYVQ%2BAW68tG4qvaxhiOnpUj37zWf4G3TxHLy9dmaMnWlXx88pitNYUQX00fWXi76s1zNGbAtOatP5EMKjtlHBj28OfDDvviU78FYRt3dfN4gaCzWySr&X-Amz-Signature=7fdfa017d43baad30ec151954146cce3c04434f481718b4295b1831e7f766b5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





