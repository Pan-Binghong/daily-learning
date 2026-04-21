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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBCBZ3OH%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDQ73ZKZa1KAXmadiJYVE2q7iEP%2FFK3cKrAehIk%2FI0LAAIhAIyrM40YcEowSjZgwxpMvWlQcJr8fLRmTzFb3%2Fzoz3tYKv8DCCwQABoMNjM3NDIzMTgzODA1Igz9YriQ1lMn7CAgol4q3AMZETWf4a8%2FfuWtVX4C4FRH1a5q6OfUdI4b0wpQgRsQIcUE4SyXoQ%2FbrTocapLdhqbciWxIJn19WT0J%2Fc77vpA8z60YqNbsuj3xJRn0%2FARZs50HmIdq8j6RmwCaJy9PtWtOqeyZnwHc5utKfmH1tk3GZLAnFYnpVywB%2F%2FHdywly6lMz%2B7oMIf9kWRJsv3LpqlL%2BCBVcOXot5jlTwlz%2FGoADR%2FLEr1Oui9lUIClkECQhjUexSJNQUs07wHFXim%2FQ1YK3FXvMSGu78J%2BJX09PyKT%2B0OOMjvvH9Cjs2Ja2NwzGmkPGJhPDQiajSA9gHoQRS1qFaji7hT6WYLI7LiJMAo%2BV9JUX2mmZvm83W36YScvIlp3DbEoaS34OFA4ojBb%2FVPDhNe9NupPsrQAnohe1tlGqmyHtbCoLjzVuaTxyGix1o%2Bep76AVhyn0CeWhoC6Xe6LjUbKfgIqsvHfqg6UuyRC%2F6uhNHc2l%2B6TLHec%2BpBF3vJ%2FOVuWu%2FXfLZqpSXkjhKHofJW5CzHCCKpTdV0Xk0O%2BDim3Z6o4kshRfvotgP1GtkKqvHizW68SdLhruITlObWzzKd8YOROjeS5dHOvfDOUzss5O53M9bNo6mJ48H%2BssAG5QPnj%2B0HT9VeEtvzCN1pvPBjqkASaso9iwiVuPjqbXWez9tsGVhyYH9SsrjrIoi8MYNLU7TAjXlCBhMBdgRydYOgBp7JtZuzvNc6aFmsJLycnOkyIOP1Q9yM%2BfBb8XwS4JwBvj8qPsHcSA6Z7CbALMpICC8GizUwXTR59U1T%2B3HSp3FuDw%2Ba7GBaeh1XdgXj1KNyVr8WJQvxjjiLXIIey0qOXtJV4vF%2FEsV7mdb3zJKZG01%2BkDjMu4&X-Amz-Signature=1dafb7a38f85cab2954e4cf37f7d7274376f40f9e00ed3d642187a55c59f965a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





