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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5QXP3DE%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGr44ULHsn0I3xNK3vmeZHzVqQzuuReaDS7R3Ae3f8CAiEAtCykbRB4CxMT5Kwzr6i6pfj4KNKH0vlUOv2hrA0W2l4q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDDlZe8Jg9%2BSMjPkaNSrcAxJiD0JyNVGXwm524mUgSJb73QS3pGWGLchyTYpq1TN2Ir7dLE7y8jx4iFKepFBndoIHEHGgvdKeALOM8iBQGfG9shRdlI395w86Vm9WgHr77kRN269M5KfBqzmi8kGXZpoJw3mzdgHY%2B5SIw6zkRaIHUEL3Qll6Uygq5%2BTbAuVqENTppRqg8lVvLKnaXMgkmJtsuhMRozUjIFYcBvIwXz5LAIVeOfO3kafUBnaWAsa30l7ywInDSIQrd%2BzybhNGQGCA7WeZqU0tghoaG50lziGsnxyGl656%2FGUTSg%2FqqhWj2iBjAgT2IkYo45l5OoR7Fdb2OhVF3dFAPMUTInV8APQ6uFj4iHxYUp2WzJwsqCU%2FGuWo994RDv8z0znU3ocWDvOo6GIRpuPA8e%2FzmFmrVWWEpDNpEH7O%2BV78XEUWkZZhKx0E9zNpBSHggkWAGgcrEXj2JCzagKON31EU%2FUz7a037MeWmdFmDm8nP7u%2FtUrVKmiPBse8Xfz2eSO%2BoEQuClWzvRimcxqu7L45qllpW2MNhTOtxRMi9zB1%2Bm8y5nCbqM615p3Ex8mlwr8amA3Oo%2BrW7V%2FwQ%2BGiecGR0vSKUXgrmTlIbJSUTJENw54KxgFSvQAMJ7QY4MPnw1AEhMK%2BulMkGOqUBtq3MAluhoOXjDbUj64CfCS8M6pR9yByuiYOyJlt2DptTnT1roEJQC61AUwR84RajEhQBMSdShDysGo6EkzdIlxt%2BQTqAj4%2FqLH9At5s26jZCBBgG6DMbFmypMJtg2jqs07Du90U5W5vO4J0jnAmhmBFedbovXbHCAQzX%2Fo3ekKgY88IS9uVM94AYTPHQ%2FkZXeDkpMEsz6z0uaiwH%2FvI%2BbFm0e5AH&X-Amz-Signature=7ae063dc74e29bbbbc5ef8aa3409ee7ec5409990f7ecdb00260cb7612d60be91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





