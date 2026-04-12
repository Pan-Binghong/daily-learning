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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZUA46X%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFUlOi92FlkLI83rq%2F7FPgB8t1eOhY2Y3EUfcbwJVJ8yAiEA166DdxOrpHO9RL9gFtLjKAbMp8KwmPRrum7nCE%2F%2B6jgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDC2EoADiZhIGgGKXZSrcA77N8g3Gyi5NpCeGucM1hw7h3B%2BGTEQWriHSezmJyPII0dY2XxnwcvI5A98nblFg6%2B0W5hc2GvCULohLohjNKs%2BLTOOAKTiDwjeWSDuwlhc4YtY3B5N6DY17S7%2Fvwm3%2BKIe8JOYWS2d5v6TKF%2BPjIVV%2BBe%2BHChIB91JZTWEhwzAB009Z%2FqF%2FVzn7MQrCUxSPs0U7PQ%2F%2FkV8vcqvEU%2FsB9YlGNly99y3ZqQhwuTlYyT1Vl0Ulblevh2APfyHuomwa9RrFRiGhOVW8fDneBOHdOZr0R8Y6ApFcCgheBD7fw5vqtQMUlMbFQRCmPDWfx88UnmMNqC%2BbvqpFMimu6O48G0oGxaEd7IzrUkGQ4RwSdhuHlVOHqg3pqenAgv8moVWi8%2FPaCXrW02DYWQlBSHFIKzgRm7v2zHDyzFQGSXQkMTUjbuiI%2FcrJwjsgY38CVfxWtWnhJYqZAxDt28EMvxEmpATeHXUqJFh5tlhqYGpkrQ0S%2FZVPBEVSW5%2FxF6%2BIO52lvH32Pv9MKz74pvDa3Yyx8XCNI6ulFYe%2Flsw1HmitBPdC93PwRFKW6M4gQiZk65sehNxJK1T0gYyZAjPAnvmNcgVxCOxeF9OWzyjEldQUGfh1%2FILF%2B8nik33qPdbPMOOG7M4GOqUBdS4FP0lwk3iiT1rmlz2OJsQsWboMtjxW3L1Se%2F1wc3zi7%2FpT35PiraLz0DlkdC%2B5Bxo%2BXxV1g%2Blbl3XuKt%2Fds1b0fQH3ab8I3Msvb%2B38NJk%2F0rRgEFcaoW9W%2F5t8r6nXC3UIYzqVxiYlHwlYco1VieCO6EemGgoB1jYullhZiKj7mJr9lMo9qw6GEc5N14c5BE7qbxl1lt6t1mi27%2FWhChmlA8%2F7&X-Amz-Signature=3e027bd667bf23da0113ad9dab5e28deaa4f7e8f570378715330584277e15969&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

