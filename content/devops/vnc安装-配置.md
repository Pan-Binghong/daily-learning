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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECCXHXW%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDF4yJexnc5Q2IHwMT7H8RILVoTxb5YcTV0H8eQFcwEvQIhAISR1ze9ZVSJbfyi%2FHikhyPOYe%2Freeof97f0mSfBUts9Kv8DCFQQABoMNjM3NDIzMTgzODA1Igx47gOYgP8lbIqY4FQq3AMB5O%2FgkvFvE%2FP84FM6wyV898OhS3pomffTlvDg%2B4zGVMzVK2UltHPQJLQa6Rm0wDzJknG6K4Q5SMxy4jqL8L0XP%2BTLK5yc1L5y7RbFuZgWv7YTStqvd1B9TO3r%2B%2FILLz%2BKdx%2Fi41%2FWu6gFw5M3qwC0qxyKGTMm4nhYEWhlh%2BSUNTmAi%2BA6LRI0qNn3F%2BB3RqJGj%2FilYM1nGKkxnBGZytCRPYLGA0lA%2BiwdN25dBtJXHE7eolmIupbNBfOnDu4MnARjfSOhT8pTvr3ZUaZKznI0Cv%2Bx%2FkoSLcMHR6fSVp4zvj%2B5Y2OELxPxNPhvQqm1L0PjPECQI4OZ9h%2BRmfYP1yzYnGqwgnOMUCULbvgk%2BSS5XrhHldwHRtxBsUBoosSlZDZFcegx1Xsi%2FtzI8V4FzGNhQr%2BaXdK8Nw6pAl5UnWgf3OOS7UEzpW8lCwhXfBtB6WKLC%2BN3zSQ9Qf5For0gFt%2BhG4eyakcqU8kGyqhXb%2BeyA1cIdsVClZrWg%2B%2BPb6wQJ%2BqBF0rHFBRsHrz8oSis8WVLT4IhCWTuM%2BVzj6NdRUmZkbKEu%2F9tOtPJ9amuxwU%2BvlPgjv4ocsupJfFWPOCJzbNe4zetfWlEkh7un%2B91M80pljGvyVdJE4%2BRV4VFNjDewMPNBjqkAexTzegm1B6aoxZrQvfoMOL7nMEdR9W9gPwAOu%2BGOhm2PeqHsxTLr4ZhEXaxUg8OS9ws6Y9eI2HGWRwIli2LErrJO2EWXZafzADkduYNGtmvpL6REJPM7110sbrqeG83AVgUh%2BYZMKvQS%2FIRVN9aMIB4UTpQBmtgCK7tBg0mk%2Fsu%2FwlZN7EGEhF2SQVWfG0sMBGtFNnkTXC1gQtI1O4T0bCuSz6M&X-Amz-Signature=e2f9db2c891c1cbb562e2afc1629fa059eed866674e7ffc0b715bc365fe4eb96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECCXHXW%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDF4yJexnc5Q2IHwMT7H8RILVoTxb5YcTV0H8eQFcwEvQIhAISR1ze9ZVSJbfyi%2FHikhyPOYe%2Freeof97f0mSfBUts9Kv8DCFQQABoMNjM3NDIzMTgzODA1Igx47gOYgP8lbIqY4FQq3AMB5O%2FgkvFvE%2FP84FM6wyV898OhS3pomffTlvDg%2B4zGVMzVK2UltHPQJLQa6Rm0wDzJknG6K4Q5SMxy4jqL8L0XP%2BTLK5yc1L5y7RbFuZgWv7YTStqvd1B9TO3r%2B%2FILLz%2BKdx%2Fi41%2FWu6gFw5M3qwC0qxyKGTMm4nhYEWhlh%2BSUNTmAi%2BA6LRI0qNn3F%2BB3RqJGj%2FilYM1nGKkxnBGZytCRPYLGA0lA%2BiwdN25dBtJXHE7eolmIupbNBfOnDu4MnARjfSOhT8pTvr3ZUaZKznI0Cv%2Bx%2FkoSLcMHR6fSVp4zvj%2B5Y2OELxPxNPhvQqm1L0PjPECQI4OZ9h%2BRmfYP1yzYnGqwgnOMUCULbvgk%2BSS5XrhHldwHRtxBsUBoosSlZDZFcegx1Xsi%2FtzI8V4FzGNhQr%2BaXdK8Nw6pAl5UnWgf3OOS7UEzpW8lCwhXfBtB6WKLC%2BN3zSQ9Qf5For0gFt%2BhG4eyakcqU8kGyqhXb%2BeyA1cIdsVClZrWg%2B%2BPb6wQJ%2BqBF0rHFBRsHrz8oSis8WVLT4IhCWTuM%2BVzj6NdRUmZkbKEu%2F9tOtPJ9amuxwU%2BvlPgjv4ocsupJfFWPOCJzbNe4zetfWlEkh7un%2B91M80pljGvyVdJE4%2BRV4VFNjDewMPNBjqkAexTzegm1B6aoxZrQvfoMOL7nMEdR9W9gPwAOu%2BGOhm2PeqHsxTLr4ZhEXaxUg8OS9ws6Y9eI2HGWRwIli2LErrJO2EWXZafzADkduYNGtmvpL6REJPM7110sbrqeG83AVgUh%2BYZMKvQS%2FIRVN9aMIB4UTpQBmtgCK7tBg0mk%2Fsu%2FwlZN7EGEhF2SQVWfG0sMBGtFNnkTXC1gQtI1O4T0bCuSz6M&X-Amz-Signature=6e256c83902b429f7e853eccb82a7b92dbbb510632f947b45e7ac7417af12a92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

