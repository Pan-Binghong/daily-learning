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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S3ZTFPQ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2vm%2FAD61tMypN0GojX5N78wKCHa%2FsWoBVpCkC1EY4NAIgMS8sA8ClxywLVWFuZxNCNaPGkKCmSQXZp27tGw9DuvcqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHiEXr9kjROjkDZrXCrcA9fRFerIhVgRniDMKFOgrVsxai4DQpuxjKn5wyJWCtYUJwUP%2Bs9yEgCHpT0JfMmkHR1JCFAfxXRbjJMVnBWFtKAq1j4fIKQGleqPUYd%2B0tu5c9A0C2tLUh0xVeq1MKf4C2tbc%2FwLrrSct1c9sdmIg2iMyG2SWmXwoaiZlJP16%2BhgCtHNwRmLe6N1s7Jj7RAWXHQ1%2BSMWePEXTEd1k21wZlhdBHeO200YGMqHBpUOEWfUWtRFhBYJ3JfqVhuz1mbhQGURlR1pGUHWV4nW1QJGIcgNFVSfMpkNk2hNdzZ44KBWChWSNlELGOvRkrs3aWyYSqhmvG0f8%2Fppiy9Y9chWGHXXSInwYnLs3B8IcaBt%2FzXuG2bGFUegBknq%2BjkLhmzmPqRdAWJ7uV%2FZ1j6oa44NArt52zFCBPlVL%2BfMKfW5BD2TgT8qq2I0B9oGeZ5aPPjEfE2FABJ5AMkD2HqAS5Y%2BX08d%2BqrpZhez0WPCZlZh%2B%2BXZaAw6cviaWeg%2Bpdvw%2Bx0mNdidrCEOqghsGeHTrw%2FYZuAvAaKQA%2FzS2jr%2FMoi%2BBeQFi%2F7od%2FUl%2BLVE2ysfqS2Fo1EfUj7bOKesuBiQcOqfdNzu3WU8eGui%2FmeCW0BBxeOyVyqKksL5pdlNCGCZMMW3zc0GOqUB5lx3SiXfRhZKBkhGsCsdQKBRHDKJBLfcOeJpJroDjqsgGpFZ5%2Bi6rdcmg4LbDBSPj0j761kMFdxFpdRp2VuVPt3f6zgxtUeV1C6IJf7mIjdZha%2F6WeGpAgWqs8MHnmTpYR%2FULH%2FYRwqyoWiVgsw8oqG%2BHW7J45i01eAVwZlrNG3CQkUtW%2BPkgi9LM%2BigJdkz3PlAW%2FbdQQMddCIC47x8cTYpJ7Gi&X-Amz-Signature=8310797cd81c9865529e74dc4c0d0c6b174642128d654de1cf62265382284979&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





