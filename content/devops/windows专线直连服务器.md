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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U7G2KX5%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIGVMg3Y5Xd3X9qOTm2hKCAuhISMJw8QbT0mTakKTNpRcAiEA8QpBLDOHWT1%2Bwvj%2BVI3nZydujmnd6DR%2F1K6jwZLjUpMq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDNLjXw%2FboBR0%2BgZhbircA9FGB75yaYsdQ2BWnUxnOXsCX4unPjFCJHFoBBXO6n6CFydThMJZZA4bkIyTwgpe49t2pK3XqkW89y%2Fe8NK3yJPxEJ0Ukup2fP8LEFYHdSSk%2FR4sqtXcK3477KiisZH1AT6EB0YP04Z4zCx1zxu9nO6P2hPXsvBvS3qaq6b4cpZmXS7Xxq%2Bngkp8jpdIBM3Ac5I7IhiFCBERchdMAzDhAXcdCsTNz9NKcg2VYt6KwbhTBxs0VkrOVwayVihUjtuTPy%2FmJOFHXfdDMblU5SQyL%2FddqG4VunUkxWs6oh3%2BtbFWzNn5mYQIWdVGN93fA0zuWbDOHEnDzutppud2Gl2qEBBOVYw%2FqMlJEfEFL%2BYai8BVYzu7Y4D9MhsN1a8USaGHiR8vtryIMEyPxhFaVWNUrPUWwv3tM7UlK777yplfjk%2BCqSYLermrcGUhWQctlnQorXIAxiVAOjpi9kuB1t9vvAohy53P6m48z%2BQC17Y%2Bwv0H%2B%2B0ecoxQnNbjMHPoBplSVuzHvA5jLvuzrtZ8JvfCF%2FkXeFOxHq8p%2BC%2FULd56Mv3EKCcUoxMpM4YLip7pA3bPnLwbFzxYOEaP87BxFlJ15xkAN1S%2BFVZUhvcHjBqTbe%2FS0gr3uf7rkc0Ew%2F9pMJm%2Bos4GOqUBt86aSn0gYXAjzutv3maKNDs4Ud0JsbTAXeXEMdJOKGqxHXHuRlV3p5j235istcy5Q0K6cNWYl6KUas2MnB0pJK9Ys7%2ByoMNQTiGSox53Ch5BIMeE6xBeLT3gaeleALgO6kMaNlkDUGVE2rFtvwrixWA12IVjyghxiQWXqr0NZGnmtqFlK39TmlzzxtNy6hjK%2Fxs4%2Fvklus34XK15AsJwRgYB68zU&X-Amz-Signature=2c6c35b4e90a66d14eac5989eb9038327197e43c10a7b195a6884a5200235481&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

