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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C2O4Q37%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCzBGQD7mpUsXIMYRdN9DonCeBVLE5kTNn65f0NpxOhEwIgC%2FYby2eMwO%2BrnPUe9CY3PjeQQA8cwNxhqoBOO3neHj4qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG74Of4EJb5AeN6wsSrcAy4ICmWZIBhpYMzIyZIbGSXSJtPBIQGXIRkO0bMlhXHDCeFlSUYXa7nSIbaliysbYhyVAPYwO%2Fgd0swn1%2FpZ20uAz9WB1ywNOxy42CV4hTlcU4Kh99Ok3ZUr5LhgPhmow0WaSoXpbC7I5KsLlKF4h4VmFHQpaRZf1E23NtxNSq3bTsUHYLI29M3gilQc0PWJKli7pK5E17beDabkxR310iFPhVmkZHp%2B8Rec%2BFf76nxkBqRlW%2Bq2eXEZxTiIU6RqfniEDGeppTxk9Liw6A3UxtrpwnPgcTT6%2FgeD0Pw1sV1G9sSVrxg1NZv5Z89TD31aV7YrMFTSR%2F2LydryrJNT4%2BGB7LD0G1ZM7zvYYKUH69QQi9yeAXC0nQXYe4MiVPoVa2207yAnv3w84UPePJtMYiGz8pHbz0QLEoLXswAqfZ1mmYwC5qLjKEEkdu0caEqoCbWJECLsdAjtjYY1ZqCXzWKKnHrMHp2XSGu5rZxgtTp5pdAHrzFYQaPu4GoSAbydQ8werpMNJ9xqpWvW8FyLaXKZFn7zXlMZz7gRCmezWT9wDwIxiVYL4QmKm0c6TbQa793pa%2B9wK%2BSC6l6o7i3LvUjZ0IYYHZCEVqezEKruAWaUXAr%2F1SsnsYkhnfgsMPisi88GOqUBNG97xxvZ5OA%2Fl2fgg9E0FvLe%2F3iXy5FZ2bm43u0rFv1e1R5VnAGMCqKoqvHgsLhkcvqyKtr%2FynJPvvABNPsF6llrGLYiGBmUkMQn1wc89MZ1yyk6a1RKkqjFCpGSAU7q4uvMKSqFWVXqVdOGhAEGrDxtK5VnpWibL5LouxAkD5fL0vYxtLv2AEHg8x5Ke8tPhUa37cY9V%2F02vLcNi9g0dvEd0y8T&X-Amz-Signature=50162f99a6bde8757d857e334f79f46a3c33e68fd253e7ae5adbd1aadfa06092&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

