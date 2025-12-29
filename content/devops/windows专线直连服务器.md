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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZ6UZL6Q%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYnWLHUlhAYaq5MMyMEVaa3Ty97QPwa6mUAw7n0FFurwIgDgI6lgUGg%2BCE2orriXHo2GeFoKvzj8c%2FUk2pkyLAip8qiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbO5Zis06JzuoyCPyrcAy5yzbL3XYWSe8p79xhIVFsWnDUsep5ZV%2FZ31Y1Wvd26X%2FVRhQlEut%2BJjzmcXogPe5VaR8dosOTfxFa%2FYwfHnVxFh1MKupe2ntvXaSclBHXWsVragtWyGHwK6kOt%2FpTh15M4UD8lz54DZykJnmSXYRKgkGPa4YAlLyJPKcISnviyHutegeC%2BJYyS1Dpdkj1eTtaxEtWbgPKZyyBZxjstXYJiTEFZomsBY3B3%2BV9zfz%2FbwyoWwF3prug3%2BfjtFbFreupESVdQgY%2Fe8MnAtTxT1d1fPq6j2CE5fmOXKqZWK4yjBddaT1XLxc3zzGUAnxnjtr8%2BW2adui9UdLLodg6r3VWfFUEWbn7ERusH0xwJcmdh9TLmF4wqgQz26UM3XIMQgDCzM4lGPfU0BOG1vSTwLLn0gQOR8h7ySJq2nP0tq%2FWGFm9A7%2B0BiB3BO6BkidmqAe22IoSzhSwlDH6mv%2Fl8OmVhjjcXv5lYYlEZHnhbRB37MpJTBL8i27DsbQBPWn2oZ8tpAGiQqJvyoxb1hQjQgrujCEuuKDoiL9fhBCHeOHpu3IjWQeVppaqUy92Xqgl4%2FKhVtXmrK6A3UzuMbhg%2FA3EF4dPanOyW7xGpGG3GnqGv4N3tKU5bkG5l3%2BOPMOSex8oGOqUBlHvwNZ7exaH7YwWsazKn5Rse5M1EeEGzETBxGjwHuMf6m1VnI%2BHwHL%2B7Y2AJcHaccnZHJyOYftF%2FSHgOmnz5lA4DH76pvH5jEW9aZUrKDPRFNqBlJzJtLbcmfz15LM3MYa0gdEw6vm2d1jZ2e%2Bj6tAtlqIk5k0p5%2BBsKh89hOrwLr7I166LxSfyPPQMKGTzftKDuqRVVJoXzCZu7CaOUISAKMr0H&X-Amz-Signature=e5239b751368105b889e303a01283c7c6abbbbd589f812d1daf91065cdd71b6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

