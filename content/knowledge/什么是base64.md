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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5acec283-4306-4186-b12a-36c0dd599f63/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RU4CT3B%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDPuNvEuvHpg2B01ZpAn2oObe8ZyRifzNCAd1P2pwjGNwIhAOmN3teH0A81hITLTOwTPc7LTK%2FVk3XJs2REUiWVM3kcKv8DCDQQABoMNjM3NDIzMTgzODA1Igy5iGtBYfrbfC4c3a0q3AMwtSRAzWePIOG2SbaHJDCIqRxCYmtiOMhsPQ9tatDSjOuXshDHNabuRtgX8t6FsIGDEuvSYIUMzo92lEayuLwiwFtONhl9ARajBLcT%2B%2BnekrEFFZyexosYEpS%2BfvI809iZIoLPET3sQNPdLOvluQJ1fUPFXDxL4AyRjh0UP%2F9RF4myBR%2FR5oCH8R5X%2Bx1D%2F3iVgOUseJYc61SCJzjRjdTldtpkuiHKtzguq7KI7QO%2BOAr2vCRxGakh7iyaR%2FkqCVlIMupsGuhi0wdnA3Sq2Cne79998Zvv0WTioIB2sJ1EGRN6OsBKvbp0P6XvmxB8MUBVtXFcc1reXhl3k%2BofF3CmSAfKggOIh5jiy%2Bx4CktEA%2Bct%2BBhWv2ga5A%2F03h6s%2BHfYc2RKS6Q6XEuTflTGj7KkkXem3ejjvgOejudUu0aqYmUo%2BH%2FA0ErgYdJbxCDoJ2mtYLPqty39sTZpWcpRzXAs%2F%2BiptTuJ1n0jZmce40Fu7tB5JDlsWFQ7XbzWATpgqb0o6YnM9SZGu4E8ab9rOoBk8%2B9DM9yf2oqe20kz6DbZfpq8l%2B66DBVl7nDjoYzOJVpvSDn33svyzG3FtqEHplsdyij1DgrKMHqPcaBlPDnzwuDPKyBfuXDl8yL2STDehoTNBjqkAdPDo9qHVtD%2BypyeODihApY9wJ%2FNxvIjkWJzJvNPqHh3NATpqR6iztsPcTPakRua30rZvVVh7lHHYFrIUaPew3omo212DgBgsNTT1jhEzapymcFkGpefEkWppgJmd4cnw3L0E7saBlSGiDGK%2FHGEOU2hgzG7TAlQpeLldQ5hPIO5MgEFEMPv88ndkRTeNpgw8i2fGOk9XRpeJaeKo7YyIZQtm8C%2B&X-Amz-Signature=a6f3ea70668f3313c78d22fcad217a7a3801d0c8fe1aa6fded8acf4598e9538b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4816b9e8-8c12-4913-b787-d8fd71461dc7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RU4CT3B%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDPuNvEuvHpg2B01ZpAn2oObe8ZyRifzNCAd1P2pwjGNwIhAOmN3teH0A81hITLTOwTPc7LTK%2FVk3XJs2REUiWVM3kcKv8DCDQQABoMNjM3NDIzMTgzODA1Igy5iGtBYfrbfC4c3a0q3AMwtSRAzWePIOG2SbaHJDCIqRxCYmtiOMhsPQ9tatDSjOuXshDHNabuRtgX8t6FsIGDEuvSYIUMzo92lEayuLwiwFtONhl9ARajBLcT%2B%2BnekrEFFZyexosYEpS%2BfvI809iZIoLPET3sQNPdLOvluQJ1fUPFXDxL4AyRjh0UP%2F9RF4myBR%2FR5oCH8R5X%2Bx1D%2F3iVgOUseJYc61SCJzjRjdTldtpkuiHKtzguq7KI7QO%2BOAr2vCRxGakh7iyaR%2FkqCVlIMupsGuhi0wdnA3Sq2Cne79998Zvv0WTioIB2sJ1EGRN6OsBKvbp0P6XvmxB8MUBVtXFcc1reXhl3k%2BofF3CmSAfKggOIh5jiy%2Bx4CktEA%2Bct%2BBhWv2ga5A%2F03h6s%2BHfYc2RKS6Q6XEuTflTGj7KkkXem3ejjvgOejudUu0aqYmUo%2BH%2FA0ErgYdJbxCDoJ2mtYLPqty39sTZpWcpRzXAs%2F%2BiptTuJ1n0jZmce40Fu7tB5JDlsWFQ7XbzWATpgqb0o6YnM9SZGu4E8ab9rOoBk8%2B9DM9yf2oqe20kz6DbZfpq8l%2B66DBVl7nDjoYzOJVpvSDn33svyzG3FtqEHplsdyij1DgrKMHqPcaBlPDnzwuDPKyBfuXDl8yL2STDehoTNBjqkAdPDo9qHVtD%2BypyeODihApY9wJ%2FNxvIjkWJzJvNPqHh3NATpqR6iztsPcTPakRua30rZvVVh7lHHYFrIUaPew3omo212DgBgsNTT1jhEzapymcFkGpefEkWppgJmd4cnw3L0E7saBlSGiDGK%2FHGEOU2hgzG7TAlQpeLldQ5hPIO5MgEFEMPv88ndkRTeNpgw8i2fGOk9XRpeJaeKo7YyIZQtm8C%2B&X-Amz-Signature=9c6fcc2cb509260c514dd8a5eb311551f2688cbeaeeca379eb338470d1969545&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 示例

- 编码Man的结果为TWFu，详细原理如下：
- 特殊形式
---

> Reference











