---
title: 什么是Base64
date: '2024-11-24T02:53:00.000Z'
lastmod: '2026-04-13T13:26:00.000Z'
draft: false
tags:
- Knowledge
categories:
- 知识
---

> 💡 记录一下Base64原理，优点之类的。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5acec283-4306-4186-b12a-36c0dd599f63/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K2XSST4%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGdBcFC9GAFAt5Su%2FFI5QaYFU%2FJbwf29UJc2TmPaP3esAiBjnINrUQCgpUhHtwg670GRmH4eFRAlYtJB05jfqolIJSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHuH001yjIBWx%2FhOxKtwDJmV%2F5AysETa%2FvxYh09vAiknZDHFmM0mzQ8KZPFVKCGZyrIX4lyh2whDOozxIfOEyFRWBMbJeSHtSMK3ueuidovkU5JC3E1X8ns7GCypuYvBDQ1%2F%2FCSd4mFOd0GDLtlalvbr%2BpyT%2Byo5IydEXGcUX33EOaqvmopht%2F%2FW7OxQpMfsmJtxkTXDRx1%2FYNxgPC4GbObsKvGaC%2FyPlKepwYaX%2FwBsDRm9tRp5MWgzis31eHT7ALBPtUC13RmKA5XwE0ByZv36vq1ZZbjRptV0WjpJVlwgHjc%2F4gIrqTF69Kh7RPhG8ZI71UhtjeST28w9iRYf1u6dEgCx2HJZBfCrDmwxedmK9dEaytG12mmnIKj5g10UlrR%2FMnzGj0P%2Fh6o%2FGKqvrR8GweHDR2rkYPATFNwJrjSXMPmXdXPO1UL0FePInWTWf7b0QZziVflfKNV5E%2FVq3Uex5GA4zVjX4yZ7%2Fy%2FUkdLFe949A7S%2F6zNTarboIAU%2FssQPGqSspRWOFODLqtpC7xfgGuaL9LztMril9tX8y6haVbHWNXWBnFSQgVEgFK7KtesWnBQ75Tfvi3oJIr459t1g2vUyqntSVOgQJQmGCWwkvWW%2FX%2Fra%2Ftyf6zcz%2B9uSOYCMBHyrmYLMENfQwnOH2zgY6pgHxDpAj%2BaX95smLS%2FNcNPXx8TlD%2BY043FeR8Z4%2BwFNOebjArTd%2BKQtcVjSJ1nTUT8qZPOaiB%2F87ThT5wMXWoVfB6%2BZXuEMArLy0WW4P4wvYxO%2Fi2vNVoGTYsdL6f2Cp7RYV98dIF9QKhf5b5g3eEd3yjfdFg4CYm3NJREEERJISy2iTPNmU5Bu4jF8C6C1DbzTUlfnZSl%2F9JYKQX5ntBSSWZ3aWd4QX&X-Amz-Signature=46473a6eb01fb87d0a07ef750f58de68e4fb83e0c7fa5aa5c2cb38f0870f3965&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 概念解释

Base64是一种基于64个可打印字符来表示二进制数据的表示方法。

常用于在不支持二进制数据的场合（如电子邮件、URL等）传输二进制数据。

---

## 应用场景

- 电子邮件中嵌入图片或者其他二进制文件。
- Web开发内，将小图片编码为Base64字符串，减少HTTP请求次数。
- 在编程语言内，用于对字符串进行编码和解码。
### 关于Base64编码格式的经典问题

1. Base64编码优缺点
1. Base64编码后的字符串为什么会变长？
1. Base64编码后的字符串末尾为什么会出现“=”号？
---

## Base64 Alphabet

## Python代码实现Base64编码

```python
def base(string:str)->str:
    oldstr = ''
    newstr = []
    base = ''
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    #把原始字符串转换为二进制，用bin转换后是0b开头的，所以把b替换了，首位补0补齐8位
    for i in string:
        oldstr += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))
    #把转换好的二进制按照6位一组分好，最后一组不足6位的后面补0
    for j in range(0, len(oldstr), 6):
        newstr.append('{:<06}'.format(oldstr[j:j + 6]))
    #在base_list中找到对应的字符，拼接
    for l in range(len(newstr)):
        base += base64_list[int(newstr[l], 2)]
    #判断base字符结尾补几个‘=’
    if len(string) % 3 == 1:
        base += '=='
    elif len(string) % 3 == 2:
        base += '='
    return  base
```

## Base64包实现

