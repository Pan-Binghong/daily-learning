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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z43TMRM%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICCGz2tts%2B6fBNENpLXTCVRsf5KOMlDlbqSJPZWRrLvwAiBa4LbT%2FHIo9Tp%2F1WdKlDmlvKNPRr0UQeKY6txiXawNjCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM16YPG%2BRn%2FUqpWBISKtwDXKyVR30cGhX%2F81P0CQsTF8pVBfjB7RM7SP3%2FLfW8wsG56RDv5gUnBvuHwAR5R12Yo5fxY%2BmUMBNUDRsSH6Mh3aJxNYnnatYPMiDNghxizkZ6OAxXlA%2FNUdBFiz%2BSRRDoMSRgGg0eAMSkftC%2F8yimRaRuh7CkKIUIGDfngk36sQhTD8ApeiqpQROo%2B5GGzhv%2FBhHr1qJGyX0kVzNKIrpEs%2BXMfG2EkxZWxnZIeg1LBqUzI8V8PVmmo3EOLLriMkrw9cPF3qGIfe%2FM2IF55TwgqJfBCmwwhnzCa%2F5VBzAtoLBvmjT0aLwGuarGRQFT0PT6z7IEi88%2FgFYqkqJBgrmZaJoFaHWCSX6DN%2BkH2Rcnis0kD7iPGKSiGBZWIi126FT3urL%2FvWqgUkWFdLJ0R79jiJwxi7TVM9BA8MBXFwei%2BskbwMfxbOloNOAf1biLc%2F%2F5oxrEDdHnC%2Fjglm6f%2Bl%2BIyEKETMY7%2BCK4yJPmDCRdUbLz1eUkjCBm4nDo2mju19V9GjB58Y4gydvA06POyqGaTWfjZeW4A1hIQCfSFKojwzLAKErt30akf8pKjXaDAiZMqe9BM%2BBDuZFlLwggdUeSyagHj4v%2ByDVdKUDZQcY1Tu4kPYXekWBh0r8wkT8wg8yvzAY6pgETnVU4f4FOJt%2By%2FWWRPHBBJbjK96wpaAWDOSWZi%2BXNoDQ0KLc%2F0iOb2XgPtruTipypI%2BR%2BkL4qCij6Q14mzof7IrZv%2F1NtNHIrjUz7JTfxZYsLT7TWlw%2BFgdZR9iMWurT7tJHGbvn76gauoLxmEy1y3RtYqurYWVZPffuQgPKZsiiI7xBK44YNeE%2FrGMN9DRbn7kl59vVLF1O9E4F7WlCgyPltytJ4&X-Amz-Signature=760fa359976546def909fcf42788945ec141625da8e2a628b4729ff2f3d81727&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

