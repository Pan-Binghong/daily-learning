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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKQEV5CS%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxWzVmCB5Smy042UiLQqPv3Ai5nrMT4MGsLMInmquxdAiA%2FDbhFRHW78k7gI3nOmss%2By%2BIrvCVtfJbeMR5xJwbH4CqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdiK35AnUbFx8%2BMt2KtwDq6mg0Dte2Yji0NOJI8rhJ%2Fz9ZH60oSUnvHBVeCEcENdDUAtXpNjGLDpAf57SSqPMCJmXfDqTlZIQ%2BWWv96eXamL9uzA4ZwyfhTIPbPw9sgfIR7BU5HD1g3sBzbBkv8EwNF4%2B01YXhm%2BZMnQHuMISvcN9WagK1ZP4hsFHD8W6Q1H53c3BNvD56JLM3BlCFRf4Uw5GtxnNwVcOqkMLpFlTHHuOdRTRx5TIAJRQTgchHR9keRag8vvymIj2zYwF30XTSPzPI4j4viICwjMwQNMkh83KvIDURz5zZgHpCj5BBqnP4fN5WzPaEZ6um0V3JZ8b8cEzsetAJei5FrR93TRN0mTJwUlDXmXf84gJ5i3Yy2sO1AHwykqQGY5xjQEHTnutrUpdYhUptpo4E6cS3IUeLkoicrxIKwwjm3C36EnKlZiJhajZR4HXre6VvQ0sA2qgTAfp7861D5QV0wzs3efseGiGI6fgK4vRl84rVQObvDtcIDMj%2Fpt4nZYMdK8NmKQzAADc6MMw9%2FY6pj5isUMgsTJl6SUVtkKySipvnky5e79vcg%2F9xwv5xDxypjoynmlbNVCK7JWc8v5n5RyiKide9e156UJYY599GlOHRklE1HDsE9T7iA2qRbM3Iw8w%2BrDMzgY6pgEukx6E%2FWp33t3zoW25q30Xz7ONmKxQxjZ%2BYinHO%2FMH8vq2PX21IftTLdC7Up%2FI%2FSCQLqaOijkAcJhZcdpkhzA4pem8ZCv00yAbR9Eg%2FBAb1y4zblpQy21kAm8CSc30SHd1SFh8yOvLcRYRR7VQBUzYz%2Ff6zcz0Z2IK4nTDu24XC6WPYxDZIXadXsgYx1M%2FZq4w3jIo5LhSmEvapb6GCIVvah0f%2FJUr&X-Amz-Signature=d022ab9a177fa1cba1a16188a8298ef757468874a638ffb41de562ffb823a31d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKQEV5CS%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxWzVmCB5Smy042UiLQqPv3Ai5nrMT4MGsLMInmquxdAiA%2FDbhFRHW78k7gI3nOmss%2By%2BIrvCVtfJbeMR5xJwbH4CqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdiK35AnUbFx8%2BMt2KtwDq6mg0Dte2Yji0NOJI8rhJ%2Fz9ZH60oSUnvHBVeCEcENdDUAtXpNjGLDpAf57SSqPMCJmXfDqTlZIQ%2BWWv96eXamL9uzA4ZwyfhTIPbPw9sgfIR7BU5HD1g3sBzbBkv8EwNF4%2B01YXhm%2BZMnQHuMISvcN9WagK1ZP4hsFHD8W6Q1H53c3BNvD56JLM3BlCFRf4Uw5GtxnNwVcOqkMLpFlTHHuOdRTRx5TIAJRQTgchHR9keRag8vvymIj2zYwF30XTSPzPI4j4viICwjMwQNMkh83KvIDURz5zZgHpCj5BBqnP4fN5WzPaEZ6um0V3JZ8b8cEzsetAJei5FrR93TRN0mTJwUlDXmXf84gJ5i3Yy2sO1AHwykqQGY5xjQEHTnutrUpdYhUptpo4E6cS3IUeLkoicrxIKwwjm3C36EnKlZiJhajZR4HXre6VvQ0sA2qgTAfp7861D5QV0wzs3efseGiGI6fgK4vRl84rVQObvDtcIDMj%2Fpt4nZYMdK8NmKQzAADc6MMw9%2FY6pj5isUMgsTJl6SUVtkKySipvnky5e79vcg%2F9xwv5xDxypjoynmlbNVCK7JWc8v5n5RyiKide9e156UJYY599GlOHRklE1HDsE9T7iA2qRbM3Iw8w%2BrDMzgY6pgEukx6E%2FWp33t3zoW25q30Xz7ONmKxQxjZ%2BYinHO%2FMH8vq2PX21IftTLdC7Up%2FI%2FSCQLqaOijkAcJhZcdpkhzA4pem8ZCv00yAbR9Eg%2FBAb1y4zblpQy21kAm8CSc30SHd1SFh8yOvLcRYRR7VQBUzYz%2Ff6zcz0Z2IK4nTDu24XC6WPYxDZIXadXsgYx1M%2FZq4w3jIo5LhSmEvapb6GCIVvah0f%2FJUr&X-Amz-Signature=354c40d8bb4d4f7b6d72ec48969d4b885111955b8a051d82cbb47f0ce9f9c7f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

