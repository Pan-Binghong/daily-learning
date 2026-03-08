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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5acec283-4306-4186-b12a-36c0dd599f63/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466537KPKLP%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIHycAWCaIBcIzndZ89n5nU%2FpwCLcA93jysXpfqqfwOaiAiEAq0YLhx0hHCw58F%2Bt3%2FRCQiDddKggWE49kcudiBfyPzUq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDPnun%2BNCbRKv%2Bo%2BE0SrcAx7uVEPEk2ralB0NF88FS2aSL9FdpKfpvdqb50KJt0KIjAPJCqwXSrMl4XjKmrp%2BOtvDwdVhWwfqroBHhymDYiWmqpbmR7yimVTrnyF%2Bm87aw3OYdBZAukNWJ6C5Wu6FWzCBicQgO8fR8o38hO4BYm1jeBYxn%2Bqxi4WBn3hWg1ucnf9EHS5MwTpuJuzeUuckfJcIipFXeGiQzStGRSjBvHpnm%2F3NmMsvS%2BRdDYY9SmRAtDyUirhBwc6i2DPQl1XYmYTbY3DlO8IGY6YzL8WBAD3as7S%2BJZ9quVw86dhlYLi48RDuKbBCzA%2FjpxgX%2FbSrp%2FrrU44vIctoFZd20fr0tOkCW2fwFlqmQPlSRB7Ywmg4U8HeY9wTfUmuUR478iE9AmAStjnccRMqC0sql77IZphTzf2oEJLED2SLnIPnWQh01EiXhUuVsC3g%2FXjbuG4%2F3a5ZJOGS%2B24zRC8AB7AaC7EWbOu%2FeiWox41En%2F24nvYMjlGfkf41YM5hQnuphQm%2BUUha%2Fx8KyqHS7edZdhEdEQSBoM3aBTBp5K%2BCiOHwVfO2tFTuphADx%2FcP%2FHjkjK2Q%2BhT9IA8cRNRlCkhflcLtW8knuvJgd50c%2Bq4yzQIK%2BpVALzWAb9Bw6CIuNHRvMOXCs80GOqUBU24UlWLCG8JXgMl%2FYH7%2BGnn5BgDSFoZWkbvab7QvRZi1aZlRYaml9hV0ZKKMoQLz7TxfLhrWH2GKUwgn36JMUAaaQMWyQaFv%2F1G8b95a%2FagINd28vFVxwbNcUn9yxYqH%2F4WEEAyfgMw0wQBJjJEmme6VHxq6IDqxdO7ctD1T0mec7xO39D1HRmq6IINbMesZGbLaM9ixUxWMEatrWzzqN%2F5TTdcB&X-Amz-Signature=e89958c646fe0680f2ab75705b806521267b0707359806384093457dc0a4f9bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4816b9e8-8c12-4913-b787-d8fd71461dc7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466537KPKLP%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIHycAWCaIBcIzndZ89n5nU%2FpwCLcA93jysXpfqqfwOaiAiEAq0YLhx0hHCw58F%2Bt3%2FRCQiDddKggWE49kcudiBfyPzUq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDPnun%2BNCbRKv%2Bo%2BE0SrcAx7uVEPEk2ralB0NF88FS2aSL9FdpKfpvdqb50KJt0KIjAPJCqwXSrMl4XjKmrp%2BOtvDwdVhWwfqroBHhymDYiWmqpbmR7yimVTrnyF%2Bm87aw3OYdBZAukNWJ6C5Wu6FWzCBicQgO8fR8o38hO4BYm1jeBYxn%2Bqxi4WBn3hWg1ucnf9EHS5MwTpuJuzeUuckfJcIipFXeGiQzStGRSjBvHpnm%2F3NmMsvS%2BRdDYY9SmRAtDyUirhBwc6i2DPQl1XYmYTbY3DlO8IGY6YzL8WBAD3as7S%2BJZ9quVw86dhlYLi48RDuKbBCzA%2FjpxgX%2FbSrp%2FrrU44vIctoFZd20fr0tOkCW2fwFlqmQPlSRB7Ywmg4U8HeY9wTfUmuUR478iE9AmAStjnccRMqC0sql77IZphTzf2oEJLED2SLnIPnWQh01EiXhUuVsC3g%2FXjbuG4%2F3a5ZJOGS%2B24zRC8AB7AaC7EWbOu%2FeiWox41En%2F24nvYMjlGfkf41YM5hQnuphQm%2BUUha%2Fx8KyqHS7edZdhEdEQSBoM3aBTBp5K%2BCiOHwVfO2tFTuphADx%2FcP%2FHjkjK2Q%2BhT9IA8cRNRlCkhflcLtW8knuvJgd50c%2Bq4yzQIK%2BpVALzWAb9Bw6CIuNHRvMOXCs80GOqUBU24UlWLCG8JXgMl%2FYH7%2BGnn5BgDSFoZWkbvab7QvRZi1aZlRYaml9hV0ZKKMoQLz7TxfLhrWH2GKUwgn36JMUAaaQMWyQaFv%2F1G8b95a%2FagINd28vFVxwbNcUn9yxYqH%2F4WEEAyfgMw0wQBJjJEmme6VHxq6IDqxdO7ctD1T0mec7xO39D1HRmq6IINbMesZGbLaM9ixUxWMEatrWzzqN%2F5TTdcB&X-Amz-Signature=598e0d5ec0c53709bd80818033788d29b4a3197356f9a7b5b59b64b271619198&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 示例

- 编码Man的结果为TWFu，详细原理如下：
- 特殊形式
---

> Reference











