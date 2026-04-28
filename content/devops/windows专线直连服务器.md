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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCZIO7EJ%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDcWpuPHw%2FeFfY6wJM8giyiqBicLgdB7VqUI6AV%2BMxuAgIhAKBTPXdghRSxZybVpQ1HFGw64M%2BEoceSwisqD71WnpT%2FKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwtaCDgClEQRI9TSwoq3AMLOe1Uyz41%2F5lyq4Wod0CDzGx78%2Fp7HeXgtlGGcJj7%2Bgm8kX3KD2bHnxBN%2FlUgVmCTl%2F%2Bjn9VAdMxn%2ByFtMdtXur4iC47m9gM42WPdR207JIc%2FVGRsl0qGsRx3KpEEUDi8jxY14rMAwKoPbr3xUfOqhIcyGLMMoLDN8vuZA95xnTpavQ%2BBoY5vtbksAqoE8XL3G6bDpQXX%2BP6ze9fEd9XoeC6yQsjpR7Ds1D5TB3uryYoIAzmXfUV%2F47ScYftg0Te%2FOg%2BnJmnKuIS0Wf%2B52iBrtDeJ9a2hynMGJGXKWDyAF3sSYVMiBho2%2FN89AqxLAO2IvJN3jzA9%2F2mIROSYFr9I7tkCDtWRCmLGF3VMMmkBoI%2FxoyYTZfXEvSL2mGK9wzy%2FneEpKyPgFISeu%2Bfgi8tIlPeJsinEJGwWGU8iQyMaCnYhEnajzfrJUvqzqFyJkgsWDfp%2B69vla1y09GSgj%2FkgpNtfzy%2F%2Fo%2B%2FZVd3T5bbtqZcTxgSWQs54iuYkPfDwQXe0UmX4UmTYMfBCJwXLK0RNqZyNxpAAWV0UBquQbXqD%2FtCJnSVwYOpOk5tCyxxVlzevUnGkqNJD3C7YtjmZkB0cSFwv3jfy%2Bb48dQDfBx%2BLR%2BQPVqJQiDgeuLf5tzC37sDPBjqkAWtDVbgatKlyMhgj9UQQZxAWHC4zRzcuIAZw3cZMxe8y7lRPrGGN43fOalVoqQDHL5r17Z6LGJBRW1WHG7YrkHdnHH13d%2BNr6IkMAZLkPrIVkecYU0l6DQrCrxDF2AvttRuwqUNkIPCPVaHeZoRJDKFt6J7q17znlrljO90FTy5aKLYaDgqcEBZLETBd5PlMJKO1dEdONeGQIgrk9WfaUrEgxxo7&X-Amz-Signature=65f2f5f946e6e8493359779d9d385bbc6b3340ba77e148d84a56bd61607f0881&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

