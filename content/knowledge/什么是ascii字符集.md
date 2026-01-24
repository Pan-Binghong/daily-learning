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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QHB7VEJ%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIFlsmlVjpID18KIkyd5btV9NMTrsPspVD5d27l%2BE7OZDAiEAzWdzbG4sgDhpbb75Cc6oskgbQMuMLpSBKpicHT1Lj1gq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDLIvwhLIKekj%2BtsOLircAy2pvZgX8jpEBIpYP2mLJLKTLGLBIQAfK3N07KbpUalf2hATGEQ%2BMTZi1WfO5CF6acx6gK2qIlSIkWKvBo4DE5EW1iFzZnXMgXMl%2BDJVGF3Vcmysb2uKRYji5IhIHtTadK0O%2BO2CLQiCNExRzX1ubuGkMYvGm%2BF8Ax50U62YrV6onzjyCiWj2VqoUcv9x%2FLX0LxJGqngKJtzsCH7yIlLwkomEnFOiil6DFpUgLutzkTGSE6gpNdZWBYlFYFFrZMRDzsI2OtZm8%2BAEEo%2FlLijfKQyJgvannkxpXrY0sP7oaz7it89FJ%2BpssZPM2ziy%2Bqy59ShwPC%2FAz9u4Pls%2FzFIVNXyjgvW8tap2iqjO2STp7fg3mW5BmWlVgGQ1nDg4VtiLMH%2FcM3AoQg7jZHLsLSFB0DQpXCWFZqQ3ZIU8VglcY3imJKg31ap%2FpDkeYz9VSDoak2X8HSTL7tlx5CY4EZhKhs6U3pVH2qpQyjGbQl%2FiiR5C%2F%2FZZENZLXk4yez8BvBrbGvxQ3XqXKPDPT1BqoOyJRGTJIHzfPcp6fw%2FR3FqE%2FMGYTWtvwjf3VaAieVRXSxHMyFAebk76d84KFLvVWZ7EuBKQUK%2BLuohrRjMIwLcBzopRqXNY1xnp5Mbzq0DMLLO0MsGOqUBbOHJyMMNGeF463YIY3cnXFFwXJxDnE5Nsm1gEhCVsL65bBivaXGklQHe18Kx2l6CWjaGqE%2Fp5AoyKl0Vg%2BTRFzS%2FNlWDcGOhcTTnSd6wmO8krQR%2FOwMGFvx5EJdJI%2Bygt99P06KZlpd7yTKf7%2Fn5TcJwvlQ5kPEggwjs%2FAFrWGZ3dQ2wxY8BxowM1hkAIHSXh1ACy7rEQew1mkospgHu%2Bmb%2FruBl&X-Amz-Signature=d908ee8b35b1b3e2d207c584015b6728ef1893d15f7135db4abb76ac4946e6f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





