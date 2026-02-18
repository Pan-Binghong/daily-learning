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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIILX7LT%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQpiOISm%2BrQ1nPPYbTYuqYNOahxm2abhCMhUvl5QiP1AiBgRQ8QsUx4BtB4Fzq6kv4qu18lQcYXbpFwqYLD9Ac4fCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMN1TNRabxiDcRG0JlKtwDerc9cwR6fGRWkjDjtupNGQOshCcVdf0Df%2B65ZjYLgwb77tz4NXyk3GJjOCSBNRVpmfwA7JDn2D09Jrh4alxKPZR8cmKsLHi1xKLNSmHRYRR9zqERW85MQLS8%2Bw6cT3tD24qvvX6C8rhq4rl1keYXMxMo3q2FL0wTFjoQzhGV%2BAlJw0dPdqc6A0jPdHQ%2BlCQ67NNXtrw0rJms4TkMb%2B2rYdg2gRiRvdBIe0Kja%2FtI5kAoHEAEhreTHKhGkjH37M9Pm4W8wfsiuqar5QDIro8B53DdRs3mY5DXxwsQpfa4ZG%2B4EYTA7exWTBYhV9H3BA9kfKLFxVIzGsR%2FkjCt2RVcr2LFSWvDv18kZ4kOzcV4fWCwVMB0YlUu9mPaEjAqPIgyh%2BThZJVTrUuYN%2FyZdWfWlME4yAQ9Dau38qZ1gCXxh21lMXImmI%2BuzzrnKhHhdOQ3Af7TiSUV75gz%2FWnkYvwJD78Ug6Jld3FYK1iNky0VGBy1VLTfaUIkut5qx%2FpySH2CVTPiVklVuoB0DXhDWxfXBlzzVBhHzSq3cPF3RHW%2BqxJLkfkvAfWA1%2BO0hG34paqv4Wl1j5pXOwi0Wz8A3TC1PDsJ3aq7xNBkM%2BlUeDL25IK4gXoIAF83juyApa8whp%2FUzAY6pgGWsqOxz4kg1rxxKzwbMPKnodUVg6pvRQnJZNALU0jBJGNB6fA0awRW6yHQNKBndcU5hbytq4GhPdSo0owb1060w3reAAtaOg078UY2Z52ug9SNBh%2FqKD54GUVsK%2BPTXRjYwOCID58Ralo7%2BVMNvcvCZmiSD2PXg%2BnwqVydd1H6Rp2i7PjRNDPqCjLD1VWOP39z6GIL%2BW%2B0UK8lTPVoNXrCLge%2FU8DJ&X-Amz-Signature=3481154b9406e45dbeb9fb63e9ab8773aeef26b48a252f45427fb83f2202110c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





