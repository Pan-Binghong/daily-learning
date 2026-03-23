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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XVYFEY4%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDz758Iz7bTXsiXkgYxVuvcpI7RGDp2qAIfzUc998azfwIgMcuDS9uCedsRv22LlBc86KJiE9WgDgaQU0cSt1I4M90q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDNG31B8DH9NMZgdrkCrcA21s9%2FXQXvwwRIEwbFyOgTbnPPLvYjMnEyfymMR7LJTRFH05WELFjgBQ%2B0VxevlAThg40FKW4U7heS2J36ppIq9P%2Fi4KXQVZ%2F0hshIDB3%2BlLy1xFma8QVN2W7wGgl8DO7mwkSZWgbhcp2MQ%2BQTZR0DV7QYOXgmyjWgqJnyMaOHTnTcvXgBi8hSuJx4t2EmeEQmZYhzjLQC76mKrBHSKYpJjFYiMnRoLEE7F3OZOcJALQ%2Brhgc2W%2BZszXDcmLYwqfBBcEpruommHcuHSNXmnjurf3TFNQzqKAWDUtgPyl5JGq6NJrsbqjgWc5NV0Sfbuudb87unQ3UiOPmvHcW8t9rZSpExBQsGaTcI25Pb2Rh%2FOAVvy5W%2B65TzTi%2BYuXiUgIundIikz7REApmv8ThlRcwXncUI9xbwNh9SXM5BAlCFpNAsaeWxQcTUCfFl%2FUXHQ0LpGwOCcjrUx9h6reAHLswYjh1087hHpNrrxOm9xcoCzZPr9A%2FS824lEOvqApl96fModpxMtG0S2JwwJzfDlURulkxfW8uB5%2BMvVs0bu5M6FVNkJ2NReZkpbpBqRQY9bAdSthqiwmx%2ByIqFPTz5gl%2BLsns2oAQ2bx1rB4l4Zc%2By5FmUkryvQ%2BpBrrkFPDMJ%2Fkgs4GOqUBc2ov1n60mVCfIu2EPpsVnH534dsi7bQbvYfFMb3JM8Xxssef38k%2FXCqjFDfm%2Fv8hr451yz%2F1g74bZI9%2BNB3k0U2vRdIdvymg5D2FoQdZ7yestXNCda%2Fih6thzPToY2HU6V0e%2BC8BgvCp%2BBr8CjlVRbxi2GDuywltReZ3Ur1%2FKsilcHOMR7p%2FEjDRNQtIrTbC7irRe%2FJSw9KIRPNOw6BcfENZ%2B5rG&X-Amz-Signature=441bbdd6062e54141b02c8c97a04ff59728330f1105b57549a70e1c5a5a65193&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

