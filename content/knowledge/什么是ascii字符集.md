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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RIBXQ37%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMO5NAeWj%2FKtIdXtBZFShcJ7ujs7fwxMteW4UDCctZBAiAtSzQafyYTjJjyVtD3pnEJB7n91oyxc51bGFT9KCUsTiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDa%2BQ9TqLfDAGbkXoKtwDdGNNl0U0ojEtbn3xWwsGbk0cuyJMIh%2B6PfQEacT1a%2F%2BW4HWM6pVkt28F7gqJHP4mlflvqeyqe9spMu8MDpzsQQc26KLUJMR8Uvp%2BlIz69E8HbLBk7ZIoiQAvlC8TggMxSQNn%2FREBt%2BI2gSwixO8k58UZ9OSTnMa8M6Zg2SIDIL6JSb99cZhTaTOlk%2FnyPX6SgB3eeoFohPxC%2F3bL0Bqubwqw0ocdv1YgF1CmBHxqAwWG%2Fa1g1OpV7XoUpZ6YIeCZch2FuCl4UB6TKKTt2TtqfgXOk40dcpopa%2Fzplm3LGLjlEGXiXRH7LiT%2BW7JV1pTCADNQWOz3pFUbo16lCZ6AEp58ixMLVjdf%2BlLjUA5Yv28j887H72mL7QLfzaHXNFXP73MWtYFA9NBdGqVVNxAuUT5o16yJs5hmSV%2BLi%2F%2F94nnG2r3tSP2tbQGsguJXta9wSK4dF0UJ1ym5fIuGNY41TRHRYxQ09YkW6NogFnWijKyMR1Fr7LiyTqwsjCXmr22ym3CFXUK4O8ghMNM%2B7ZutfH7V0ggo0HFKPKeYAHtJVDJCPw3ACmZHH0tNkG%2Bd18tqSe4vrRpmi%2FvDDXm2ZWeKJm4HphnBcyK4cT%2BAaUImlW004yoUV%2FTuf6%2FOGbsw18OBywY6pgEIUpuv3OeuPE0tTQeUQ99HTwpGabxaKkCYmDykn986P6wVu3Ipy3wFq0pRulpaPfgOf52wnVRC8Ok4%2BJqs9g0Ih33lZBxt7bi0cAZnfDYwkC3DKz37ndlj643AnQ%2BtdW3oDwk4480GgsZkoqGl4nZfVsUyxVxns3VYluyOfNIIYJ2BQL3pDpPtmLheEMyYTYjer3zb0eH8W5kQldbqArQTA6wzPN46&X-Amz-Signature=91d517789cbaa2594054bcb27a0afaeb4cf32fcf3bc90883ace9edcf57f0b561&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





