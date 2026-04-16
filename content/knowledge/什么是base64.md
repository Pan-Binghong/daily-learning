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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5acec283-4306-4186-b12a-36c0dd599f63/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEPDYSLM%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHJ3cB3n0o%2BlpnYl%2B7Z%2FqjMy7UzvGNWw9b1AxJLN6ypPAiEAv7jTdsRHdFEMz95CtfirdtQaELBrJ5l7gfVCTHpuePEqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMIwzWJfiiQWrME9SrcA9Nm2uqypwIWGO%2FuGAam3FZPNBqLYomwDk2UOH1ptawbcVlyap9%2FjvX3vHYH3CncgfgTTmfflvYgDYW39WaE0jFiTf9pAahDfitE6jyIDYGjALQMxbHyykNP8%2BbK2t98uOuMJ2uRLefAMU1PUa6%2FgU8xgVwXVHUzvfUq3t8Qqmh8KoMBMRXZnX2n17YpXBh8AFg3sf0vJUoNMnZUhKm5Adq6YOEFFcXN2Bg8PpDOFf6ZPN%2BCgPwVsk6cQqLcRE8xAXy7BFT7PxfUcgdDpzxGwiLYLY7R8XcjiH6gqudz5uoLXzI8e1jIGJUVTAIlIBYu42b4jO0QmXXT05TkYbaqYuhzc4bKjzULxlv7Ng6sQqu9%2BUWP9u4PsgU3MXcq82LHmNlL3hEANoRBWXr%2BT8chgoE%2Bi1gufP0K8D9%2BK9kzm%2Fiy1UXId0RGDQpeLIc1FfcLCxbxPit%2BbOu%2BmeFFp%2FY5BDm4qMoxpPD9MgwvjFmBF5AL0ypLEXUCDKokruWtz150lc7yQv0NucXmB4%2BiTKr5fHWEds6zLEN2yfoP5ytQxL3ZF7VKIShadDCGjAbGVaL7X%2BJUwNFIYR%2Boo%2FYGdckh3xH88JFfsh6hSUXRK0isOrCvN4Vu3KY%2BDFEM%2BhP%2BMI60gc8GOqUBV8VatG4VTXBQQg2QAhzP9YsVx2vcq5iAtPkstB0i7oc65Jc6ReXo0akbNP7l%2BVbVxRsfnefzyYmIlpsVBE2SggOYwLY57goFGjGlyWqx%2Fy8jnmGjk0MeKyjqafyXTWFRGTGMs7yOmrqROFyTZS1Pz%2Bjfr5HF80mddkPAEjDzauzIQ%2BMmlpm8rjT0Tr%2F9AAg%2FCH2oIbIKr4xPGjHNPah5vm0rtyxe&X-Amz-Signature=ae7d94aa984483da187c8a2e3ff2b32aef0c1407968ad587766238da5758a022&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4816b9e8-8c12-4913-b787-d8fd71461dc7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEPDYSLM%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHJ3cB3n0o%2BlpnYl%2B7Z%2FqjMy7UzvGNWw9b1AxJLN6ypPAiEAv7jTdsRHdFEMz95CtfirdtQaELBrJ5l7gfVCTHpuePEqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMIwzWJfiiQWrME9SrcA9Nm2uqypwIWGO%2FuGAam3FZPNBqLYomwDk2UOH1ptawbcVlyap9%2FjvX3vHYH3CncgfgTTmfflvYgDYW39WaE0jFiTf9pAahDfitE6jyIDYGjALQMxbHyykNP8%2BbK2t98uOuMJ2uRLefAMU1PUa6%2FgU8xgVwXVHUzvfUq3t8Qqmh8KoMBMRXZnX2n17YpXBh8AFg3sf0vJUoNMnZUhKm5Adq6YOEFFcXN2Bg8PpDOFf6ZPN%2BCgPwVsk6cQqLcRE8xAXy7BFT7PxfUcgdDpzxGwiLYLY7R8XcjiH6gqudz5uoLXzI8e1jIGJUVTAIlIBYu42b4jO0QmXXT05TkYbaqYuhzc4bKjzULxlv7Ng6sQqu9%2BUWP9u4PsgU3MXcq82LHmNlL3hEANoRBWXr%2BT8chgoE%2Bi1gufP0K8D9%2BK9kzm%2Fiy1UXId0RGDQpeLIc1FfcLCxbxPit%2BbOu%2BmeFFp%2FY5BDm4qMoxpPD9MgwvjFmBF5AL0ypLEXUCDKokruWtz150lc7yQv0NucXmB4%2BiTKr5fHWEds6zLEN2yfoP5ytQxL3ZF7VKIShadDCGjAbGVaL7X%2BJUwNFIYR%2Boo%2FYGdckh3xH88JFfsh6hSUXRK0isOrCvN4Vu3KY%2BDFEM%2BhP%2BMI60gc8GOqUBV8VatG4VTXBQQg2QAhzP9YsVx2vcq5iAtPkstB0i7oc65Jc6ReXo0akbNP7l%2BVbVxRsfnefzyYmIlpsVBE2SggOYwLY57goFGjGlyWqx%2Fy8jnmGjk0MeKyjqafyXTWFRGTGMs7yOmrqROFyTZS1Pz%2Bjfr5HF80mddkPAEjDzauzIQ%2BMmlpm8rjT0Tr%2F9AAg%2FCH2oIbIKr4xPGjHNPah5vm0rtyxe&X-Amz-Signature=1da21c2980b9c1686f019ef70e1f89fce4b852f91ced4aeba12bddb7656d0e99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 示例

- 编码Man的结果为TWFu，详细原理如下：
- 特殊形式
---

> Reference











