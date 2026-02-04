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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXQBPJSM%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCICrBJOcTZmJWqVgRlrkdLmQFqwFmeR2PH2es50rJPSuyAiB%2FLDo1qf1e2e9hUQuvNBKGfVo4O85Zj0L5UE6%2Bo3gcWir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMhwABHCAwTToCyBCNKtwDKVR5CJeXzkwPNcNEZXeLMZccxIFAAJERFZ%2FcDrdfp0jyRDfrcszwspIpUB34No7YoluXW6vibd6MacfpMvHiRTTT9SdCVf0ewpkrOtr0hY4TXfsG%2F3yJ0aaTV%2BHkZwBiufyDetL6yGdRYNb%2B8Lq0BggqmajS%2FV%2BE%2BhoOGOHEcO52CO%2F80ZkSVofp0B4jbhDfge2XBgGNDzjtnJaIc4t6lFFpHReEdJ9GcBdMNk8jCwgXpii8jBd6kwjNvcsUQf5P%2Ft9hXMyftUab%2Fu2fsZTOq9zDuWpHyB7gUezJP8k%2FHJHIt8QSA%2BCep1MDayrJCDKIGzyF4%2FkgYRVCz9ma%2FtYXmBNm5uOVZJTA00v8om3jcnVoTRs1LELhg5Ay7ck86JM69RlLqPu6Uz9dApRbi5SnVgI%2BqCG3Chx3eNgkOQVUpiMGYpt3zc3Qwe091F%2Bf8LJaempFQc6i4ZtCFeG9yDm%2Bz33fJqWV%2BwUq38pcUx3L6VKdQI9jy1pOB6U2A0Voch8l5yEqrZ20WZcuTeLB%2Fivclw15E7bAwUz4h5xxe7b6m59r3LFR0bwnb0DZatmKyxJSHYWU9OWVKbFEavwxFfuZxz12QDWKcnLan9S1fSp9CKzsx1S4%2FBiEDd4FAccwpOiKzAY6pgHd%2FQ1tLeW1czLWSbZ04sEh%2B0gU0z0nKXpRLMFligKoygH7XD8CmRTL41N7jSqUciwYXOu%2Ff%2FMkaX5ph9CmOfHP%2BeND036Axh9m6w%2BSU6ViT6fEZg2hnJMPk6KoFXdPtipyYGoBcOXfnPPtlz8OkKoQt4urUGEUCmgR2vqYXs79eTydIJYOWywSY96gijoO7pV%2FV877fzMr%2Frv0oo%2Ft5mQ%2FAav7IrGa&X-Amz-Signature=0cd95a8e286ac80e187ea8d370227f610edcd282bdae6f2d2e19e7ef7dd1c2f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

