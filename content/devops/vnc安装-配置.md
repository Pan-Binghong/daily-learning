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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TGZMPLK%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFMZeikqBF%2BY9ZHJ0ORMAp8oK1iwZQAba6SQEQjgqy11AiA9tcK%2FOpCzCdUgNhGpUQPc0BboWomNe8uafo7WanjQ8SqIBAjc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZLjU69RuYhWUGbr%2BKtwD%2BU6YQBZItsCoVl8iTi1ojpsGGvHeVHfWJomRumea2reLkWWz6fXBG2SIuYEcUqlTZakTspegYmrQS4N26Z%2BM%2BLiFS2PSQ0LOPDWAeD1gIngjCvj8aUSf8OMqkE6cibeZePP%2Bz%2By5US0%2B2HOGwnrdKAzPw6i3%2FCHel5WqbJZgDHqAzlqfeYpZ7Nycbudbg5le7dKbszlQFAmO6xNYpMz8XW1u7SLqrWhxET71%2BhautC2zu7wdrbGBuihft4edDWc4SLdUl2xsEKOkewr7ZM70%2FUzC9LKGKJQfIgyyrM1Djvh91kFYS0VIV%2Furis%2BWjc9mk3AUQzcb0gCDIZkSq150PtNiF6g0fkjPj%2FJsEaPQmcw4M2LVGTO%2Ftwxql8x6xRbazqHN3qVtd%2Bxnf9LOjRELNsIel5LYdJHhHMyfHww95p8jn6g1MeFIsM1rPYUjDbQGo4FgQd2ZFW1hHfFN5M%2By9jUVW2Rxfjl0mfgI3I7mZBB3YHh2FT2ds20PwE3st%2BQpQXGb45O1RrldsMcU9jnjWlHvoXHMQJWpWVhIeU2Frh5HH8e84%2FgQAN0gdbKDR68HvQ%2BLtrrORbg443s55JkSrRqPuw%2FGf6u6sLJtusL4m1N%2FLepVX5t7WC9ipk8w%2BYipzQY6pgGpo8LD%2Byx2AenVtTSyfMhwSGPlSYHX%2FxS1JN6I0j5xLLAcfURvgKQwdbNWmGgAQpJUUNvmWEbOmt5orao4IcNulGBYZBtTBcAjnxF%2F8l0%2FQdmUG2Fxi%2Fcs4gcXatGd30ddp%2BTyuHTDgub6EoG767ymNpJtnugHoVKfEODT6AvO6xw0aKjo81sfK8u4wO2ANvGmOQ0E2dxyuIT9auLQJX7YAZqPOOC7&X-Amz-Signature=9c80328aa73a381f7a2d5b18d5b4d6500f9acccf6b9c88c46e0a0ed5a19cb9f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TGZMPLK%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFMZeikqBF%2BY9ZHJ0ORMAp8oK1iwZQAba6SQEQjgqy11AiA9tcK%2FOpCzCdUgNhGpUQPc0BboWomNe8uafo7WanjQ8SqIBAjc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZLjU69RuYhWUGbr%2BKtwD%2BU6YQBZItsCoVl8iTi1ojpsGGvHeVHfWJomRumea2reLkWWz6fXBG2SIuYEcUqlTZakTspegYmrQS4N26Z%2BM%2BLiFS2PSQ0LOPDWAeD1gIngjCvj8aUSf8OMqkE6cibeZePP%2Bz%2By5US0%2B2HOGwnrdKAzPw6i3%2FCHel5WqbJZgDHqAzlqfeYpZ7Nycbudbg5le7dKbszlQFAmO6xNYpMz8XW1u7SLqrWhxET71%2BhautC2zu7wdrbGBuihft4edDWc4SLdUl2xsEKOkewr7ZM70%2FUzC9LKGKJQfIgyyrM1Djvh91kFYS0VIV%2Furis%2BWjc9mk3AUQzcb0gCDIZkSq150PtNiF6g0fkjPj%2FJsEaPQmcw4M2LVGTO%2Ftwxql8x6xRbazqHN3qVtd%2Bxnf9LOjRELNsIel5LYdJHhHMyfHww95p8jn6g1MeFIsM1rPYUjDbQGo4FgQd2ZFW1hHfFN5M%2By9jUVW2Rxfjl0mfgI3I7mZBB3YHh2FT2ds20PwE3st%2BQpQXGb45O1RrldsMcU9jnjWlHvoXHMQJWpWVhIeU2Frh5HH8e84%2FgQAN0gdbKDR68HvQ%2BLtrrORbg443s55JkSrRqPuw%2FGf6u6sLJtusL4m1N%2FLepVX5t7WC9ipk8w%2BYipzQY6pgGpo8LD%2Byx2AenVtTSyfMhwSGPlSYHX%2FxS1JN6I0j5xLLAcfURvgKQwdbNWmGgAQpJUUNvmWEbOmt5orao4IcNulGBYZBtTBcAjnxF%2F8l0%2FQdmUG2Fxi%2Fcs4gcXatGd30ddp%2BTyuHTDgub6EoG767ymNpJtnugHoVKfEODT6AvO6xw0aKjo81sfK8u4wO2ANvGmOQ0E2dxyuIT9auLQJX7YAZqPOOC7&X-Amz-Signature=de02c9340b865632eb1ef3914af6133dd5e81148ab7d53d2f1e500ef9bae3bc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

