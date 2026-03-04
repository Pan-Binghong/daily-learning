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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VKKGCFE%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPmj3EX%2Fk8aCbj7t%2FvM1LuOr0suj%2FfsalGQmqlI3GsyAiAZsqQ1U3Mm1x855wosxQyNR%2BxIQZ5iiO7QIEqIXQpUMiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFWOy1KsaNGq7mo2kKtwDZikziskFNzkBHC5KGpqC8OhnQpNHdekBdiYSNQbf6WzRgChNwXGIVjsWcCq5KLqdbl1x2HS5zo1w9Zs4SiqKeEwTbL7i7e6X1%2BXu2D2K%2FJDlv7Wk6QTG1iMNzr8TlDOohZ4TbLqbFwidAj2IqER%2FI9owDfTV6JG0yxolaVjRJ1JiSuoEuOzCDyjcu1EA3uMJ9HPspQoWDCgDVUlfW5XgkWG6UV9XFjUQlfjVBrDqLq4Bg5lT%2FRJkpCn2y7N2QnF2aBw%2FFBy0%2FwTOwkidZHRSLOmf5YRSSTNlRL4g8wi8GohOmSXw3L9pCsEIr5zvbSlKBrHoBrxBcleqGizJza1da8mJsvtc%2BaPk0%2Fuz3P%2FURFSVy3xgm5DTbk9qceZsHSDJLUi7vUvPd7ablzj1100Ygz%2Ban69LvBhT5s8M4M%2BORQzyoTQrvYzx0jC3JoyPZD7C8IfVjvdesx2iY7DLEn87TyfiFWkDN%2Bi572%2FGO2D6tDto42xOY87RwX9CEe3atPeHL3NIQnvagWu3OoxJX55kaXheyLFhgj13rQPTWYWlBx%2FXaV2%2FfWPKEsQ3Ed6gxkM0KbSF2IdTcP58exZgxBE9hYoR%2BOUPzoyu2SbR06v8apRVn%2B8DuZVu6z58WoQw%2BZeezQY6pgEFv2qcbQiNwYuOQywoT0MtBmnzH2eG%2FCPWGhzZLXA4sN%2BBd7fl%2By2GDecOeEFX8xHpFKh%2Bd%2FwaQbkvxmxeRweHptjZr8XdiT84fSSJX6If1xP%2B009IPed%2BWCQG6m1X5xcykThtkMHcbTRNzYgpw2w7sCFN0XHdkMepUVLjkjVXfdio5RSiLo1pAYDL2avOOZsbviNZNkM1NC4wQ9QAeM4tZdog%2Fb%2BB&X-Amz-Signature=bc4f19e0a07aceca825f6bf928927ed6a0832be79cee8106bfd5f3f5df50881f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





