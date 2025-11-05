---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
标签:
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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SSCRY5S%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA5WOsineBvdj20QrcSPWqf8ZZcXt9POm%2Bnw1M%2FxJKpnAiA%2BD%2FReKTmNa4wi0am0KSr6mEV3eFN9y2psAUHglr8fuCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUiLa4ZT2V5XA7HY1KtwDpBjm4N9gRqcL%2BM4bUl4b%2Bu2HpEa1WY2iSD7gv3neDkOQjSQYLYFuVwTbi%2Bbigt7lNFH3aqrEpm9iwQWeHKn7t1z%2BnVvUAjvr5P7vb3kWotJT6oXpdZaAIpJ8uOiu%2BFnLkAp%2BQ%2ByLBIsR4X2LYZriMi0HY3mQzUyJsmc7BbTxH0RhPZyaUCbRGH28TIW%2FqOVBjZIg1kCP7ohrvXjGV3%2BDV3jjdRKUAxSr86E0jhl1FKcuCr%2B%2BEL8%2F0c43T2wYUq%2BnHLM6ZBfORtCcPQ37UQHZiFV9s7TxFHwNhNVTqaCHVi3OUx4Egnlo6NH1alq9ggZlksaTJuu0sUh1oYJzAwkH6ji%2BRsKIHOP9%2BDDYdHcARvKuCOBTq3SvzjgKNHfTPsSGDFzEhD5RkxZg07BZdHvHi5QtVEf9kfgVzOINzldfmX5d0ijxyfys0xiOKhIjewpPICX5xFDKLm0xUByHyG%2B4n0F%2F6EAcvHLoKicAS9JaSFOwfZa9bp%2BpZz7KQIqo%2BVnN5y1nfOHyCWRlhrT2Qa5EyFqFKYpIAeqc752ZjxJ85k8rhITRgT9xN3FNODHRhFj1B95k9XViaVU8RAwvJ3VWsXjqeRmirm3ERmboNlYPhucw7ZX0WtFgm%2FaOTz0wuqOsyAY6pgEKubQCaM3%2BMUgSjS3Q6Cx4myZA4nGX4cfw%2F7L6wFc58qCGcTgBlI6hlK6sQYPKv8dV%2FNix5Rj7VDc%2FZM5NicU7nkJImYivOctQ%2FP5FHRwSiLfBnTta9sVkk4w9gZYXU%2FQxHEVy3aFyjHJVNeZV%2FU9Mf3aLJ1XgJmrVQvDdv8mi9XatZSnHv%2F43OBNMaCpnhyGxCVR%2Bx%2FN8rB7Z5kTWqmqu2IgJRC%2Fq&X-Amz-Signature=3557cc6d82f32deda4f5d3e1bc9c3e0d4f729ef41deb289beaa6ea2bcee93c5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

