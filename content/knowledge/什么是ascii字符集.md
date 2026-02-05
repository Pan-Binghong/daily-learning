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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM6TSESO%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDqjY%2BS34v%2FO2GpLIQSxE%2F0J1GPCLWBylFrzgtvtfcnFwIhANl0G963Ao4baBFfdv7FBxCJUnIy9G9nXDjZ29aaG5mMKv8DCCQQABoMNjM3NDIzMTgzODA1Igz0xcnNBgcXr84iB8Yq3AMMlYh7rFu%2B7Dif%2BQpAP%2BPgvXqEHKgG4GfqFjTt%2FYqLl2l7yIe7hSV4VOQ%2Fi3RCx2P1hDYcLXqzEjunqj0z%2B3ruYCZSpB%2FfEO3LVop9fWtF%2BWXZwKMEK2tnXo%2F%2B0lLdGaNl6KDKYR%2Bu57KlYyTQrhMwhSQqBahYw%2BbNYoixHaeu%2Fez65fcaQ4wLtskO%2FFUdIYIqw7AKN2WZOvqXJc2QXwr6b5tSYC4%2FVNT8nD6fOQc1TKjoDa7ERqJ%2BVR6%2BWVN2dK9SExZayN6iXbRTLslhsgaxQ%2BNTjjX1OUztE9oQ1Hmu8kl%2BmMpR5hUKzYZPE43ZsxETZDsGM4W8hOlTBSMMnjmxFJFVmbwlbnRHLE5GsE6Yiqwe5mOZ0WJyiAVQUuON%2B2qguA2cr0VzsMeIWDYChRtARorBrx7sj6SNV7ePzUIiy4dY1i6vzI7ypRLQepyVaeM124edmwuq%2Bv5Cs2QyCKWlwTv5zsi7zsMk7DgqiUU1wkGylic07Xi5n%2BnZrs7OTtgKshtqdzbP2eucFsa8BAPLZu3zxW%2Fxyfi1lyrD5uAMYP4UPdNTPYXX5MBR4rSMMEQsi%2FxWhOEoqxzOPFypF9yUzU0MljorrvETkNkB2CMClBDJAZeRTQYqVSNnrjD%2BkpDMBjqkAYJ8rllpW%2FrPe1p4Vwqoi3ex7MWYb2IC7lBhBJNWqFJeiqEScdJ6JcA3FZmZL2JAIdbZJD9OX7JayZp1plzQOZcpzszib4ggcrpHmdwthTynRihT%2B6fdNT8jTQ6W4AhDQ0ggQ2HIZMb444zpT3eJ5v8vZWBFuUgKMzkgTkIH%2BKmQhFlx04%2Fc83hvz31Y94hJBmCMkUopPTMzVaKSPqkJMpFrRUZ%2B&X-Amz-Signature=1633b690ed9f4342fbfe31fddaca22abbc1e0ae87516290f0080b238250eec77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