```python
import base64
from pathlib import Path

def base64_converter(text, mode='encode', output_path=None):
    """
    处理base64编解码的函数
    
    参数:
        text (str/Path/bytes): 要处理的文本、图片文件路径或base64编码的bytes
        mode (str): 'encode' 用于编码，'decode' 用于解码
        output_path (str/Path): 解码图片时的保存路径，默认为None
    """
    # 处理文本字符串
    if isinstance(text, str) and not Path(text).is_file():
        if mode == 'encode':
            text_bytes = text.encode('utf-8')
            encoded = base64.b64encode(text_bytes)
            return encoded.decode('utf-8')
        else:
            decoded = base64.b64decode(text)
            return decoded.decode('utf-8')
    
    # 处理图片文件或bytes数据
    if mode == 'encode':
        if isinstance(text, bytes):
            return base64.b64encode(text)
        with open(text, 'rb') as image_file:
            return base64.b64encode(image_file.read())
    else:
        # 使用指定的输出路径或当前目录
        save_path = Path(output_path) if output_path else Path.cwd() / "decoded_image.png"
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 解码并保存图片
        if isinstance(text, bytes):
            image_data = base64.b64decode(text)
        else:
            image_data = base64.b64decode(text.encode('ascii') if isinstance(text, str) else text)
        
        with open(save_path, 'wb') as image_file:
            image_file.write(image_data)
        return f"图片已保存到: {save_path.absolute()}"

if __name__ == "__main__":
    # 文本编解码测试
    result = base64_converter("Hello, World!", mode='encode')
    print("编码结果:", result)
    decoded = base64_converter(result, mode='decode')
    print("解码结果:", decoded)
    
    # 图片编解码测试
    test_image_path = "test.png"
    if Path(test_image_path).exists():
        # 编码图片
        image_base64 = base64_converter(test_image_path, mode='encode')
        # 解码到输出文件
        result = base64_converter(image_base64, mode='decode', output_path="decoded_test.png")
        print(result)
```

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4816b9e8-8c12-4913-b787-d8fd71461dc7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K2XSST4%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGdBcFC9GAFAt5Su%2FFI5QaYFU%2FJbwf29UJc2TmPaP3esAiBjnINrUQCgpUhHtwg670GRmH4eFRAlYtJB05jfqolIJSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHuH001yjIBWx%2FhOxKtwDJmV%2F5AysETa%2FvxYh09vAiknZDHFmM0mzQ8KZPFVKCGZyrIX4lyh2whDOozxIfOEyFRWBMbJeSHtSMK3ueuidovkU5JC3E1X8ns7GCypuYvBDQ1%2F%2FCSd4mFOd0GDLtlalvbr%2BpyT%2Byo5IydEXGcUX33EOaqvmopht%2F%2FW7OxQpMfsmJtxkTXDRx1%2FYNxgPC4GbObsKvGaC%2FyPlKepwYaX%2FwBsDRm9tRp5MWgzis31eHT7ALBPtUC13RmKA5XwE0ByZv36vq1ZZbjRptV0WjpJVlwgHjc%2F4gIrqTF69Kh7RPhG8ZI71UhtjeST28w9iRYf1u6dEgCx2HJZBfCrDmwxedmK9dEaytG12mmnIKj5g10UlrR%2FMnzGj0P%2Fh6o%2FGKqvrR8GweHDR2rkYPATFNwJrjSXMPmXdXPO1UL0FePInWTWf7b0QZziVflfKNV5E%2FVq3Uex5GA4zVjX4yZ7%2Fy%2FUkdLFe949A7S%2F6zNTarboIAU%2FssQPGqSspRWOFODLqtpC7xfgGuaL9LztMril9tX8y6haVbHWNXWBnFSQgVEgFK7KtesWnBQ75Tfvi3oJIr459t1g2vUyqntSVOgQJQmGCWwkvWW%2FX%2Fra%2Ftyf6zcz%2B9uSOYCMBHyrmYLMENfQwnOH2zgY6pgHxDpAj%2BaX95smLS%2FNcNPXx8TlD%2BY043FeR8Z4%2BwFNOebjArTd%2BKQtcVjSJ1nTUT8qZPOaiB%2F87ThT5wMXWoVfB6%2BZXuEMArLy0WW4P4wvYxO%2Fi2vNVoGTYsdL6f2Cp7RYV98dIF9QKhf5b5g3eEd3yjfdFg4CYm3NJREEERJISy2iTPNmU5Bu4jF8C6C1DbzTUlfnZSl%2F9JYKQX5ntBSSWZ3aWd4QX&X-Amz-Signature=c308543819f5094c648381297275aac739ad11aa414c6f78cf831a5fd5b2b251&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 示例

- 编码Man的结果为TWFu，详细原理如下：
- 特殊形式
---

> Reference











