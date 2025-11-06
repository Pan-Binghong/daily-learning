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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWUDBWTM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaG0SBe7oyv5M73B66pZj3jzG05UwA9wvqDbYOcsj3MgIhALLaQRZBNx4VqcTmVG6h15erAYjdVE6dvAs%2BAKJAT51xKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpDHlEtIWwEBbnu74q3AP70fxh4TtHmpr%2FbajYZgW8Qvw7BQdhwNFX6PaWAUKgX7IuNXoGxKFeDcu9mZm2xHdQA0XS%2F5gIxk1WhOsdOtbEyAhDXcmCSQqwvB%2FjV8QFVYyaQy%2F%2BQyt21MoXUsEFz7z%2Fsj3h%2Bs%2BafTuG5%2FPsjjr0Tk4uiNCCm85Vr6ZS3Kd%2F3dKK31SCbgZIBlyF5LYKMfwc5o7XtilK8oU7SD3HBMVp%2BjE%2FXWxb4d%2FV2OaDOb7cvWLQQw4YIvyBvCJboDNyC1Twj6maZ%2FndcmReYWdQ9nAd%2B5qXmVy8AldmaD336wTmf%2FOZ1i8NM7OpRDac12RaDA9U4vHbSanI7vIxklDoFiUMQGYUKEMknqp47Lx2Lx1T581e%2FWyUqY9rtxZ9eUJxpNwKaMw2QzdjTCYIhq9pIkU06QoNyFnAlXH090tDsp%2BGb841jjZlH9ckb8%2Fh%2FfTK%2F1j8CaVaNhpwwwc%2Ff1ABO0w6HfWq7Zhje5wrexECxkmousKU6ua7oP8XXlt8rJAAGhpf8cIIJ87mlTcmZBQSd2Af130y7CVG71%2FmsptlPhwp0%2BuhsAQc0beJG3P4uG1Al%2FzPBhxEsr5KaMuxrVtdqeQPpttE4eY4jy5aNYc4NoLXkIXZTXhjGw76L5%2BcRjCGlrDIBjqkAcsUrKdFyR2UiLHmVQ4IMdREaJMG%2FDUVcTP0VBnTxorx8LanGiM1VEh46%2F458moFjwnIQVuV6idDXzqwhpnJIAYYUPSvhQXL8wwOMm8TqzTXAcwbYi4sVTFbXrxeVwHxD5%2F8lQmnEEiHuu0iC86KzUhiAJHcAf4f5Hj3%2Fb05K2q6lUQxUgyRHlMbhP63I21GnZreQtubmWsa%2BkINqDjsQvT2AIsH&X-Amz-Signature=b10469bf16b87c6eb4a416fc3a6e941978c42832e631c198efa394ac47f3886d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

