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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOGUAJ7U%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClK5Eqed3r5MfScTTEjExgjMIH%2B6ZrD5ruKXzKDuEyJQIgHLQgqQqx%2Bpdwqw4Gi4GQ04Cj4DJRqqPQ1j%2BK9JjinR0q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDLVnq3sd51YqHj%2FfnircAy%2B5dwIlPhVcunKfR47iVMyhg%2Blm2eSwQBGNRPjK0ck1RRhKlOkIblYVSt9eDK8P4Vnb3spiXoCw3qtckSNnG4slOUKqgizRYAYq%2B7V5ZiRh9RpuYXHyy0gMc9pCyQwujutPH%2BlwUFEYrBvZmn3n5VYWo3HoDhBKfgpV3DoBlXlBIyY%2BzExkyvlRLnVoK3ubrV72%2BtyCd3X6bQ%2FuV5LRRvMdJPuy9AJwlk%2B9V5rnDpOe5%2Bi7%2BPPjW%2BChWZvd1qlooP6GQYBlurxvgSuWhsKiSUm%2B1M6MAPG7hNWXzNAxFra7lzdDc4TCxTDbosTWsEKM2UrIi5xDcKuIh9HRH7P%2FBKDBE05oFgQmpDjdS%2Bs%2B0BtGHLJ0M89GNwfhEQNamnLEumI0mcMl2jqTrxM92FQotPuHFVjszp0OHl9YF1etE1Vtr5wR%2FgKd8mmrc6yjLHCOTiru6QSEqGewPqEn2tSyHG0M1PzV%2F2ZSube57Kevf5iXjE09QwsiaSyAmfG9B%2BBs1JqJxqC1NljvAoxqEBtv48hloCFNF69t6oY%2BDi%2BQrFoKS%2FURFjvOyOPpd6GLPFWUa8K%2FIVYizuo3QdkV1MfWsitJU2rQ2baEc9%2Banip5MntWWoGBFx20T7owDLOqMNmi68sGOqUBojaC7TwQOQfJaMdWZlnG7kTA7kakGvTvuvit4%2B6NyJY7k4ocH%2BzdJ0fGHp6LaAkNE%2BqNEF6RmxSBZ0SbYoOd89jmgRhqoqRZyxlQtna9MI4Redhw1N2tR08fRQDcBsH6IJulw9kQilzL4KkH28%2BBBuC04Ijbu9%2F%2BshH4fV7dcZgjw2u05DoJp2YhLsAfwfz%2FyDgR769HvKgoHh%2FKUcd4sd87FZt5&X-Amz-Signature=89f51f97f4d7bf45d8228208a54c89f11ed7332c4dc243a944c50736caf64b22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





