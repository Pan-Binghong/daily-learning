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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5acec283-4306-4186-b12a-36c0dd599f63/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQIUDXSZ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKMmsU6Oo3q1%2Byf8800V7XYHl9pna3LqpMUUuQ0ZdhVAIhAMe9IgqhOgjQ3NryE65g8LFf8KzFovjrCXMS3VqlQttHKv8DCH0QABoMNjM3NDIzMTgzODA1Igzbdog4g%2BTs4YQMAFoq3AOjSZo5Q3bgyI40d%2FJaPohj2E%2BQwHdF2QMSz0bQog03yjSdfX%2FjNAx162yuPoXVrG6fCnj6LV%2FICf3SoX25wXCFc71W3X7bsRtc9NbRUioNR%2BaFlud2IzZ9wwprXlJG9WN9v%2B1yQxyIL8%2Be53%2BiJsgxz3j4%2BH9pgl2%2FQ5GNF6uG1ug1lDDyZKaXVSDiMtFONZWXXooH6uKJKs%2BWD3FsnZf24xCFanyhx8htpMTKtuxcnjD1BsEnJIN%2BAnANHdhBIxTUQbXorgEjPXyv1cSITeI%2FHYCRWnDrT5uQ2FkMn4%2FX%2BtTN%2B3tqPzSoN8xaqNWgwuijHO51XmpMuoIa8IUK9a9ib%2ButxBb7t9BE8VRogDRDmGWs009K08naL0UZjfEH2FyEsHZ65sqttOrRZdsB67xgnKVVnHSvLKLgk1Pl8vnNCfrZs60e0ZlEyTzJesJrScYUPEBLZqt4iVYa7eS3y4B%2FyhVa%2BMR%2BjXhjbGdV98dxNxRVEff6ZXRiSlEdOded0lp3k27Y0DdviEpp2s718l0sa%2FAcqPQTqsFTR2eOZ1LyM0n%2FPq%2BkdcVqSx5HY3kQoUJNsMPeaP7Qj0ywk67jaYdGcjxi9ApGrh6hTUV5KRayAIZq5zN1tfzjBDhxSDDH67zOBjqkAbGzqbh7ozO39%2FjLrECtWx4%2BsOiZHkGiPNiZpwrodMkwbzFgseA3rEPGD6p4%2FIQ4R7PO97nLtLhOphLgQAstcq5g4Oyqbgi8VN7QS0AeS%2BjHYZn8W8vWTI1kKkdpBwhXrSxpBYO8BbAfhnYTFAp30H%2BWuYmu9hfdcw5hHwtdzInsllgScSdaESeTO8boOkTU3V%2Fsu82I1nvsNus%2Bo77bQ%2BEiMbnJ&X-Amz-Signature=e7429a8252179f633442b569a000602cbd6d43c518b88883abffc839fe6de247&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4816b9e8-8c12-4913-b787-d8fd71461dc7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQIUDXSZ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKMmsU6Oo3q1%2Byf8800V7XYHl9pna3LqpMUUuQ0ZdhVAIhAMe9IgqhOgjQ3NryE65g8LFf8KzFovjrCXMS3VqlQttHKv8DCH0QABoMNjM3NDIzMTgzODA1Igzbdog4g%2BTs4YQMAFoq3AOjSZo5Q3bgyI40d%2FJaPohj2E%2BQwHdF2QMSz0bQog03yjSdfX%2FjNAx162yuPoXVrG6fCnj6LV%2FICf3SoX25wXCFc71W3X7bsRtc9NbRUioNR%2BaFlud2IzZ9wwprXlJG9WN9v%2B1yQxyIL8%2Be53%2BiJsgxz3j4%2BH9pgl2%2FQ5GNF6uG1ug1lDDyZKaXVSDiMtFONZWXXooH6uKJKs%2BWD3FsnZf24xCFanyhx8htpMTKtuxcnjD1BsEnJIN%2BAnANHdhBIxTUQbXorgEjPXyv1cSITeI%2FHYCRWnDrT5uQ2FkMn4%2FX%2BtTN%2B3tqPzSoN8xaqNWgwuijHO51XmpMuoIa8IUK9a9ib%2ButxBb7t9BE8VRogDRDmGWs009K08naL0UZjfEH2FyEsHZ65sqttOrRZdsB67xgnKVVnHSvLKLgk1Pl8vnNCfrZs60e0ZlEyTzJesJrScYUPEBLZqt4iVYa7eS3y4B%2FyhVa%2BMR%2BjXhjbGdV98dxNxRVEff6ZXRiSlEdOded0lp3k27Y0DdviEpp2s718l0sa%2FAcqPQTqsFTR2eOZ1LyM0n%2FPq%2BkdcVqSx5HY3kQoUJNsMPeaP7Qj0ywk67jaYdGcjxi9ApGrh6hTUV5KRayAIZq5zN1tfzjBDhxSDDH67zOBjqkAbGzqbh7ozO39%2FjLrECtWx4%2BsOiZHkGiPNiZpwrodMkwbzFgseA3rEPGD6p4%2FIQ4R7PO97nLtLhOphLgQAstcq5g4Oyqbgi8VN7QS0AeS%2BjHYZn8W8vWTI1kKkdpBwhXrSxpBYO8BbAfhnYTFAp30H%2BWuYmu9hfdcw5hHwtdzInsllgScSdaESeTO8boOkTU3V%2Fsu82I1nvsNus%2Bo77bQ%2BEiMbnJ&X-Amz-Signature=0b98e6dd97688c9b832f0665e783744393cc5031457b8d5355f9fc02a88dbbc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 示例

- 编码Man的结果为TWFu，详细原理如下：
- 特殊形式
---

> Reference











