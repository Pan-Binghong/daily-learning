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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNJVLGU%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqWaQKz3Ia%2FqTHzsj%2Brqgjm3TCAp0Vvj2nYLzgDSiQ2AiAQXYj%2FjfTeJmSsILFR1xAhZnRSQGcAuTFBe2lnNBGFEyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FXqIyLOmQ35gvDgnKtwDpnjIrCe81LfwRSlyZ26UAdSWFGLPS1E4wSWzMSaWIXPrQQg7V6NFnbtIBu6hAnOCZ73zTiCF4Mol0%2FiDB3fW5zTf9kY6uXNFSX3npa%2FApLWAlWFt7nziy7sbdkMgQKaU66U8aj9MDsf6tcEgtK96zXpAEg8IG1PFGK%2FYAYiGbn0myvIlYAaSW9sThAbnR5DQePaP9A9pKIkddhHfD1FzinzTbC4j%2BNuBSTIqBXVfjCHH5%2F7Rjc2tz41JCijBSdZTcfc%2BCsOfPRYIontZsUwaGvEMzLZxp2l4N%2FCDWHOIZVxjcTTose%2Fda063QmvTZ2of7vq84mU%2FyEm4OXcZWndGp96laJZ2BcBfAVHUvJJmBTXvLLWAoOkurn6C%2BUq0kVCFyaI48yq1JlsMt1y82pEILHc9Z9R9QD7oe%2FcxT5xps0uk7x%2B9jFMx%2BLwCV7ByqH3l3a2ZBvVQbXjSzlTXWCrLze5YG17k6d0CSRnoMmDgP9td6ahSVDSZhEPV0mkM2YX5MpJ%2FEUlJPeYl0NZNHVmR8u4KxezyZXwQbyTpeNcm1GR7JsLJsLpInS6mTTYEQHiubAab%2FJCg4Vh8JMBD23JMaaAqDmexJ1Yi3y91SxZRWUjTQDa6FaGa195ssM4w3MOqzAY6pgFPnt7jTGipxp07j5FKgHPWAr0c3MF%2BTJagN%2BRNjMf1U%2BQy0%2Bd2jgTc%2FUDv6vy%2FEuvANh84JcRG7T4DtFC%2Fsh0hcNP4U5MGxwJPG7D5zGZhkGzXYW8FhG8TVEQAxRqlkhbuyXJdez58ZjS764Mvc9aeZZLQmXw2ha%2FyVMs1gWyfon3LINPJIOyUNySC4qJfNA585Mmhs%2FCzcq78sR%2BD8d4OHuG5C8%2Fb&X-Amz-Signature=2dca92f074f9c35038b4e94bb97fa2670e7c5c5a2b41014b676c548494807c8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNJVLGU%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqWaQKz3Ia%2FqTHzsj%2Brqgjm3TCAp0Vvj2nYLzgDSiQ2AiAQXYj%2FjfTeJmSsILFR1xAhZnRSQGcAuTFBe2lnNBGFEyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FXqIyLOmQ35gvDgnKtwDpnjIrCe81LfwRSlyZ26UAdSWFGLPS1E4wSWzMSaWIXPrQQg7V6NFnbtIBu6hAnOCZ73zTiCF4Mol0%2FiDB3fW5zTf9kY6uXNFSX3npa%2FApLWAlWFt7nziy7sbdkMgQKaU66U8aj9MDsf6tcEgtK96zXpAEg8IG1PFGK%2FYAYiGbn0myvIlYAaSW9sThAbnR5DQePaP9A9pKIkddhHfD1FzinzTbC4j%2BNuBSTIqBXVfjCHH5%2F7Rjc2tz41JCijBSdZTcfc%2BCsOfPRYIontZsUwaGvEMzLZxp2l4N%2FCDWHOIZVxjcTTose%2Fda063QmvTZ2of7vq84mU%2FyEm4OXcZWndGp96laJZ2BcBfAVHUvJJmBTXvLLWAoOkurn6C%2BUq0kVCFyaI48yq1JlsMt1y82pEILHc9Z9R9QD7oe%2FcxT5xps0uk7x%2B9jFMx%2BLwCV7ByqH3l3a2ZBvVQbXjSzlTXWCrLze5YG17k6d0CSRnoMmDgP9td6ahSVDSZhEPV0mkM2YX5MpJ%2FEUlJPeYl0NZNHVmR8u4KxezyZXwQbyTpeNcm1GR7JsLJsLpInS6mTTYEQHiubAab%2FJCg4Vh8JMBD23JMaaAqDmexJ1Yi3y91SxZRWUjTQDa6FaGa195ssM4w3MOqzAY6pgFPnt7jTGipxp07j5FKgHPWAr0c3MF%2BTJagN%2BRNjMf1U%2BQy0%2Bd2jgTc%2FUDv6vy%2FEuvANh84JcRG7T4DtFC%2Fsh0hcNP4U5MGxwJPG7D5zGZhkGzXYW8FhG8TVEQAxRqlkhbuyXJdez58ZjS764Mvc9aeZZLQmXw2ha%2FyVMs1gWyfon3LINPJIOyUNySC4qJfNA585Mmhs%2FCzcq78sR%2BD8d4OHuG5C8%2Fb&X-Amz-Signature=5a7ab9b727074744a0f4dbc73809f6828da7c234ccd817e611bc28814cf1f4c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

