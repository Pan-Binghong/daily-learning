---
title: 什么是Base64
date: '2024-11-24T02:53:00.000Z'
lastmod: '2024-11-25T01:10:00.000Z'
draft: false
tags:
- Knowledge
categories:
- 知识
---

> 💡 记录一下Base64原理，优点之类的。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5acec283-4306-4186-b12a-36c0dd599f63/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCM2LK27%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIDfpmWKMn3O2D%2Bim3ZY26Nmu14b2hlCjsro4knWc1EuXAiB4Q%2FqLJYXUNodZHm4PcvXXw9XdfrS3WGXmU4QuUT8STCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi3Js3EvtN1KA1ozIKtwD5Xot01QTiTjxVKqYPsPPA96IUIY769YFl2TttuuHLBO5IOb0IfHHL9daew47zcrLNhYy6aJftbd%2Bp18V%2FthB1HOsbknO3i96Bbib3yGcCALJBepn9Mz0UK9ANciLKZVaz8Nn7FuVp9EE0qw8Se0lRLTLJShKCxLklLlWe7iG5hhLIZvTTTL1vLJ1r4KO5WIy8aOPSBOOZZzhvOTR42cImPbMLVHftdW7FI%2BCLEjcEa0OVgiL5e1mjCHhSIPwursEX%2BQITTLqqBGXDBJo3VMPPfnSnX7c8isvcxLmslU298OcPnZ1mQk20uqWgZAhsecOTS%2BYUmZThnCm%2Bzlf4E1yNzttkG08dq3tAPpndmup5220gRt0wOda%2BV36AA0Oe%2FinGI0Ko4LkOKtGW0BYGw4Pj%2BVpotLfxXHOSEjCrtM%2BzyNOZPcYjcZjoTNKL45sE%2BsBRqTI2wcmbL6kmHpu8%2B8i4RIvJir6FGShUyJOzNOD8UvGtZC0u6B4LGy6DCZyPwTt9qV%2BiBxGTTeOcZEoRUL3UvohLCsSUGKJ0AbkRmo36m1WxWkPOh3nAb5BPyzS8t4TglshOPgo6HrHqeVtjJdXp4CPrbTSNHAC2ra8jsw4akAINFmFWeKl2G4vWL8w5tfFywY6pgF4uZ4ZDJJarONgaWqFAft7q2waN4Esf2AkJDYtsqh7k%2FgwOcQ8FHFrH%2FgLIAAG3l9X%2FnA2Ahi4i7jpiVVnCgXqSELteWe8kXEIPHdmVGUqvGP%2BP%2FgLeBpNLNNGpbwBV%2BonzvkL7u%2BCk2kU%2FWXjELf87yHed8RaQ34Yzmrv5X3DSDLHS2Hzn9n%2FJ1s2IXDZM24Pilz7hlMzrY3uP2zV0j5h%2FaOlIzav&X-Amz-Signature=1d8d5dd82fa24338fec8d71fb893b0ba1fd6523a2aa60474a21e2b4f88dec5ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4816b9e8-8c12-4913-b787-d8fd71461dc7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCM2LK27%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIDfpmWKMn3O2D%2Bim3ZY26Nmu14b2hlCjsro4knWc1EuXAiB4Q%2FqLJYXUNodZHm4PcvXXw9XdfrS3WGXmU4QuUT8STCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi3Js3EvtN1KA1ozIKtwD5Xot01QTiTjxVKqYPsPPA96IUIY769YFl2TttuuHLBO5IOb0IfHHL9daew47zcrLNhYy6aJftbd%2Bp18V%2FthB1HOsbknO3i96Bbib3yGcCALJBepn9Mz0UK9ANciLKZVaz8Nn7FuVp9EE0qw8Se0lRLTLJShKCxLklLlWe7iG5hhLIZvTTTL1vLJ1r4KO5WIy8aOPSBOOZZzhvOTR42cImPbMLVHftdW7FI%2BCLEjcEa0OVgiL5e1mjCHhSIPwursEX%2BQITTLqqBGXDBJo3VMPPfnSnX7c8isvcxLmslU298OcPnZ1mQk20uqWgZAhsecOTS%2BYUmZThnCm%2Bzlf4E1yNzttkG08dq3tAPpndmup5220gRt0wOda%2BV36AA0Oe%2FinGI0Ko4LkOKtGW0BYGw4Pj%2BVpotLfxXHOSEjCrtM%2BzyNOZPcYjcZjoTNKL45sE%2BsBRqTI2wcmbL6kmHpu8%2B8i4RIvJir6FGShUyJOzNOD8UvGtZC0u6B4LGy6DCZyPwTt9qV%2BiBxGTTeOcZEoRUL3UvohLCsSUGKJ0AbkRmo36m1WxWkPOh3nAb5BPyzS8t4TglshOPgo6HrHqeVtjJdXp4CPrbTSNHAC2ra8jsw4akAINFmFWeKl2G4vWL8w5tfFywY6pgF4uZ4ZDJJarONgaWqFAft7q2waN4Esf2AkJDYtsqh7k%2FgwOcQ8FHFrH%2FgLIAAG3l9X%2FnA2Ahi4i7jpiVVnCgXqSELteWe8kXEIPHdmVGUqvGP%2BP%2FgLeBpNLNNGpbwBV%2BonzvkL7u%2BCk2kU%2FWXjELf87yHed8RaQ34Yzmrv5X3DSDLHS2Hzn9n%2FJ1s2IXDZM24Pilz7hlMzrY3uP2zV0j5h%2FaOlIzav&X-Amz-Signature=c7ae1a7f050c625251e4de546aa64370422174957a8f6cb6f64220de72cd51ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 示例

- 编码Man的结果为TWFu，详细原理如下：
- 特殊形式
---

> Reference











