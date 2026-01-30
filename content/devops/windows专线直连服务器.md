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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HW47SAU%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeRDlngpbGJnLZ1LpA3yRWS8UJ284%2Bk5XHxIQljmYwXAiB6zgPqvzZs8nXxVRJNC0neWac8KYanCMk0oOCcrdwlyCqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3t7mfACAdMUww3rYKtwDJXPx8vyUM%2B04IHJd58BsnMh8o2ACYnDhph1lC1jF4t%2Fk%2BgQh1sI1kTer%2F7KToWlETdwbtiWch9p%2Bgst%2BuKJXHDjCfxXhSgHlvUSq2AhwmfbFgoulEVA%2Bg%2BmdcvEXNUoVlarPyq6DWk8HbmszdiuhGMfdlrQ1flMSEEBub5yaVYdeja3wxRBt%2FlnPcnNMSxD7n2Civ%2Ft5khI8yGmSueq1xZPkubcLN4t4Se6qd1BikLwnyyGajCGkm9t134GnQ3lIs5MmAly6VbwRWwabPBaNcGNuAiT9%2BjXXcJlK5uUkrldQXjoZ6PqXs3NrGFq8T5pVJSGg%2FSdRa7fkDKCjyy59JEFyxD%2B4hIp4mY0HconENl0K5JFApPILkkOcCCTAcioRtiPwyGrSG9MgG9uDsbYwCoB54bA7qm9CuT24QF2Z7G7nsCUiCkHO6tLB%2BWHASt88SvRqzAr38mg8Nn%2BbXwiyEvz1%2B1V%2BeSvDgvnbTngNmSNJHZohZBKsyk54fpxS%2BdkQmYaCQw%2FGIGEfFtlgRYBRNolD1uUatTiWMS0rapN9JaXvzq9CudfAfNSyvCFG4%2BAgVq%2F6oD70pVBzPiuVPlQ45i6m8E406N4sW1AlFZorql%2F5dN9EfIhgbUDeDLUw08jwywY6pgENuC%2BWEHz50aXWvsUYyjpvI8XE3MH%2F3eI%2FxtM1fjkH7HHTo6I4lGSRWjHtohm9gR1s%2FS85%2BtkImtj8rdMtL2eRcRC76oyXgQWlfCTHclHGmE5nwtUQHP706dxCAH5lqz1u3YMpeyOLvoE2DNvss4ais61t3s%2FbjmwkpxbdX9A8nmXz%2FY0j6OF6S3PQHOlvlOp0LKwnyAOtyaAdfoBCcKopmXfj%2FPiV&X-Amz-Signature=e1bb5357ed5521abffdef2fe7f1f9940a48f28a74523a3b30425e8ceabb254e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

