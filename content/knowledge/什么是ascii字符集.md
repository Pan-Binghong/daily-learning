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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEVFK4EE%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJZY7S3EOCXFsu0O8tKmtPsj8DxR1Y%2BeW05Vio4MWOSAiBQEPgvxH%2F8duG88EDxRlAQMjVlCGUpvbnMCcW1KlOlmSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv3%2Fc5zWTovHRYtFAKtwDMUs089oHWOoxONFB17rQSK7vbOnp8jaEuw9Wgq5Gw%2F2OEpXydW%2BCkNPh%2FNGLzZy5ZFQYhH8lBHPkewR%2F%2BhTNSqgm6l7b7c8jpRYv08EKpkBk2txhpCV6Cx%2Bf5JLKRb4oc74VYdig6%2FhqH8KgDFQoMkD7AMJr4EpZ6yOUbMZbB8%2F3kBO%2FkpOL%2FxhZv8A4kp7zmtJsEuNlnTzfhTZtfoBYOWdL7yYPKIay4LKPNeDNYdnLGOOeuLuFSNiUaiPQh7pneu6KCgYvCGzHhOjhqgZcC5dN9MCnOEcwhYEtagZtHTjoZ7SjF8JTVEbZ2Z%2FzXTsdFxzuL3OLbiE5fIrFECvjLeB8unKoivBpG%2BuGKC6LOY6Ua5B9qEyjCNF9bU3WOALNdstW6Fa9w8qP7pc9l5T0q2emz93RLT1ZFYwtYW6V%2BNFCvPUErQomMHPKmDYBSEDJ%2BZvSsXQkWvwyBFeh0exmL5pMO5E8lLDTrSVs8tfT9a8wqvgDkMowH%2FzzpYlxlW2UYPUkdbmLl8%2Bdvb7JFS%2BbxkxYGDyM5E%2B87sn5IC37mXgsiDImH%2FCE9T0SuSX9zxuHn4shl%2FbWEj%2F9vjO%2BTz1UtoZRL7R3S%2FMMXdbC1KPf3rU2d7J4%2Fap7HNCXeV8wn%2FXRygY6pgGWwxGSaNvYv5qMyBo9ZA5wQSHcIXIL4hLj0Z78BTnm2mRbkWFfbfYVjWccedTlivfGbJSdejWhdYjSARyXGhH96m3FWekOAnz773b9Koxfdx6NnHLq8n0XmwHgpy8zIzhcTD9NXdF6vZRoyDO35pPV4piHGhstDDVTY8TKrEAaihvitnxNoDP6lecq40hLreBxQ52hgCPsr6BQOgif2eOhLAz1wL%2F9&X-Amz-Signature=539e6db1c88da0686b5f1ec21ac46007b3cc311e3c022239dbc35239941c0ff6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





