---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665L2PTVAT%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQCvitrPVcm9zACMQ0vnmqCTXGmg7YGI6dZYxpC6Cg0rlAIhANR6LotFhM4EWl%2BJwQlCi934Kpsc2FURJk2MuWOvzH9%2FKv8DCBsQABoMNjM3NDIzMTgzODA1Igxdbya3IMSF6Xf7Oj8q3APk4YDqT%2FpAjFItgq8%2F8u9LaWFeUx3V%2FbbJnje17Y0zyM4dgfuFqbZI9urcOmLcArTjhMijT%2FihTd8tbWayugAkMg9Kv0fRQYm9qY5kdycXeOsiItyCHkp5VTQHzTm5JGRFUjnT%2BDAs3YGnfJUGrrF1AX3OAmvqPcjkMMZPeKHQsai4g3x6prQrO8cvPcXhxf4eEQN1610wF9ftiH%2FQIjAzcuHTpPBlWv7zrilIMhs27MNh9CqcAXmSQYCOogBuWGlYyy7amZuJWSe1Od0qDjNEkz3df6EAObLsNiTcoTxiAtn2fZcHN%2BXDXQcn2yrGhpyaT855iE6F9dK2yS8pamYTrOlQcs%2FJ96Yh1VTTxM61Rz%2Fd7B5K8DrRDKD%2FXxjbjc7%2FOm1Y2XQVpRhnunS9CX%2FpWpBY57X9Ig3OZYXH0JOGvheihgxJmGSXBCrqh3pTuAskfDOihpOC49Oegsuq2I2wjQF7RdpoETSZf1XCcEc2EVIUg7ER14dCBWlTptGiYP60jMA7q3zDU1gxoSpzHT5mXgDUiI0mfQIZITOpsv2%2B2Bjz7KduGazd%2FT6Aewr2fNelXmwCnpEgJMPg1mxzFM8mXk3Gz7i7o8qax7w0gzAeDXcLbpbIpaEPgeb28DCnoYTJBjqkASteDemXy%2BNaYMkJXuKdu%2B7mx7S4U1ZSZcd8yHsPlXts1w9u5qS9LhNM2c8QoopWPp6xwDd63AgCOyIQNWddM94t%2B9RqcUEY2BKbcoTq0PzVdPiGqLBvB6ktn99%2FzKCo4yLG3mrFf%2FkbReqVXqgLiTl5t7llfdauxupBLS2t4X5oeXJA1K8OJ1fc4endMBg3pbaPhXxZe9xmzsS4qGDEjRBU2egP&X-Amz-Signature=407a8e9cb260d929c1aa13f557cd5b6431e5112ba861be8fa6d96204c034ad4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665L2PTVAT%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQCvitrPVcm9zACMQ0vnmqCTXGmg7YGI6dZYxpC6Cg0rlAIhANR6LotFhM4EWl%2BJwQlCi934Kpsc2FURJk2MuWOvzH9%2FKv8DCBsQABoMNjM3NDIzMTgzODA1Igxdbya3IMSF6Xf7Oj8q3APk4YDqT%2FpAjFItgq8%2F8u9LaWFeUx3V%2FbbJnje17Y0zyM4dgfuFqbZI9urcOmLcArTjhMijT%2FihTd8tbWayugAkMg9Kv0fRQYm9qY5kdycXeOsiItyCHkp5VTQHzTm5JGRFUjnT%2BDAs3YGnfJUGrrF1AX3OAmvqPcjkMMZPeKHQsai4g3x6prQrO8cvPcXhxf4eEQN1610wF9ftiH%2FQIjAzcuHTpPBlWv7zrilIMhs27MNh9CqcAXmSQYCOogBuWGlYyy7amZuJWSe1Od0qDjNEkz3df6EAObLsNiTcoTxiAtn2fZcHN%2BXDXQcn2yrGhpyaT855iE6F9dK2yS8pamYTrOlQcs%2FJ96Yh1VTTxM61Rz%2Fd7B5K8DrRDKD%2FXxjbjc7%2FOm1Y2XQVpRhnunS9CX%2FpWpBY57X9Ig3OZYXH0JOGvheihgxJmGSXBCrqh3pTuAskfDOihpOC49Oegsuq2I2wjQF7RdpoETSZf1XCcEc2EVIUg7ER14dCBWlTptGiYP60jMA7q3zDU1gxoSpzHT5mXgDUiI0mfQIZITOpsv2%2B2Bjz7KduGazd%2FT6Aewr2fNelXmwCnpEgJMPg1mxzFM8mXk3Gz7i7o8qax7w0gzAeDXcLbpbIpaEPgeb28DCnoYTJBjqkASteDemXy%2BNaYMkJXuKdu%2B7mx7S4U1ZSZcd8yHsPlXts1w9u5qS9LhNM2c8QoopWPp6xwDd63AgCOyIQNWddM94t%2B9RqcUEY2BKbcoTq0PzVdPiGqLBvB6ktn99%2FzKCo4yLG3mrFf%2FkbReqVXqgLiTl5t7llfdauxupBLS2t4X5oeXJA1K8OJ1fc4endMBg3pbaPhXxZe9xmzsS4qGDEjRBU2egP&X-Amz-Signature=4d4ee1316a554fb2cf87fda4cb6e31e9fe562bde741f88a8e39a614c078d2627&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

