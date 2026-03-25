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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O74QTRQ%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDRmKqxoZu0GBh7IuQUQ8ZwzZ4Qo6JHjNYK4DT9ai4UyAiBJfd9UXhP%2BM%2FFxfDgW2wPlT83q1w1hRfdHrC%2BfYt7jICqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuP9Rifg4r%2BPIXEDUKtwDAuWgc%2BysppCLXYF6y0u6TZZSULXKhz%2F5hXGb5QRGxlau%2BmkokscGy%2FDJRw%2FtIh9ARw7s1KrgzmLtPVNidX%2F6ZXvKLZRfPkeJrN2YpR0OshqslhD7trIyqKh9Cbjl4hVesmSDOgHuECSDV1lHHF%2BFzAvCgLeI6MGuqPRwDHc7n3oyxAKVeewhCFRM4JySR3rpVRbP76FxQwiSpTB9yVV1glp934yvfxCLRw6qC5Rv5QWTbEgSh0RgOO8FwSCwD0IckVGmxck11wumE9h%2FgFdE0TXUPSTj033TnqEgFlHMD2NV%2BV6MOtYn6D5u5TZqS0qN7tSs%2BckX4ZnBb9F5dx320RyDEGUAmqaXGkiUIVt7tYTB4C6hEva6lbe8zJTvrvSi1EfTaij3LT8ceORVXC4mSB%2BMBDNt%2BIpHwMgw1kPRpBCczQ5nOXCN3JvymuKrocR%2BxZ1bkniL0ZKtuQ467ybrOiFiW0vnaFXLZnrK8UEii%2BwI5S1FIL%2FU3XsRV9AyVEGrzFkO485PLGraCQp1r1zObJ0CfaPnaY86bKjorCNKrdIDRix5hpQcQOXedsbQmVoYIQ45JGD2blk%2BPOk5ltotTPT16peK%2FPqop%2FYCB7z%2FJTYhgbRPAapdD1iFYbswiNaOzgY6pgFrn1EfoEFYCbOabepU0ps1XLQuoGXxBZ%2FPJctEBaWOZW56UqDulAfb7y28udp9gARQIxvZZx57e96gn491a4yEuwgVsoa54ARk60YuosdJ%2FJnbme6%2B1Zlvis5pF%2FPr0yFGn9gw9AuweZ81XA8nUrDq7LTRhFScyRsXt0AUwMOt8OALDBCaCvpyCdXboHUocsi6dfSXf26O4ivVq635Krq3iU%2FzYn1e&X-Amz-Signature=758856e58205a6285c9bc999b141770c2040c5b77866ef5a927620254e56c93a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





