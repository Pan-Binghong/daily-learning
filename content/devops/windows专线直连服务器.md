---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDH2EHM2%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICEs7q4zkAbo6ZMA2s9EyNMHlJBYOA2Yij7wmdhur%2Bx1AiEAm713oFEkIEtfXkI25HF6vwbJxh06W4iWCTrPJWK35ZUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhBK5xlnc2GeyVgPircA1ZSCUiUAj%2Bq4NabKZkTUiD85Pml7fV8QeM6h%2FY4qPcJPKW1KMPJ4OEhsJw3PYRvY0p7yBsmiIM0YDROeIkbcDPWPZCWS%2FIrs6gCUnu8S2%2BmsVuK44hWCktyzRx9%2FoUk5copmyYOtk27GeWp%2Bx3GXe2MyVbUz8aD7u5vzWSa%2FHX4nUdbSy7kAKDzQXuFHDb%2FuZkvFz4F6aqtpgiYYbre4VtVnnVpEmEXzryfVkzISHkIhbAg5x%2BGivLV741YPeWsk%2F9Zm3u2iR2rdMF8RTpVu9AzsngP0%2B8%2F9LovglFQCQxvrtEtltshwSD3aU7VhdIdXxLfXQ7Yilq8MR%2BJDH%2By%2FTETTSKiGGDZ8%2FzU9X2p9ZF%2FnEGoFeDC4bOP%2Bgm4EtCQljHOLAb5mpzh38kSBCDBG2J4D79WUidi%2FTICsVwFpJSne1RWdVxa7sQDTvxQ%2B6cyWwp%2FsNRcOZSOyR1ehdcE72aen6SNGM0eijMAvl%2BuHRwNJn0z54J1JIUc%2F4shBK3OxEBkjzEaJuImPXk9zHFcqOHwcbP3e4oR1DmUI%2FXT7USoKcnoU%2Fn3JPujQ0pmmf3JWXCd%2FJSDirodUlA4KBo3gNILnV5CqV1JfdK7rEnCaRyWO%2B6SiJ2SNEGGyjR9MLfzsM8GOqUB1tQkc9jG3NK2jWNAxtrLMLfGZ29A8tG38zWg1QhT5J9HEZ97B198%2F6mxOyMTt7neeFOaEzo5FELYJ016D5iCsDe1zmvRcYM3d9l5HzKOlDnjB%2BQ1dHOFjJMfCtVIaeF6sHGqsOO2ojKcuo4ea4XTluup8XunEmaP8imoyXeMMmF%2ByN8uVapQ8rVz%2BsFEzioWl23uO6LNBH6HjKysM4CufMaUs9Rg&X-Amz-Signature=de668d6e101ca8b54e96b59919f853a784925580e2716dbda292cd125734dcc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

