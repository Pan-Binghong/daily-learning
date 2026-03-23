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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C4RS3HP%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEvppp43DSROBaiFvIG1y842RwP0lYlrbjnODRoZLF%2FwAiEAtZ%2F5iYcG9gneACI%2F104h4pz5SqnECIO5xcaLjbRQxfcq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDLXNESn5hONyTgprbircA4C3EbqbY639Z0amiffmHrRj2VaQb3ImbXvQMIU96%2Fa1pAXLCKlkxAY4aCLQBjH8cgP8uxDFzFUgU5UPKqa57HN6tGARVyXDRIuCu%2BoaG4hU4wFb6QRoMtqC6IOhe8%2BfmOl6fom5tibn2XRHWgiR9LpLT0foyS5Bzh2CVT1PtTqZdWlb6xw3KbkVwaVQ25oDyFqxzHmZl8nM3XF3L%2FOrUTd2rkynq1BsEK2K%2FmKT%2BAz052%2BNCnw9Va%2BfWJ3V9oA2uIvCSpl5K%2F8OXLby3CcT07ofSPkFzMiCkGhw3YNx1FCVepGn7r9yCVaw8qsBLlO66wYx82lQb5RM2iH839YjXqg2TUatRhYxnGaaqKP9h5CJD1b5O81DBfX5ffjlyV0N3%2B2PU3X4yoEOXj8XARJxdptTBD%2FV%2BNMQxNRtyJD8rSD0XpJf1eV7%2F0W4WLsJp%2BYpi0KbEBOimHjs6IeIXpBuWEOLhkflvVtPRbrk%2B2QmtUZDLiFnYS%2Fp1dhF4wIyf8Dhztnlg3LZC%2B865F15iBlortWvt6tnk2ZrtIWd4JTPqw1Zfs2hqbDQRExVht6oq1SuVcGaC8S0kje2TwispWB973hAcH8y7O8FQWdrTQdd52ZhGsaoOqTZz09GDD2sMP3kgs4GOqUBUTg%2B83kw%2Boddl97ZDG%2FSgZqUVoJLw3Fq8VigMAYXOEhnD8XW4SOYtXaVTLdqPOyfeRn112suozPSmiFJf8ZfWShkFuT1qrc%2BBIYnhtDhFYDV4qStBvVnG6FFjDRYNU4CJaNBRbGl2wGe%2BMmyk8S0S3lbTtbuPOSKEpJwy7izNsE0BkO10GoN1wQDF%2BP2Lr8%2FP%2FtISdKYdmqQ4SLpq3mgip6Mzwu6&X-Amz-Signature=3359d339a58a2bbd866264e108f2be7c051e3b68df15c0695edf448128bc35dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





