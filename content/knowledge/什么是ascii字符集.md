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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9530f324-66a6-4b78-a32c-dd11cfc4a7a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YADUTWE%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQDgxkAWVD5W9Nn36qHxpxQg4Ak4248VK4X4dmR7FNJnbwIgZYmZ8UObs1OuCgRvJrPyL2zOhHs3Oo%2Bwg%2B1NSMyP71Mq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDIe6Uu3clYVfAv%2FzdCrcA4QJzES33jh3UMsWna%2BCMvyZ4HfW7Sntwrat9AfGfVPLDUWrYayu3SCVQhv%2BLKij15YJv6pr0NpP3ICdTiXqmQ7SeutvVt1gNi1Z0LkUBO6fqi89ORgacxcxSeO%2BfcfuEj9VzLuC71iKcnzLZE4L3muyC5SUE3mIXBpGziHT5bhe1XHFaP8%2BzQM6IcrX97Ao%2BTid%2FmiXFIi2J5zEud6%2BhY5eDEQn4gMT2UbRBPd8tYtsbIxMQY9x7UokULEEM5PPA7H5OjE7R3vooQJSIkFZY%2FSSlefZLkFfPYEfbhhyjVrTDGfQN1viJIjy3z%2BZ9UIJ2V0xp4lsXlD%2BSUtndtto5XPu3fdRfQLKAbaLJKg27PN07xDns3jWkEW9VLJu4C60C%2BQuO84KKwbrR560EU%2FVhHsVC33kFES1rSbj0E59j2hUw%2BNXK4jTNd0fWFnY8LvZz2kWyf%2FQ%2BJWPepTvRFtyeR8zaglZEhqG16BZmqufnbGPiLYX1WoNYTqjr%2ByLLy9iefK2D2rt379DwtcfMsCt%2B1Piic6jUM6m5ZHbN54ggxLg3Fuqo0pjNvWDInEw0BO%2Bfgx3Txh%2BsC3RJxP8yUQQr%2FDiLLxDulU7Cx6BsoLV6sVb4C8sUssgNAxpDQLoMOzUw8kGOqUBZr6ERqQ6vgu2XvpW0PtjZa27Xcu3hzunJvzGMM2O39YbGi0T6ja1c%2FYJKkTzL61rpwZ7FTKBVwtmZrgz9uTVmuxtPHbqRfU4KpmXysRYbV4KFtgsHixNglfdbLmQZK7z6Yp2AhCeTX%2Fmyt%2BZuDIk61jwiStBGjfPJE3Sp%2BS0MgqbScm%2FfqxZhCxtLCelLsem7PUu%2FlFJkMutQR2r7xDITNa2cUDy&X-Amz-Signature=dd2b823388ed8d93e22fbd9c5a256df6a5e80c27ed9616099c06240cfb1b9d01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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





