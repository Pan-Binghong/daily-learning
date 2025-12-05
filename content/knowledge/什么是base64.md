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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5acec283-4306-4186-b12a-36c0dd599f63/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VEOCSZO%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOqIdycFJ9GOeV%2FBFuLFbwowpxGxKTqBl7B8QAT2esHQIgEJUKyj6C%2FKYkRBcvU5ZQl9rvXYKQxuLL7LpikF3x5FYq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDCayfwJvoK%2FJe4TnAyrcAzAJ8w1YgBOrRfBUG0fotJ2iRFXpuG3Ef0ZsKzOOsH%2B7FZDa3ioI6c3vVL7CyRZcxhGvJpLnT%2F07xwm1dYhv%2BRbAPIEYBU%2BICDsqvPCYoAvJJQ8LloyJQHzx72enZzDTGpArQbY34cUUOzz3y%2B1Zs6X7auuTqE5yvpDmqo0%2Fm8zorby%2BnJKZZV4au2qa14VNKGiSzM1yfW8Orvo3ijmqc%2FUHKU0AyrgRdt4MWE7wgAKsgRUq%2BZN%2BZDj2EyZz7%2BqWuvTpLgp%2Bn9logZoWLC3x36WQWacnkG%2BKMWaiIENJomnII3HfyDuLcfovPzWwyH%2BM0Vw6W8UX8j974dETXlYqJy7uPKqW8mZGkKNYPb5yprob9yGxcG1Rn97U%2F7YzYG62Go8LFwygRuFCgPqtAxT2zGTvtXZLA0JFBQnckkGI3v7MD5ln69XeiGV4IeCuV7%2F33HvVlP%2FwINJ%2FUHncwBd2MoNELDrSKMdllDqwJAlVgPEcngD%2FDBz7I1pcdKI1xG0lm%2FBsNDRNIW3eE7UVI7wzsyfAkgftrW5QETBW4MYGs8zGaSvW5ox5sgSsggpiFQckU%2BaFW2DmH10%2FESMP7cE4uEKNsEFI1rRF4C2toGYitiQuk0RWVNRsOABK0uodMLSMyMkGOqUBeUPujbNu3lWUuoiC%2BQ2WnJk%2FXU07RZLBHNGROu%2B6nuTifXBz3E01Jbl3fxHdUqxstKulk1ucHEJy31Z9km%2F5Z182YtRa0%2BfbZdbp%2Bca5AL89FP2v8iYYv%2FSzCzumOot%2FasflJ3jt4FMI7EGWPQYI4V5kcC9ryzrvwhOmw%2F7bkJ8il1pZXnCgU9pXHcw99IItnaKxxZ%2BAXcFNUW02xexEH%2Fr%2Bj1go&X-Amz-Signature=6ed03c5273f3cf76eae21f1ddb6366a257b3d8b43d97bf9aedf90fc5e0af80d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4816b9e8-8c12-4913-b787-d8fd71461dc7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VEOCSZO%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOqIdycFJ9GOeV%2FBFuLFbwowpxGxKTqBl7B8QAT2esHQIgEJUKyj6C%2FKYkRBcvU5ZQl9rvXYKQxuLL7LpikF3x5FYq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDCayfwJvoK%2FJe4TnAyrcAzAJ8w1YgBOrRfBUG0fotJ2iRFXpuG3Ef0ZsKzOOsH%2B7FZDa3ioI6c3vVL7CyRZcxhGvJpLnT%2F07xwm1dYhv%2BRbAPIEYBU%2BICDsqvPCYoAvJJQ8LloyJQHzx72enZzDTGpArQbY34cUUOzz3y%2B1Zs6X7auuTqE5yvpDmqo0%2Fm8zorby%2BnJKZZV4au2qa14VNKGiSzM1yfW8Orvo3ijmqc%2FUHKU0AyrgRdt4MWE7wgAKsgRUq%2BZN%2BZDj2EyZz7%2BqWuvTpLgp%2Bn9logZoWLC3x36WQWacnkG%2BKMWaiIENJomnII3HfyDuLcfovPzWwyH%2BM0Vw6W8UX8j974dETXlYqJy7uPKqW8mZGkKNYPb5yprob9yGxcG1Rn97U%2F7YzYG62Go8LFwygRuFCgPqtAxT2zGTvtXZLA0JFBQnckkGI3v7MD5ln69XeiGV4IeCuV7%2F33HvVlP%2FwINJ%2FUHncwBd2MoNELDrSKMdllDqwJAlVgPEcngD%2FDBz7I1pcdKI1xG0lm%2FBsNDRNIW3eE7UVI7wzsyfAkgftrW5QETBW4MYGs8zGaSvW5ox5sgSsggpiFQckU%2BaFW2DmH10%2FESMP7cE4uEKNsEFI1rRF4C2toGYitiQuk0RWVNRsOABK0uodMLSMyMkGOqUBeUPujbNu3lWUuoiC%2BQ2WnJk%2FXU07RZLBHNGROu%2B6nuTifXBz3E01Jbl3fxHdUqxstKulk1ucHEJy31Z9km%2F5Z182YtRa0%2BfbZdbp%2Bca5AL89FP2v8iYYv%2FSzCzumOot%2FasflJ3jt4FMI7EGWPQYI4V5kcC9ryzrvwhOmw%2F7bkJ8il1pZXnCgU9pXHcw99IItnaKxxZ%2BAXcFNUW02xexEH%2Fr%2Bj1go&X-Amz-Signature=813cd7a193389c1db0369fab53e8b041810aff87cc9eaa515b199b035d662c5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 示例

- 编码Man的结果为TWFu，详细原理如下：
- 特殊形式
---

> Reference











