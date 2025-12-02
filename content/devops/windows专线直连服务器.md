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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN2D3Q5W%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIEyROe0HM3RxZf63UJXqEeI8Lr7fVaueFdw798ytdWF3AiB6AidSOfV4DWm6Lhxnj4YgJZADedFo%2BNiJ3BbHTUY1tSr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM6pN5fodogxsneOTkKtwDevPuqnhWCjo%2FnBkBk1DncjC5NbMEYjrDRKG5f1uh%2F%2BCAgeIG0V23KSn8jZIvNmbnHJuK7duaiuqJs7nSq8Egojl%2Fz8gfJc2YFjh%2BCyFT8x%2FGeuxwNebXiAEbES5YW%2FeWnNf4bC6A8SjNo0BD%2Fr5ZnSyIxyNjccU1wrtYH7300s6UO9TWse2F3xB0rc6E4aqP9SRKY6%2BNb0V4zRtT1VkW4HYpUci8m5ITTv3rIXmKSpRp4BMQNmeGZpOvU1bVAH1PgD15um86B8WD079AmRBPQcJHy6JRazRkZT7GCBm61VSGn8Fiz%2F90LR1re6MyDDhmSdo190UbEBVHpWH6vJCSqdocHanLS%2FQS1gBal4MoukCH%2FZhhEGLWl%2FxKd9kv%2Flhp9DlS9owPBAB4ZjMsZ45P5GPnnjp3RCEjn7fp1PSDPPUV9bws38LHsO0tKiTyh7vkabXBEj4HgyzfUOgLADmH6eZb9qt%2FOLz3X6cZfDoMyOV9C3gUswaTYl66Lpy0ESlfjz4DNVyGpoW49yt%2B9ibPeoZre7PbCRmwNmwWGBe5I2PZUYEfyZoPsqrKovb1OBuGxD1u%2BYkRrV1w3v6P92ykezdJs1nRRxxEpiuwuqsyAi1Nj4eK8DCI8WXEY8Yw9N24yQY6pgFQ%2BzzF9oux96ENZc3mwiwXhc5B6tOqeLlWgAADNY2H9R6KVoTtIUIOLULjSks3wUk%2BVVrQ58v7PYyf4aPfQkAnUbshY9b%2BKVZIYG%2BX70W1CaD%2FYJOpjMkAk1D2ZFqfiolnE1pNnL1FE%2BwMXWbNSNYuSj6L%2BfW9P06J3mCMFsyq5gQx%2F9fzDdAwBoULt9XWf35QJsiBgVBtYY0k%2Buv2DntQHrKw1jM%2F&X-Amz-Signature=f695059821004214137e080ed01d2b636ac433b75278e9c9d5b61bdb6798d188&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

